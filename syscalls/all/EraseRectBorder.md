---
title: EraseRectBorder
geekdocHidden: true
params:
    address: $021248
    category: Graphics
    name: EraseRectBorder
---

### Address: $021248

Draws a white one-pixel outline over the specified rectangle border.

### Inputs:
* `hl` and `b` hold the top-left X and Y coordinates. `de` and `c` hold the bottom-right X and Y coordinates.
* Coordinates use the LCD’s top-left origin. Supply ordered corners within the LCD.
* [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) suppresses the outline draw.

### Outputs:
* Sets [`drawFGColor`](../../memory/all/drawFGColor.md) to `$FFFF` and runs [DrawRectBorder](DrawRectBorder.md).
* Sets `plotLoc`, resets `g_style_active`, and returns with interrupts disabled on the ordinary path.

### Destroys:
* `af`
