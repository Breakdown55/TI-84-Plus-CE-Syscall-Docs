---
title: DrawCirc
geekdocHidden: true
params:
    address: $021114
    category: Graphics
    name: DrawCirc
---

### Address: $021114

Draws a circle in the current graph window from a center and radius.

### Inputs:
* Push the center X, center Y, and radius in that order as TI-OS real numbers on the floating-point stack.
* The current graph window sets the scale. [`drawFGColor`](../../memory/all/drawFGColor.md) supplies the drawing color.
* [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) suppresses the ordinary LCD draw.

### Outputs:
* Draws the circle and consumes the three real numbers.

### Destroys:
* `af`, `bc`, `de`, `hl`, and `ix`.
* Writes `OP1`, `OP2`, `OP3`, `OP4`, `OP5`, `OP6` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* With the ordinary graph layout, updates `plotSScreen` if `plotLoc` is reset or `bufferOnly` is set.
* [GrphCirc](GrphCirc.md) accepts a center and circumference point in pixel coordinates.
