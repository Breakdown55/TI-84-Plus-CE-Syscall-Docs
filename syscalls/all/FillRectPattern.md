---
title: FillRectPattern
geekdocHidden: true
params:
    address: $02124C
    category: Graphics
    name: FillRectPattern
---

### Address: $02124C

Redraws a fixed region used by the TI-OS graph interface.

### Inputs:
* Uses the active graph interface and text-window state.

### Outputs:
* Begins by clearing the LCD rectangle from `(194, 0)` to `(319, 239)`, then runs the graph UI drawing path.

### Destroys:
* Save live registers and floating-point operands before calling. The routine changes drawing colors and OS display state.
* Writes `OP1`, `OP2`, `OP3`, `OP4`, `OP5`, `OP6` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* The ROM supplies its own rectangle coordinates. The full graph UI state contract is still unverified. Use [FillRect](FillRect.md) for caller-supplied rectangle bounds.
