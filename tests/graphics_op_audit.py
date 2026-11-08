"""Check graphics calls and watch all six TI-OS operand areas."""

import argparse
from collections import defaultdict
from ctypes import c_void_p, string_at
from itertools import product
from pathlib import Path
import re

from graphics import BG, BUFFER_LEN, CODE, FG, HOOK, NAMES, PLOT, REGS, SAVE, VRAM, Probe, WORKSPACE


OP1 = 0xD005F8
OP_SIZE = 11
FPS = 0xD0258D
DATA = 0xD23A00
STACK = 0xD23F00
CUR_Y = 0xD02FD6
BASE_REGS = (0x0195, 0x0A14, 50, 30, DATA, 0xD00080,
             0x5A43, 0x173052, 0x245063, 0xB91074, 0)
PALETTE = (0xFFFF, 0x001F, 0xF800, 0x0000, 0xF81F, 0x04E0, 0xFC64, 0xB100,
           0x0010, 0x049F, 0xFFE0, 0xFFFF, 0xE71C, 0xC618, 0x8C51, 0x52AA)


def entries():
    result = {}
    for path in (Path(__file__).resolve().parents[1] / "syscalls/all").glob("*.md"):
        page = path.read_text(encoding="utf-8")
        if "    category: Graphics\n" in page:
            result[path.stem] = int(re.search(r"    address: \$([0-9A-F]+)", page)[1], 16)
    return result


def real(value):
    if value == 0:
        return bytes(9)
    assert -9 <= value <= 9
    return bytes((0x80 if value < 0 else 0, 0x80, abs(value) << 4)) + bytes(6)


class Audit(Probe):
    def __init__(self, image):
        super().__init__(image)
        self.addresses = entries()
        self.core.get_op_access.restype = c_void_p
        self.read_ops = defaultdict(set)
        self.wrote_ops = defaultdict(set)
        self.changed_ops = defaultdict(set)

    def setup(self, seed=0):
        self.prepare(seed)
        self.put(0xD01501, 265, 2)
        self.put(0xD014FE, 165)

    def fps(self, *values):
        self.write(DATA, b"".join(map(real, values)))
        self.put(FPS, DATA + 9 * len(values), 3)

    def operands(self, *values):
        for i, value in enumerate(values):
            self.write(OP1 + i * OP_SIZE, real(value))

    def call(self, name, **overrides):
        inputs = dict(zip(NAMES, BASE_REGS))
        inputs.update(overrides)
        regs = REGS(*(inputs[key] for key in NAMES))
        before = self.read(OP1, OP_SIZE * 6)
        status = self.core.invoke(self.addresses[name], regs, VRAM)
        assert status == 0, (name, hex(status))
        self.counts[name] += 1
        access = string_at(self.core.get_op_access(), len(before))
        after = self.read(OP1, len(before))
        assert all(old == new or flags & 2 for old, new, flags in zip(before, after, access)), name
        for i, (old, new, flags) in enumerate(zip(before, after, access)):
            op = i // OP_SIZE + 1
            if flags & 1:
                self.read_ops[name].add(op)
            if flags & 2:
                self.wrote_ops[name].add(op)
            if old != new:
                self.changed_ops[name].add(op)
        return dict(zip(NAMES, regs))


def check_coordinates(p):
    for name, full, x, y in product(("IBounds", "IBoundsFull"), range(2),
                                     (0, 265, 266, 319, 320, 0xFFFFFF), (0, 164, 165, 239, 240)):
        p.setup()
        p.flags("full", b2=full)
        regs = p.call(name, de=x, bc=y)
        width, height = (320, 240) if full or name == "IBoundsFull" else (266, 165)
        assert regs["af"] & 1 == (x >= width or y >= height)
    for full, split, x, y in product(range(2), range(2), (0, 1, 12, 13), (0, 31, 164)):
        p.setup()
        p.flags("full", b2=full)
        p.flags("split", b1=split)
        regs = p.call("IOffset", de=x, bc=y, hl=0)
        height = 240 if full else 165
        stride = 160 if full else 93 if split else 133
        assert regs["hl"] == (height - 1 - y) * stride + x // 2
        assert regs["af"] >> 8 == (0x0F if x & 1 else 0xF0)


def check_setup(p):
    for index, expected in enumerate(PALETTE):
        p.setup()
        assert p.call("GetColorValue", af=index << 8)["de"] == expected, index
    for fg, color in product(range(2), (0, 0xFFFF, 0xAB1234, 0x65657E)):
        p.setup()
        p.put(STACK, color, 3)
        slot = FG if fg else BG
        p.call("os_SetDrawFGColor" if fg else "os_SetDrawBGColor")
        assert p.get(slot, 2) == color & 0xFFFF
        name = "os_GetDrawFGColor" if fg else "os_GetDrawBGColor_BROKEN"
        assert p.call(name, hl=0xABCD12)["hl"] == color & 0xFFFF
    for row in (0, 30, 117, 239):
        p.setup()
        p.put(STACK, row, 3)
        p.call("os_SetYDrawLocation")
        assert p.call("os_GetYDrawLocation")["hl"] == row
    for app, row in ((0x40, 0), (0x58, 30)):
        p.setup()
        p.put(0xD007E0, app)
        p.call("os_InitDrawing")
        assert (p.get(CUR_Y, 3), p.get(FG, 2)) == (row, 0)
        assert (p.get(0xD02FDC, 3), p.get(0xD02FE0, 3), p.get(0xD02FE3, 3)) == (240, 640, VRAM)
    for row, count in ((0, 1), (30, 2), (100, 14), (239, 1)):
        p.setup()
        p.put(CUR_Y, row, 3)
        p.put(0xD02FDC, row + count, 3)
        p.put(0xD02FE0, 640, 3)
        p.put(0xD02FE3, VRAM, 3)
        p.call("os_ClearVRAMLines")
        expected = b"\x77" * (640 * row) + b"\xff" * (640 * count) + b"\x77" * (640 * (240-row-count))
        assert p.read(VRAM, len(expected)) == expected
    p.setup()
    p.write(HOOK, bytes((0x83, 0x3E, 1, 0xB7, 0xC9)))
    p.call("SetGraphicsHook", hl=HOOK)
    assert p.get(0xD025F3, 3) == HOOK and p.get(0xD000B5) & 0x80
    before = p.surfaces()
    p.call("IPoint", bc=17, de=12)
    assert p.surfaces() == before
    p.call("ClrGraphicsHook")
    assert not p.get(0xD000B5) & 0x80
    p.call("IPoint", bc=17, de=12)
    assert p.surfaces() != before


def check_shapes(p):
    for mode in range(3):
        for name in ("CPoint", "CPointS", "DarkPnt"):
            p.setup()
            p.fps(1, 2)
            p.operands(1, 2)
            before = p.surfaces()
            p.call(name, af=mode << 8)
            assert p.surfaces()[0] != before[0]
            assert p.get(FPS, 3) == (DATA if name == "CPointS" else DATA + 18)
    reference = None
    for name in ("CLine", "CLines", "UCLines"):
        p.setup()
        p.fps(1, 2, 3, 4)
        p.operands(3, 4, 1, 2)
        before = p.surfaces()[0]
        p.call(name)
        screen = p.surfaces()[0]
        pixels = {i for i in range(0, len(screen), 2) if screen[i:i+2] != before[i:i+2]}
        if reference is None:
            reference = pixels
        assert pixels == reference and len(pixels) > 1
        assert all(screen[i:i+2] == (b"\xff\xff" if name == "UCLines" else b"\xb7\x65") for i in pixels)
        assert p.get(FPS, 3) == (DATA + 36 if name == "CLine" else DATA)
    for name, only in product(("EraseRectBorder", "DrawRectBorderClear"), range(2)):
        p.setup()
        p.flags("buffer", b0=only)
        p.call(name)
        edge = p.get(VRAM + (320 * 10 + 30) * 2, 2)
        inside = p.get(VRAM + (320 * 11 + 31) * 2, 2)
        assert edge == (0x7777 if only else 0xFFFF if name == "EraseRectBorder" else 0x65B7)
        assert inside == (0xFFFF if name == "DrawRectBorderClear" else 0x7777)
    for x, y in ((0, 0), (30, 10), (317, 238)):
        p.setup()
        p.write(DATA, bytes((0, 3, 0, 6, 0, 0xA8)))
        p.call("DrawSprite16bpp", hl=DATA, de=x, bc=y)
        a = VRAM + (320 * y + x) * 2
        assert p.read(a, 6) == b"\0\0\xff\xff\0\0"
        assert p.read(a + 640, 6) == b"\xff\xff\0\0\xff\xff"
    for name in ("GrBufCpy", "GrBufCpyV", "BufCpy"):
        p.setup()
        p.write(PLOT, b"\x11" * BUFFER_LEN)
        p.write(SAVE, b"\x22" * BUFFER_LEN)
        p.call(name, hl=SAVE)
        assert p.get(VRAM + 2 * (46 * 320 + 27), 2) == (0xF800 if name == "BufCpy" else 0x001F)
    for name, mode, hook in product(("ILineNoGraphicsHook", "ILineNoHook"), range(3), range(2)):
        p.setup()
        if hook:
            p.write(HOOK, bytes((0x83, 0x3E, 1, 0xB7, 0xC9)))
            p.call("SetGraphicsHook", hl=HOOK)
        p.put(0xD02AC8, mode)
        p.put(0xD02AD4, 0)
        p.call(name, af=(1 - mode % 2 if name == "ILineNoGraphicsHook" else mode) << 8,
               bc=0x140A, de=30, hl=50)
        screen = p.surfaces()[0]
        color = b"\xff\xff" if mode == 0 else b"\xb7\x65"
        expected = 1 if name == "ILineNoGraphicsHook" else 0 if hook else 21
        assert screen.count(color) == expected


def check_circles(p):
    for name, only, loc, fast in product(("DrawCirc", "GrphCirc"), range(2), range(2), range(2)):
        p.setup()
        p.flags("buffer", b0=only, b4=fast)
        p.flags("plot", b1=loc)
        p.fps(1, 2, 1)
        p.write(0xD0146E, bytes((60, 120, 0, 60, 100, 0)))
        before = p.surfaces()
        p.call(name)
        screen, plot, _ = p.surfaces()
        assert (screen != before[0]) == (not only)
        assert (plot != before[1]) == (not loc or bool(only))
        assert p.get(FPS, 3) == (DATA if name == "DrawCirc" else DATA + 27)
        if name == "GrphCirc" and not only:
            points = [(offset // 2 % 320, offset // 640) for offset in range(0, len(screen), 2)
                      if screen[offset:offset+2] != before[0][offset:offset+2]]
            xs, ys = zip(*points)
            assert (min(xs), min(ys), max(xs), max(ys)) == (107, 130, 147, 170)


def check_other_paths(p):
    tested = set(p.counts)
    for name in sorted(p.addresses.keys() - tested):
        p.setup()
        p.put(0xD01471, 17)
        p.fps(1, 2, 1)
        p.operands(1, 2, 1, 2)
        args = {}
        if name == "ScreenScrollPixelsUp":
            p.write(DATA, bytes((1, 4)))
            p.write(VRAM, b"".join(bytes((row,)) * 640 for row in range(240)))
        elif name == "DrawSplitLine":
            p.flags("split", b0=1)
        elif name == "PlotPt":
            p.put(0xD00087, p.get(0xD00087) | 1)
        elif name == "DrawSPlot":
            p.put(0xD01D45, 0)
        elif name == "DrawTILogo":
            args = {"bc": 120}
        elif name == "DrawThickRectBorder":
            args = {"af": 0}
        p.call(name, **args)
    assert p.addresses.keys() == p.counts.keys()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=WORKSPACE / "ipoint-tests/before-tests.ce")
    args = parser.parse_args()
    probe = Audit(args.state.resolve())
    for check in (check_coordinates, check_setup, check_shapes, check_circles, check_other_paths):
        check(probe)
    print("| Routine | Calls | OP reads | OP writes | OP contents changed at return |")
    print("| --- | ---: | --- | --- | --- |")
    for name in sorted(probe.counts, key=str.lower):
        columns = [", ".join(f"OP{op}" for op in sorted(result[name])) or "None"
                   for result in (probe.read_ops, probe.wrote_ops, probe.changed_ops)]
        print(f"| {name} | {probe.counts[name]} | {' | '.join(columns)} |")
    print(f"\nTotal: {sum(probe.counts.values())} calls across {len(probe.counts)} entries.")


if __name__ == "__main__":
    main()
