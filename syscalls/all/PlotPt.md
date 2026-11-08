---
title: PlotPt
geekdocHidden: true
params:
    address: $0210B0
    category: Graphics
    name: PlotPt
---

### Address: $0210B0

Processes a point for the OS grapher. The active graph style can make it draw a line from the preceding point.

### Inputs:
* Uses the grapher’s current and previous coordinates and its active graphing state.

### Outputs:
* May draw a point, marker, or connecting line and update the grapher’s state.

### Destroys:
* Save any live registers and floating-point operands before calling.
* Writes `OP1`, `OP2`, `OP3`, `OP5`, `OP6` on the [tested path](../../tests/graphics-ops.md).

### Additional Information:
* The routine can return without drawing when graph processing is inactive. The input layout for every graph style is still unverified.
* For a standalone point, use [CPoint](CPoint.md) with graph coordinates or [IPoint](IPoint.md) with pixel coordinates.
