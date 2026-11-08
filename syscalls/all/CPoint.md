---
title: CPoint
geekdocHidden: true
params:
    address: $021268
    category: Graphics
    name: CPoint
---

### Address: $021268

Draws, erases, or toggles a point at a floating-point coordinate in the current graph window.

### Inputs:
* `OP1` holds X and `OP2` holds Y as TI-OS real numbers.
* `a` selects `0` to erase, `1` to draw, or `2` to toggle.
* [`drawFGColor`](../../memory/all/drawFGColor.md) supplies the draw color. [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) suppresses ordinary VRAM writes.

### Outputs:
* Converts the graph coordinates and calls [IPoint](IPoint.md) if the point is in bounds.

### Destroys:
* `af`, `bc`, `de`, and `hl`.
* Writes `OP1`, `OP2`, `OP3` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* The [IPoint destination and toggle rules](IPoint.md#outputs) apply after coordinate conversion. A drawing hook can intercept the point.
* Use [CPointS](CPointS.md) when the coordinates are already on the floating-point stack. `CPoint` leaves the floating-point stack depth unchanged.
