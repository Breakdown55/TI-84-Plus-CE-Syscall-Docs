# Graphics syscall tests

The suite ran **1,509 calls** on the TI-OS 5.8.2 ROM in the CEmu v2.0 core. That includes **1,019 calls** to the 12 new entries and 490 comparison calls to `ILine` and `IPoint`. The runner loads a copy of the workspace's saved emulator state and never uses a live CEmu window. It verifies that each routine returns in ADL mode with both stack pointers restored. It checks caller-visible register changes and varies the initial interrupt enable state with hardware interrupt sources masked.

| New routine | Calls | What the tests cover |
| --- | ---: | --- |
| [BufIPoint](../syscalls/all/BufIPoint.md) | 227 | All three modes, destination flags, point bounds, `write_on_graph`, hooks and styles, plus solid background restoration with either buffer. |
| [ClrLCD](../syscalls/all/ClrLCD.md) | 64 | Full-body and split-pane ranges, `plotDisp`, the split override, and the byte-per-pixel path. |
| [ClrLCDAll](../syscalls/all/ClrLCDAll.md) | 64 | Entire LCD with alternate split and drawing flags in both pixel paths. |
| [ClrLCDFull](../syscalls/all/ClrLCDFull.md) | 64 | Exact rows below the status bar with alternate split and drawing flags in both pixel paths. |
| [DarkLine](../syscalls/all/DarkLine.md) | 71 | Destination flags, reversed endpoints, coordinate boundaries, style, and hooks that allow or veto drawing. |
| [GrBufClr](../syscalls/all/GrBufClr.md) | 64 | Every combination of the three split flags, the two buffer flags, and two initial patterns. Checks the exact cleared range, adjacent bytes, and output pointers. |
| [GraphBGColorToDrawBGColor](../syscalls/all/GraphBGColorToDrawBGColor.md) | 64 | Sixteen source colors and four initial states. Checks the destination word, `hl`, and the drawing surfaces. |
| [HorizontalLine](../syscalls/all/HorizontalLine.md) | 101 | Destination flags, style, hooks, and five lengths with three Y coordinates in both coordinate systems. |
| [PointOn](../syscalls/all/PointOn.md) | 71 | Input `a` values, destination flags, coordinate boundaries, style, and hooks. |
| [SetDrawFGColorA](../syscalls/all/SetDrawFGColorA.md) | 64 | All 16 documented palette indices and four initial states. Checks RGB565, `drawColorCode`, and register results. |
| [SetWhiteDrawBGColor](../syscalls/all/SetWhiteDrawBGColor.md) | 64 | Sixteen initial background values and four initial states. Checks the output word, `hl`, and preserved drawing surfaces. |
| [VerticalLine](../syscalls/all/VerticalLine.md) | 101 | Destination flags, style, hooks, and five heights with three X coordinates in both coordinate systems. |

The wrapper tests compare full VRAM, `plotSScreen`, `saveSScreen`, relevant OS flags, and register results against calls to the underlying routine. Separate tests verify absolute pixel locations and output colors without calling a reference syscall. The 8-bit LCD cases exercise the ROM's byte-per-pixel path with a relocated framebuffer. Hook tests use short callbacks that preserve the coordinates. Results apply to the tested OS and configurations.

## Run again

From the workspace root in PowerShell, with MinGW GCC and 64-bit Python available:

```powershell
./manual/tests/build.ps1
python manual/tests/graphics.py
```

The build uses the CEmu v2.0 source at `iline-tests/cemu-source` (commit `a0a9d35a498b40ce0561ac51215b283d4059e816`). The tests use the local `ipoint-tests/before-tests.ce` snapshot by default. Pass `--state` to select a compatible 5.8.2 snapshot. The ROM and snapshot are not part of the manual.
