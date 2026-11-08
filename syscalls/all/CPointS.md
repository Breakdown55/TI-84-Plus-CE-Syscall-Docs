---
title: CPointS
geekdocHidden: true
params:
    address: $020B94
    category: Graphics
    name: CPointS
---

### Address: $020B94

Draws, erases, or toggles a point whose coordinates are already on the TI-OS floating-point stack.

### Inputs:
* Push X and then Y as TI-OS real numbers. Y is at the top of the floating-point stack.
* `a` selects `0` to erase, `1` to draw, or `2` to toggle.
* Uses the current graph window and the drawing inputs of [CPoint](CPoint.md).

### Outputs:
* Consumes both real numbers and calls [IPoint](IPoint.md) if the converted point is in bounds.

### Destroys:
* `af`, `bc`, `de`, and `hl`.
* Writes `OP1`, `OP2`, `OP3` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* The [IPoint destination and toggle rules](IPoint.md#outputs) apply after coordinate conversion. A drawing hook can intercept the point.
