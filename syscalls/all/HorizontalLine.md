---
title: HorizontalLine
geekdocHidden: true
params:
    address: $02132C
    category: Graphics
    name: HorizontalLine
---

### Address: $02132C

Draws a horizontal line from `(0, y)` to `(x_end, y)`, including both endpoints.

### Inputs:
* The byte at `curGX2` (`$D01471`) supplies `y`, the Y coordinate of both endpoints.
* The 16-bit value at `pixWide_m_2` (`$D01501`) supplies `x_end`, the X coordinate of the right endpoint.
* Value at [`drawFGColor`](../../memory/all/drawFGColor.md) contains the 16-bit color to write to VRAM.
* [`fullScrnDraw`](../../memory/all/flags/apiFlg4.md#bit-2---fullscrndraw) flag set to use full LCD coordinates or reset to use graph area coordinates. X increases to the right and Y increases upward in both modes.
* [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) flag set to skip drawing to VRAM.

### Outputs:
* Draws the line using [ILine](ILine.md) in draw mode.
* `a` is set to `1`.

### Destroys:
* `bc`, `de`, `hl`, and `ix`.

### Additional Information:

* [`drawingHookActive`](../../memory/all/flags/hookflags3.md#bit-7---drawinghookactive) flag set to call the drawing hook before drawing. The hook can cancel drawing by returning with the CPU zero flag clear.
* [`g_style_active`](../../memory/all/flags/sGrFlags.md#bit-5---g_style_active) flag set to use `currGrphStyle`. Style `1` makes the line thicker.
* With `fullScrnDraw` reset, writes the 4-bit `drawColorCode` to a graph buffer if [`plotLoc`](../../memory/all/flags/plotFlags.md#bit-1---plotloc) is reset or `bufferOnly` is set.
* Bit 3 of [`plotFlag3`](../../memory/all/flags/plotFlag3.md) selects [`plotSScreen`](../../memory/all/plotSScreen.md) when reset or `saveSScreen` when set.
* [`vertSplit`](../../memory/all/flags/sGrFlags.md#bit-1---vertsplit) flag set to use 93 bytes per row in `plotSScreen` or `saveSScreen`, instead of 133. VRAM coordinates are unchanged.
* If `pixWide_m_2` contains `265`, the endpoints are `(0, y)` and `(265, y)`.
