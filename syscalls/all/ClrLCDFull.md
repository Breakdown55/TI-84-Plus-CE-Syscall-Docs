---
title: ClrLCDFull
geekdocHidden: true
params:
    address: $020808
    category: Graphics
    name: ClrLCDFull
---

### Address: $020808

Clears the area below the status bar to white across the full width of the LCD.

### Inputs:
* None.

### Outputs:
* Fills LCD rows `30` through `239` in VRAM, measured from the top.
* Sets [`fillRectColor`](../../memory/all/fillRectColor.md) to `$FFFF`.

### Destroys:
* `bc`, `de`, and `hl`.

### Additional Information:
In the 8-bit drawing path, writes `$FF` per pixel to the LCD's configured framebuffer. [ClrLCD](ClrLCD.md) can limit the clear to one pane in split mode. [ClrLCDAll](ClrLCDAll.md) also clears the status bar.
