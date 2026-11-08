---
title: BufIPoint
geekdocHidden: true
params:
    address: $021A14
    category: Graphics
    name: BufIPoint
---

### Address: $021A14

Resets `write_on_graph` and then draws, erases, or toggles a pixel through [IPoint](IPoint.md).

### Inputs:
* `de` holds the X coordinate.
* `c` holds the Y coordinate.
* Set `a` to `0` to erase, `1` to draw, or `2` to toggle.
* Uses the colors and drawing flags listed in [IPoint](IPoint.md). Set `bufferOnly` if you want to suppress ordinary VRAM writes.

### Outputs:
* Resets the [`write_on_graph`](../../memory/all/flags/sGrFlags.md#bit-4---write_on_graph) flag.
* Updates VRAM, `plotSScreen`, or `saveSScreen` under the same conditions as [IPoint](IPoint.md).

### Destroys:
* None on the ordinary drawing path.

### Additional Information:

* With `drawGrBackground` (bit 0 of `$D000CF`) set, erasing can restore the configured graph background pixel in VRAM even with `bufferOnly` set. The conditions are the same as for [IPoint](IPoint.md#additional-information).
* [`drawingHookActive`](../../memory/all/flags/hookflags3.md#bit-7---drawinghookactive) flag set to call the drawing hook before drawing the pixel. A hook that returns with the CPU zero flag clear cancels drawing.
* [`g_style_active`](../../memory/all/flags/sGrFlags.md#bit-5---g_style_active) flag set to use `currGrphStyle`. Style `1` can draw additional pixels.
* [`vertSplit`](../../memory/all/flags/sGrFlags.md#bit-1---vertsplit) flag set to use 93 bytes per row in `plotSScreen` or `saveSScreen`, instead of 133. In toggle mode, this can change which color code the routine reads and whether it draws or erases on the LCD.
