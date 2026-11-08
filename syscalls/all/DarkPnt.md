---
title: DarkPnt
geekdocHidden: true
params:
    address: $020B90
    category: Graphics
    name: DarkPnt
---

### Address: $020B90

Draws one point at a floating-point graph coordinate. This is the draw mode of [CPoint](CPoint.md).

### Inputs:
* `OP1` holds X and `OP2` holds Y as TI-OS real numbers.
* The current graph window determines how the coordinates map to pixels.
* [`drawFGColor`](../../memory/all/drawFGColor.md) supplies the LCD color. [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) suppresses ordinary VRAM writes.

### Outputs:
* Draws the point if it is within the graph window. The routine sets `a` to `1` before processing it.

### Destroys:
* `af`, `bc`, `de`, and `hl`.
* Writes `OP1`, `OP2`, `OP3` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* Uses the graph-buffer and hook settings described in [CPoint](CPoint.md).
