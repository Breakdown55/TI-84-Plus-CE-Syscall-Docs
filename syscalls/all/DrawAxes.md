---
title: DrawAxes
geekdocHidden: true
params:
    address: $0210B8
    category: Graphics
    name: DrawAxes
---

### Address: $0210B8

Draws axes and tick marks for the current graph window.

### Inputs:
* Uses the active graph window, scale values, and configured axes color.

### Outputs:
* Draws the axes that intersect the window. The tested graph setup updated both VRAM and `plotSScreen`.

### Destroys:
* `af`, `bc`, `de`, and `hl`.
* Writes `OP1`, `OP2`, `OP3`, `OP4`, `OP5` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* The routine loads the axes color into [`drawFGColor`](../../memory/all/drawFGColor.md). Save the current color if subsequent drawing needs it.
