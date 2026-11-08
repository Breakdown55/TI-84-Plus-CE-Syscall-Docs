---
title: DrawSPlot
geekdocHidden: true
params:
    address: $020B30
    category: Graphics
    name: DrawSPlot
---

### Address: $020B30

Processes the next stat plot in the OS graphing pass.

### Inputs:
* Uses the stat-plot definitions, lists, graph window, and `curPlotNumber` at `$D01D45`.

### Outputs:
* Advances the plot index and dispatches according to the enabled plot’s type. A disabled plot can return without drawing.

### Destroys:
* Save live registers and floating-point operands before calling.
* Writes `OP1` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* The active scatter, histogram, and box-plot setups are still unverified as standalone calls.
