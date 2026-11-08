---
title: VerticalLine
geekdocHidden: true
params:
    address: $021258
    category: Graphics
    name: VerticalLine
---

### Address: $021258

Draws a vertical line from Y coordinate zero to the current graph's top edge.

### Inputs:
* `de` holds the X coordinate.
* The byte at `pixWideP` (`$D014FE`) supplies the graph height. The default graph layout uses `165`.
* Value at [`drawFGColor`](../../memory/all/drawFGColor.md) contains the 16-bit color to write to VRAM.
* [`fullScrnDraw`](../../memory/all/flags/apiFlg4.md#bit-2---fullscrndraw) flag set to use full LCD coordinates or reset to use graph area coordinates. The routine takes the line height from `pixWideP` in both cases.
* [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) flag set to skip drawing to VRAM.

### Outputs:
* Draws from `(x, 0)` to `(x, pixWideP - 1)`, inclusive, using [ILine](ILine.md) in draw mode.
* `a` is set to `1`.

### Destroys:
* `af`, `bc`, `hl`, and `ix`.

### Additional Information:

* [`drawingHookActive`](../../memory/all/flags/hookflags3.md#bit-7---drawinghookactive) flag set to call the drawing hook before drawing the line. A hook that returns with the CPU zero flag clear cancels drawing.
* [`g_style_active`](../../memory/all/flags/sGrFlags.md#bit-5---g_style_active) flag set to use `currGrphStyle`. Style `1` makes the line thicker.
* With `fullScrnDraw` reset, writes the 4-bit `drawColorCode` to a graph buffer if [`plotLoc`](../../memory/all/flags/plotFlags.md#bit-1---plotloc) is reset or `bufferOnly` is set.
* Bit 3 of [`plotFlag3`](../../memory/all/flags/plotFlag3.md) selects [`plotSScreen`](../../memory/all/plotSScreen.md) when reset or `saveSScreen` when set.
* [`vertSplit`](../../memory/all/flags/sGrFlags.md#bit-1---vertsplit) flag set to use 93 bytes per row in `plotSScreen` or `saveSScreen`, instead of 133. VRAM coordinates are unchanged.
