---
title: ClrLCDAll
geekdocHidden: true
params:
    address: $021A10
    category: Graphics
    name: ClrLCDAll
---

### Address: $021A10

Clears the entire LCD to white, including the status bar.

### Inputs:
* None.

### Outputs:
* Fills all 320 × 240 pixels in VRAM with white.
* Sets [`fillRectColor`](../../memory/all/fillRectColor.md) to `$FFFF`.

### Destroys:
* `bc`, `de`, and `hl`.

### Additional Information:
In the 8-bit drawing path, writes `$FF` per pixel to the LCD's configured framebuffer. For a clear that keeps the status bar, use [ClrLCDFull](ClrLCDFull.md).
