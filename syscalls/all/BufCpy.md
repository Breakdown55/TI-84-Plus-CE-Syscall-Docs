---
title: BufCpy
geekdocHidden: true
params:
    address: $021F50
    category: Graphics
    name: BufCpy
---

### Address: $021F50

Renders packed graph color codes from a caller-supplied buffer into the LCD graph region.

### Inputs:
* `hl` points to a buffer in the same format and size as [`plotSScreen`](../../memory/all/plotSScreen.md) for the current layout.
* Uses the current graph layout and background.

### Outputs:
* Renders the buffer into VRAM and sets `plotDisp`.

### Destroys:
* `af`, `bc`, `de`, and `hl` on the tested full-layout path.

### Additional Information:
* Each input byte holds two color codes. The routine shares the rendering body of [GrBufCpy](GrBufCpy.md).
