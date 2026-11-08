---
title: ILine
geekdocHidden: true
params:
    address: $020B78
    category: Graphics
    name: ILine
---

### Address: $020B78

Draws, erases, or toggles a line between two pixel coordinates. Both endpoints are included. X increases to the right and Y increases upward.

### Inputs:
* `de` and `c` hold the starting X and Y coordinates.
* `hl` and `b` hold the ending X and Y coordinates.
* Set `a` to `0` to erase, `1` to draw, or `2` to toggle.
* Value at [`drawFGColor`](../../memory/all/drawFGColor.md) contains the 16-bit color to draw with. `drawColorCode` supplies the 4-bit color code for `plotSScreen` or `saveSScreen`.
* [`fullScrnDraw`](../../memory/all/flags/apiFlg4.md#bit-2---fullscrndraw) flag set to use the full LCD. The origin is LCD pixel `(0, 239)` when set or `(27, 210)` in the default graph layout when reset, measured from the LCD's top-left corner.
* [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) flag set to skip ordinary VRAM writes.
* `plotLoc` (bit 1 of `plotFlags`) flag set to skip writes to `plotSScreen` and `saveSScreen` when `bufferOnly` is reset.
* Bit 3 of [`plotFlag3`](../../memory/all/flags/plotFlag3.md) selects [`plotSScreen`](../../memory/all/plotSScreen.md) when reset or `saveSScreen` when set.

### Outputs:
* If `bufferOnly` is reset, draws to VRAM. With `fullScrnDraw` reset, this is the region of VRAM that corresponds to the graph area.
* If `fullScrnDraw` is reset and either `plotLoc` is reset or `bufferOnly` is set, updates `plotSScreen` or `saveSScreen` as selected by bit 3 of `plotFlag3`. These two buffers store color codes for points in the graph area. VRAM holds the pixels displayed on the LCD.
* If `a` is `1`, writes `drawFGColor` to VRAM and `drawColorCode` to `plotSScreen` or `saveSScreen`, according to the destination rules above.
* If `a` is `0`, writes white (`$FFFF`) to VRAM and zero to `plotSScreen` or `saveSScreen`, according to the same rules.
* If `a` is `2`, decides whether to draw or erase each pixel.
    * If the destination includes `plotSScreen` or `saveSScreen`, reads the pixel's color code from that buffer. Draws if the code is zero and erases otherwise.
    * Otherwise, reads the pixel from VRAM. Erases if the pixel is black (`$0000`) and draws otherwise.

### Destroys:

* `ix` receives the incoming value of `bc` when line processing proceeds.

The ordinary drawing behavior above was tested on TI-84 Plus CE OS 5.8.2 in 16-bit display mode, with graph styles and drawing hooks disabled.

### Additional Information:

* If `drawGrBackground` (bit 0 of `$D000CF`) is set, erasing writes the color or image pixel chosen under **2nd → FORMAT → Background** into VRAM. This applies to `a = 0` when `fullScrnDraw` and `plotLoc` are reset, or to `a = 2` when the routine reads a nonzero code from `plotSScreen` or `saveSScreen`. Both cases can write to VRAM even with `bufferOnly` set.
* [`drawingHookActive`](../../memory/all/flags/hookflags3.md#bit-7---drawinghookactive) flag set to call the drawing hook before processing the line. A hook that returns with the CPU zero flag clear stops the line.
* [`g_style_active`](../../memory/all/flags/sGrFlags.md#bit-5---g_style_active) flag set to use `currGrphStyle`. Style `1` makes the line thicker.
* [`vertSplit`](../../memory/all/flags/sGrFlags.md#bit-1---vertsplit) flag set to use 93 bytes per row in `plotSScreen` or `saveSScreen`, instead of 133. In toggle mode, this can change which color code the routine reads and whether it draws or erases on the LCD.
