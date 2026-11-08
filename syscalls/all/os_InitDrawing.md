---
title: os_InitDrawing
geekdocHidden: true
params:
    address: $021E1C
    category: Graphics
    name: os_InitDrawing
---

### Address: $021E1C

Initializes the TI-OS drawing context used by the stack-based display calls.

### Inputs:
* Uses the current app context.

### Outputs:
* Sets [`drawFGColor`](../../memory/all/drawFGColor.md) to black and initializes the drawing cursor and bounds.
* Initializes the drawing base to `$D40000`, the stride to 640 bytes, and the exclusive bottom row to `240`.

### Destroys:
* `af`, `bc`, `de`, and `hl`. `iy` is loaded with the OS flags base.

### Additional Information:
* The Y drawing cursor starts at `0` in the ordinary app context and `30` when the active context ID is `$58`.
