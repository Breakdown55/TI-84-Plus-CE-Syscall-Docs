---
title: GraphLine
geekdocHidden: true
params:
    address: $021730
    category: Graphics
    name: GraphLine
---

### Address: $021730

Draws a line as part of TI-OS graph processing.

### Inputs:
* Uses the current graph window and the OS graphing workspace. The routine reads `Xmin` and `Xmax` during setup.

### Outputs:
* Prepares graph coordinates and dispatches to [CLine](CLine.md). It can return early depending on the graphing state.

### Destroys:
* `af`, `bc`, `de`, `hl`, and `ix`.
* Writes `OP1`, `OP2`, `OP3`, `OP4`, `OP5`, `OP6` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* The graph workspace setup for a general standalone call is still unverified. Use [CLine](CLine.md) for explicitly supplied endpoints.
