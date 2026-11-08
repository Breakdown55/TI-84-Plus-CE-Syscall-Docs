---
title: GrBufCpyV
geekdocHidden: true
params:
    address: $0210A0
    category: Graphics
    name: GrBufCpyV
---

### Address: $0210A0

Refreshes the graph pane according to the active graph layout.

### Inputs:
* Uses the current split-screen mode and TI-OS graph display state.

### Outputs:
* In the full graph layout, renders [`plotSScreen`](../../memory/all/plotSScreen.md) as [GrBufCpy](GrBufCpy.md) does and sets `plotDisp`.

### Destroys:
* `af`, `bc`, `de`, and `hl` on the tested full-layout path.

### Additional Information:
* In vertical split mode, the routine can update the graph and adjacent pane separately. The complete split-state contract is unverified.
