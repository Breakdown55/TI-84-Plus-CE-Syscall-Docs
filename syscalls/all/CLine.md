---
title: CLine
geekdocHidden: true
params:
    address: $020B18
    category: Graphics
    name: CLine
---

### Address: $020B18

Draws a line between two floating-point graph coordinates.

### Inputs:
* `OP3` and `OP4` hold the starting X and Y coordinates.
* `OP1` and `OP2` hold the ending X and Y coordinates.
* Uses the current graph window and [`drawFGColor`](../../memory/all/drawFGColor.md).

### Outputs:
* Draws the portion of the line that falls within the graph window.

### Destroys:
* `af`, `bc`, `de`, `hl`, and `ix`.
* Writes `OP1`, `OP2`, `OP3`, `OP5`, `OP6` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* Shares the drawing path with [CLines](CLines.md). A drawing hook can intercept the line, and `bufferOnly` can suppress ordinary VRAM writes.
* The routine leaves the floating-point stack depth unchanged.
