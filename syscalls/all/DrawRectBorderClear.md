---
title: DrawRectBorderClear
geekdocHidden: true
params:
    address: $021250
    category: Graphics
    name: DrawRectBorderClear
---

### Address: $021250

Draws a one-pixel border and fills its interior with white.

### Inputs:
* `hl` and `b` hold the top-left X and Y coordinates. `de` and `c` hold the bottom-right X and Y coordinates.
* Coordinates use the LCD’s top-left origin. Supply ordered corners within the LCD with at least one pixel of interior in each dimension.
* [`drawFGColor`](../../memory/all/drawFGColor.md) supplies the outline color.
* [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) suppresses the outline. The interior still clears.

### Outputs:
* Calls [DrawRectBorder](DrawRectBorder.md), then [ClearRect](ClearRect.md) with each edge moved inward by one pixel.
* Returns the interior corners in `hl`, `b`, `de`, and `c` and sets `fillRectColor` to `$FFFF`.

### Destroys:
* `af`

### Additional Information:
* Returns with interrupts disabled on the ordinary path.
