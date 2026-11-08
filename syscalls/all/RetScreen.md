---
title: RetScreen
geekdocHidden: true
params:
    address: $020E20
    category: Graphics
    name: RetScreen
---

### Address: $020E20

Restores the TI-OS display after [SaveScreen](SaveScreen.md).

### Inputs:
* Uses the saved screen context and the current text or graph display state.

### Outputs:
* Restores saved cursor and app flags and runs the OS screen redraw path.

### Destroys:
* `de` and `hl` on the tested text path. Split and graph redraws can have additional clobbers.

### Additional Information:
* The routine clears `plotDisp` before restoring the text display. The split graph path can redraw from `plotSScreen`.
