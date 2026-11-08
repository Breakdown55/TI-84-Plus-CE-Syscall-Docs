"""Exercise the TI-OS 5.8.2 graphics calls in the headless CEmu core."""

import argparse
from collections import Counter, defaultdict
from ctypes import CDLL, c_char_p, c_uint32, c_void_p, memmove, string_at
from itertools import product
from pathlib import Path
import struct

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parents[1]
RAM = 0xD00000
VRAM = 0xD40000
ALT = 0xD26000
PLOT = 0xD09466
SAVE = 0xD0EA1F
BUFFER_LEN = SAVE - PLOT
SCREEN_LEN = 320 * 240 * 2
FG = 0xD026AC
BG = 0xD026AA
CODE = 0xD026AE
FILL = 0xD02AC0
GRAPH_BG = 0xD02A98
HOOK = 0xD1C020
FLAG_BYTES = {"plot": 0xD00082, "split": 0xD00094, "full": 0xD000AB,
              "hooks": 0xD000B5, "buffer": 0xD000BC, "pixel": 0xD000C6}
NAMES = ("af", "bc", "de", "hl", "ix", "iy", "af'", "bc'", "de'", "hl'", "interrupts")
REGS = (c_uint32 * len(NAMES))
MAY_CHANGE = {
    "ClrLCDFull": {"bc", "de", "hl"}, "ClrLCD": {"af", "bc", "de", "hl"},
    "DarkLine": {"af", "ix"}, "GrBufClr": {"af", "bc", "de", "hl"},
    "PointOn": {"af"}, "VerticalLine": {"af", "bc", "hl", "ix"},
    "HorizontalLine": {"af", "bc", "de", "hl", "ix"},
    "ClrLCDAll": {"bc", "de", "hl"}, "BufIPoint": set(),
    "SetDrawFGColorA": {"af", "de"}, "GraphBGColorToDrawBGColor": {"hl"},
    "SetWhiteDrawBGColor": {"hl"}, "ILine": {"ix"}, "IPoint": set(),
}
ENTRIES = {
    "ClrLCDFull": 0x020808, "ClrLCD": 0x02080C, "DarkLine": 0x020B74,
    "GrBufClr": 0x02109C, "PointOn": 0x0210E4, "VerticalLine": 0x021258,
    "HorizontalLine": 0x02132C, "ClrLCDAll": 0x021A10, "BufIPoint": 0x021A14,
    "SetDrawFGColorA": 0x021A28, "GraphBGColorToDrawBGColor": 0x021BC4,
    "SetWhiteDrawBGColor": 0x021BC8, "ILine": 0x020B78, "IPoint": 0x020B7C,
}


class Probe:
    def __init__(self, image):
        self.core = CDLL(str(HERE / "runner.dll"))
        self.core.load_state.argtypes = (c_char_p,)
        self.core.load_state.restype = c_void_p
        self.core.invoke.argtypes = (c_uint32, REGS, c_uint32)
        self.core.invoke.restype = c_uint32
        self.ram = self.core.load_state(bytes(str(image), "utf-8"))
        if not self.ram:
            raise RuntimeError(f"Could not load {image}")
        self.baseline = self.read(RAM, 0x65800)
        self.counts = Counter()
        self.changed = defaultdict(Counter)

    def read(self, address, length):
        return string_at(self.ram + address - RAM, length)

    def write(self, address, data):
        memmove(self.ram + address - RAM, data, len(data))

    def put(self, address, value, width=1):
        self.write(address, value.to_bytes(width, "little"))

    def get(self, address, width=1):
        return int.from_bytes(self.read(address, width), "little")

    def flags(self, group, **bits):
        address = FLAG_BYTES[group]
        value = self.get(address)
        for key, state in bits.items():
            bit = int(key[1:])
            value = value & ~(1 << bit) | (int(bool(state)) << bit)
        self.put(address, value)

    def prepare(self, seed=0):
        self.write(RAM, self.baseline)
        for group, value in (("plot", 0), ("split", 0), ("full", 0),
                             ("hooks", 0), ("buffer", 0), ("pixel", 0)):
            self.put(FLAG_BYTES[group], value)
        # Clear the mirror, force-draw, and background bits to test ordinary drawing.
        self.put(0xD0009E, self.get(0xD0009E) & 0x7F)
        self.put(0xD000CA, self.get(0xD000CA) & ~4)
        self.put(0xD000CF, self.get(0xD000CF) & ~1)
        self.put(0xD024F3, 0)
        self.put(FG, (0x65B7, 0x1234, 0xF800)[seed % 3], 2)
        self.put(CODE, 3 + seed % 3)
        self.write(VRAM, b"\x77" * SCREEN_LEN)
        self.write(PLOT, bytes([0x55 if seed & 1 else 0]) * BUFFER_LEN)
        self.write(SAVE, bytes([0x66 if seed & 2 else 0]) * BUFFER_LEN)

    def invoke(self, name, seed=0, lcd_base=VRAM, **kwargs):
        inputs = dict(zip(NAMES, (0x5A95 ^ seed, 0xA55C46, 0x00006C, 0x00005B,
                                  0x654300 | seed, 0xD00080, 0x5A43, 0x173052,
                                  0x245063, 0xB91074, seed & 1)))
        inputs.update(kwargs)
        regs = REGS(*(inputs[key] for key in NAMES))
        status = self.core.invoke(ENTRIES[name], regs, lcd_base)
        assert status == 0, (name, hex(status), kwargs)
        outputs = dict(zip(NAMES, regs))
        assert outputs["interrupts"] == inputs["interrupts"] * 3, (name, inputs, outputs)
        self.counts[name] += 1
        changed = tuple(key for key in NAMES[:-1] if outputs[key] != inputs[key])
        assert set(changed) <= MAY_CHANGE[name], (name, changed, inputs, outputs)
        self.changed[name][", ".join(changed) or "none"] += 1
        return outputs

    def surfaces(self):
        return (self.read(VRAM, SCREEN_LEN), self.read(PLOT, BUFFER_LEN), self.read(SAVE, BUFFER_LEN))


def check_wrappers(p):
    targets = {"DarkLine": "ILine", "PointOn": "IPoint", "BufIPoint": "IPoint",
               "HorizontalLine": "ILine", "VerticalLine": "ILine"}
    points = ((12, 17, 39, 41), (41, 37, 12, 17), (265, 164, 265, 164), (319, 239, 312, 232))
    for name, reference in targets.items():
        # Cover all destination combinations, each with in-bounds and boundary fixtures.
        matrix = [(flags, i, 0) for flags in product(range(2), repeat=4) for i in range(len(points))]
        matrix += [((0, 0, 0, 0), i, extra) for i in range(2) for extra in (1, 2, 3)]
        for (full, loc, only, save), i, extra in matrix:
            for mode in range(3) if name == "BufIPoint" else (i % 3,):
                x0, y0, x1, y1 = points[i]
                seed = i + full + loc * 2 + only + save + extra
                af = mode << 8 | (0x95 ^ seed)
                entry = dict(af=af, bc=0xA50000 | y1 << 8 | y0, de=x0, hl=x1)
                normalized = dict(entry)
                if name != "BufIPoint":
                    normalized["af"] = 0x100 | af & 0xFF
                if name == "HorizontalLine":
                    normalized.update(bc=y0 * 257, de=0, hl=265)
                if name == "VerticalLine":
                    normalized.update(af=0x0182 | af & 0x29, bc=0xA5A400, hl=x0)

                for direct in (False, True):
                    p.prepare(seed)
                    p.flags("full", b2=full)
                    p.flags("plot", b1=loc)
                    p.flags("buffer", b0=only, b3=save)
                    p.flags("split", b4=not (direct and name == "BufIPoint"), b5=extra == 1)
                    p.put(0xD024BE, 1)
                    if extra in (2, 3):
                        p.flags("hooks", b7=1)
                        p.write(HOOK, bytes((0x83, 0x3E, extra == 3, 0xB7, 0xC9)))
                        p.put(0xD025F3, HOOK, 3)
                    p.put(0xD01470, 0x57)
                    p.put(0xD01471, y0)
                    p.put(0xD014FE, 165)
                    p.put(0xD01501, 265, 2)
                    if not direct:
                        actual_regs = p.invoke(name, seed, **entry)
                        actual = p.surfaces()
                        actual_flag = p.get(FLAG_BYTES["split"])
                    else:
                        expected_regs = p.invoke(reference, seed, **normalized)
                        assert actual == p.surfaces(), (name, full, loc, only, save, i, extra, mode)
                        assert actual_flag == p.get(FLAG_BYTES["split"]), (name, "write_on_graph")
                        assert actual_regs == expected_regs, (name, full, loc, only, save, i, extra, actual_regs, expected_regs)

    # Independent coordinate checks, including the two separate Y bytes read by HorizontalLine.
    expected = {
        "DarkLine": [(27+x, 210-17) for x in range(12, 40)],
        "PointOn": [(39, 193)], "BufIPoint": [(39, 193)],
        "HorizontalLine": [(27+x, 210-31) for x in range(266)],
        "VerticalLine": [(39, 210-y) for y in range(165)],
    }
    for name, points_to_draw in expected.items():
        p.prepare()
        p.put(0xD01470, 99)
        p.put(0xD01471, 31)
        p.put(0xD014FE, 165)
        p.put(0xD01501, 265, 2)
        p.invoke(name, af=0x100, bc=0x1111, de=12, hl=39)
        screen = bytearray(b"\x77" * SCREEN_LEN)
        for x, y in points_to_draw:
            struct.pack_into("<H", screen, (y * 320 + x) * 2, 0x65B7)
        assert p.read(VRAM, SCREEN_LEN) == screen, name


def check_lcd_clears(p):
    for name in ("ClrLCDAll", "ClrLCDFull", "ClrLCD"):
        for split, override, graph, byte_pixels, seed in product(range(2), range(2), range(2), range(2), range(4)):
            p.prepare(seed)
            p.flags("split", b0=split, b3=override)
            p.flags("plot", b2=graph, b1=seed & 1)
            p.flags("full", b2=seed & 2)
            p.flags("buffer", b0=seed & 1, b3=seed & 2)
            p.flags("pixel", b2=byte_pixels)
            p.put(FILL, 0x1234, 2)
            p.write(ALT, b"\x66" * (320 * 240))
            before = p.surfaces()
            start, end = 30, 239
            if name == "ClrLCDAll":
                start = 0
            elif name == "ClrLCD" and split and not override:
                start, end = (30, 154) if graph else (155, 239)
            regs = p.invoke(name, seed, ALT if byte_pixels else VRAM)
            assert (regs["bc"], regs["de"], regs["hl"]) == (start << 8 | end, 319, 0), name
            assert regs["af"] >> 8 == 0x5A, name
            assert p.get(FILL, 2) == 0xFFFF, name
            assert p.surfaces()[1:] == before[1:], name
            if byte_pixels:
                expected = b"\x66" * (start * 320) + b"\xff" * ((end-start+1)*320) + b"\x66" * ((239-end)*320)
                assert p.read(ALT, 320 * 240) == expected and p.read(VRAM, SCREEN_LEN) == before[0], name
            else:
                expected = b"\x77" * (start * 640) + b"\xff" * ((end-start+1)*640) + b"\x77" * ((239-end)*640)
                assert p.read(VRAM, SCREEN_LEN) == expected and p.read(ALT, 320 * 240) == b"\x66" * (320 * 240), name


def check_graph_clear(p):
    for split, vertical, override, only, save, seed in product(range(2), repeat=6):
        p.prepare(seed)
        p.flags("split", b0=split, b1=vertical, b3=override)
        p.flags("buffer", b0=only, b3=save)
        p.put(PLOT - 1, 0xA9)
        p.write(PLOT, bytes([0x55 if seed else 0xFE]) * BUFFER_LEN)
        p.write(SAVE, b"\x66" * BUFFER_LEN)
        before = p.surfaces()
        regs = p.invoke("GrBufClr", seed)
        count = 10773 if split and not override else 13485 if vertical else BUFFER_LEN
        assert p.read(PLOT, BUFFER_LEN) == b"\x00" * count + before[1][count:], (split, vertical, override)
        assert p.read(VRAM, SCREEN_LEN) == before[0] and p.read(SAVE, BUFFER_LEN) == before[2]
        assert p.get(PLOT - 1) == 0xA9
        assert (regs["bc"], regs["de"], regs["hl"]) == (0, PLOT + count, PLOT + count - 1)


def check_colors(p):
    palette = (0xFFFF, 0x001F, 0xF800, 0x0000, 0xF81F, 0x04E0, 0xFC64, 0xB100,
               0x0010, 0x049F, 0xFFE0, 0xFFFF, 0xE71C, 0xC618, 0x8C51, 0x52AA)
    for index, seed in product(range(len(palette)), range(4)):
        p.prepare(seed)
        before = p.surfaces()
        bg = p.get(BG, 2)
        registers = p.invoke("SetDrawFGColorA", seed, af=index << 8 | 0x95)
        assert p.get(FG, 2) == registers["de"] == palette[index]
        assert registers["af"] >> 8 == index
        assert p.get(CODE) == index and p.get(BG, 2) == bg and p.surfaces() == before

    for name, value, seed in product(("GraphBGColorToDrawBGColor", "SetWhiteDrawBGColor"), palette, range(4)):
        p.prepare(seed)
        p.put(GRAPH_BG, value, 2)
        p.put(BG, value ^ 0xFFFF, 2)
        before = p.surfaces()
        foreground = p.read(FG, 3)
        regs = p.invoke(name, seed)
        assert p.get(BG, 2) == regs["hl"] == (value if name == "GraphBGColorToDrawBGColor" else 0xFFFF)
        assert p.get(GRAPH_BG, 2) == value and p.read(FG, 3) == foreground and p.surfaces() == before


def check_line_extents(p):
    for name, full, extent, fixed in product(("HorizontalLine", "VerticalLine"), range(2), (1, 2, 63, 128, 160), (0, 27, 62)):
        seed = full + extent + fixed
        p.prepare(seed)
        p.flags("full", b2=full)
        p.flags("plot", b1=1)
        p.put(0xD01471, fixed)
        if name == "HorizontalLine":
            p.put(0xD01501, extent - 1, 2)
            p.put(0xD014FE, 165)
            points = ((x, fixed) for x in range(extent))
        else:
            p.put(0xD01501, 265, 2)
            p.put(0xD014FE, extent)
            points = ((fixed, y) for y in range(extent))
        color = p.get(FG, 2)
        screen = bytearray(p.read(VRAM, SCREEN_LEN))
        for x, y in points:
            lcd_x = x + (0 if full else 27)
            lcd_y = (239 if full else 210) - y
            struct.pack_into("<H", screen, (320 * lcd_y + lcd_x) * 2, color)
        p.invoke(name, seed, de=fixed)
        assert p.read(VRAM, SCREEN_LEN) == screen, (name, full, extent, fixed)


def check_point_background(p):
    for mode, only, save, on in product((0, 2), range(2), range(2), range(2)):
        seed = mode + only + save + on
        p.prepare(seed)
        p.flags("split", b4=1)
        p.flags("buffer", b0=only, b3=save)
        p.put(0xD000CF, p.get(0xD000CF) | 1)
        p.put(0xD024F3, 12)  # Solid red, entry 2 in the RGB565 table.
        p.write(PLOT, bytes([0x55 if on else 0]) * BUFFER_LEN)
        p.write(SAVE, bytes([0x66 if on else 0]) * BUFFER_LEN)
        selected = SAVE if save else PLOT
        other = PLOT if save else SAVE
        color = p.get(FG, 2)
        code = p.get(CODE)
        screen, other_before = bytearray(p.read(VRAM, SCREEN_LEN)), p.read(other, BUFFER_LEN)
        expected_buffer = bytearray(p.read(selected, BUFFER_LEN))
        erase = mode == 0 or on
        if erase or not only:
            struct.pack_into("<H", screen, (193 * 320 + 39) * 2, 0xF800 if erase else color)
        offset = (165 - 17 - 1) * 133 + 12 // 2
        expected_buffer[offset] = expected_buffer[offset] & 0x0F | (0 if erase else code << 4)
        p.invoke("BufIPoint", seed, af=mode << 8, bc=17, de=12)
        assert p.read(VRAM, SCREEN_LEN) == screen, (mode, only, save, on)
        assert p.read(selected, BUFFER_LEN) == expected_buffer and p.read(other, BUFFER_LEN) == other_before
        assert p.get(FLAG_BYTES["split"]) & 0x10 == 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=WORKSPACE / "ipoint-tests/before-tests.ce")
    args = parser.parse_args()
    probe = Probe(args.state.resolve())
    for test in (check_wrappers, check_lcd_clears, check_graph_clear, check_colors,
                 check_line_extents, check_point_background):
        test(probe)
    print("Routine | Cases | Observed register changes (case counts)")
    print("--- | ---: | ---")
    for name in sorted(probe.counts):
        changes = "; ".join(f"{regs} ({count})" for regs, count in sorted(probe.changed[name].items()))
        print(f"{name} | {probe.counts[name]} | {changes}")
    print(f"\nTotal: {sum(probe.counts.values())} calls")


if __name__ == "__main__":
    main()
