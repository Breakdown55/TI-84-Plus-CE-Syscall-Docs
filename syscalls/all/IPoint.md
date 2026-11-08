---
title: IPoint
geekdocHidden: true
params:
    address: $020B7C
    category: Graphics
    name: IPoint
---

### Address: $020B7C

Draws, erases, or toggles a pixel. The drawing area's bottom-left pixel is (0, 0). X increases to the right and Y increases upward. The behavior below applies in 16-bit display mode with drawing hooks and graph styles disabled.

### Inputs:
* `de`: X coordinate of the pixel.
* `c`: Y coordinate of the pixel.
* `a`: Set to `0` to erase, `1` to draw, or `2` to toggle.
* [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) flag set to skip ordinary VRAM writes.
* `plotLoc` (bit 1 of `plotFlags`) flag set to skip writes to `plotSScreen` and `saveSScreen` when `bufferOnly` is reset.
* Bit 3 of [`plotFlag3`](../../memory/all/flags/plotFlag3.md) selects `plotSScreen` when reset or `saveSScreen` when set.
* Value at [`drawFGColor`](../../memory/all/drawFGColor.md) contains the 16-bit color to draw with. `drawColorCode` contains the color code to store in `plotSScreen` or `saveSScreen`.
* [`fullScrnDraw`](../../memory/all/flags/apiFlg4.md#bit-2---fullscrndraw) flag set to use the full LCD as the drawing area. When reset, the default graph area's (0, 0) is LCD pixel (27, 210), measured from the LCD's top-left corner.

### Outputs:
* Draws to the screen if [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) is reset. Erasing sets the pixel to white (`$FFFF`).
* If `fullScrnDraw` is reset and either `plotLoc` is reset or `bufferOnly` is set, drawing writes `drawColorCode` to `plotSScreen` or `saveSScreen`, according to bit 3 of `plotFlag3` and erasing writes zero.
* If `a` is `2` and the routine uses `plotSScreen` or `saveSScreen`, it reads the pixel’s color code from that buffer. It draws a pixel if the code is zero and erases it otherwise.
* If `a` is `2` and either `fullScrnDraw` is set or (`plotLoc` is set and `bufferOnly` is reset), the routine reads the pixel from the screen. It erases the pixel if it is black (`$0000`) and draws it otherwise.

### Destroys:
* None.

### Additional Information:

With `drawGrBackground` (bit 0 of `$D000CF`) set, the routine restores the configured background pixel on the screen even if `bufferOnly` is set. This applies to `a = 0` when `fullScrnDraw` and `plotLoc` are both reset, and to `a = 2` when it reads a nonzero color code from `plotSScreen` or `saveSScreen`.
* [`drawingHookActive`](../../memory/all/flags/hookflags3.md#bit-7---drawinghookactive) flag set to call the drawing hook before processing the pixel. A hook that returns with the CPU zero flag clear stops the draw.
* [`g_style_active`](../../memory/all/flags/sGrFlags.md#bit-5---g_style_active) flag set to use `currGrphStyle`. Style `1` can draw additional pixels.
* [`vertSplit`](../../memory/all/flags/sGrFlags.md#bit-1---vertsplit) flag set to use 93 bytes per row in `plotSScreen` or `saveSScreen`, instead of 133. In toggle mode, this can change which color code the routine reads and whether it draws or erases on the LCD.
