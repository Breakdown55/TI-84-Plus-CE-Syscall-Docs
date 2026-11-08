---
title: PointOn
geekdocHidden: true
params:
    address: $0210E4
    category: Graphics
    name: PointOn
---

### Address: $0210E4

Draws one pixel using the current drawing color. This is the draw mode of [IPoint](IPoint.md), with `a` set to `1` by the routine.

### Inputs:
* `de` holds the X coordinate.
* `c` holds the Y coordinate.
* Value at [`drawFGColor`](../../memory/all/drawFGColor.md) contains the 16-bit color to write to VRAM.
* [`fullScrnDraw`](../../memory/all/flags/apiFlg4.md#bit-2---fullscrndraw) flag set to use full LCD coordinates or reset to use graph area coordinates.
* [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) flag set to skip drawing to VRAM.

### Outputs:
* Draws the pixel to the destination chosen by the [IPoint flags](IPoint.md#outputs).
* `a` is set to `1`.

### Destroys:
* None on the ordinary drawing path.

### Additional Information:

* [`drawingHookActive`](../../memory/all/flags/hookflags3.md#bit-7---drawinghookactive) flag set to call the drawing hook before drawing the pixel. A hook that returns with the CPU zero flag clear cancels drawing.
* [`g_style_active`](../../memory/all/flags/sGrFlags.md#bit-5---g_style_active) flag set to use `currGrphStyle`. Style `1` can draw additional pixels.
* With `fullScrnDraw` reset, writes the 4-bit `drawColorCode` to a graph buffer if [`plotLoc`](../../memory/all/flags/plotFlags.md#bit-1---plotloc) is reset or `bufferOnly` is set.
* Bit 3 of [`plotFlag3`](../../memory/all/flags/plotFlag3.md) selects [`plotSScreen`](../../memory/all/plotSScreen.md) when reset or `saveSScreen` when set.
* [`vertSplit`](../../memory/all/flags/sGrFlags.md#bit-1---vertsplit) flag set to use 93 bytes per row in `plotSScreen` or `saveSScreen`, instead of 133. VRAM coordinates are unchanged.
