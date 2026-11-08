---
title: UCLines
geekdocHidden: true
params:
    address: $020B14
    category: Graphics
    name: UCLines
---

### Address: $020B14

Erases a line using two endpoints already on the TI-OS floating-point stack.

### Inputs:
* Push starting X, starting Y, ending X, and ending Y in that order as TI-OS real numbers.
* Uses the current graph window.

### Outputs:
* Erases the visible portion of the line and consumes all four real numbers. In the ordinary draw setup, erased LCD pixels become white.

### Destroys:
* `ix` on the ordinary drawing path.
* Writes `OP1`, `OP2`, `OP3`, `OP5`, `OP6` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* A drawing hook can intercept the call before the four numbers are consumed. See [CLines](CLines.md) for the draw entry point.
