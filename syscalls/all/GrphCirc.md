---
title: GrphCirc
geekdocHidden: true
params:
    address: $020B6C
    category: Graphics
    name: GrphCirc
---

### Address: $020B6C

Draws a circle from its center and a point on its circumference, both in graph-area pixel coordinates.

### Inputs:
* The center X is a 16-bit value at `$D01472`. Center Y is a byte at `$D01471`.
* The circumference point’s X is a 16-bit value at `$D0146F`. Its Y is a byte at `$D0146E`.
* Coordinates start at the bottom left of the graph area and increase to the right and upward.
* [`drawFGColor`](../../memory/all/drawFGColor.md) supplies the drawing color. [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) suppresses the ordinary LCD draw.

### Outputs:
* Draws the circle and restores the floating-point stack depth.

### Destroys:
* `af`, `bc`, `de`, `hl`, and `ix`.
* Writes `OP1`, `OP2`, `OP3`, `OP4`, `OP5`, `OP6` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* With the ordinary graph layout, updates `plotSScreen` if `plotLoc` is reset or `bufferOnly` is set.
* [DrawCirc](DrawCirc.md) accepts a center and radius in floating-point graph coordinates.
