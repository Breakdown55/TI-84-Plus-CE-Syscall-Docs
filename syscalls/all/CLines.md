---
title: CLines
geekdocHidden: true
params:
    address: $020B1C
    category: Graphics
    name: CLines
---

### Address: $020B1C

Draws a line using two endpoints already on the TI-OS floating-point stack.

### Inputs:
* Push starting X, starting Y, ending X, and ending Y in that order as TI-OS real numbers.
* Uses the current graph window and [`drawFGColor`](../../memory/all/drawFGColor.md).

### Outputs:
* Draws the portion of the line that falls within the graph window and consumes all four real numbers.

### Destroys:
* `ix` on the ordinary drawing path.
* Writes `OP1`, `OP2`, `OP3`, `OP5`, `OP6` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* A drawing hook can intercept the call before the four numbers are consumed. `bufferOnly` can suppress ordinary VRAM writes.
