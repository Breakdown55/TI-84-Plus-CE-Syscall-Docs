---
title: GrBufCpy
geekdocHidden: true
params:
    address: $020C30
    category: Graphics
    name: GrBufCpy
---

### Address: $020C30

Renders [`plotSScreen`](../../memory/all/plotSScreen.md) into the LCD region used for graphing.

### Inputs:
* Uses the current graph layout, graph background, and `plotSScreen` color codes.

### Outputs:
* Expands the packed color codes into 16-bit LCD pixels. Sets `plotDisp`.

### Destroys:
* `af`, `bc`, `de`, and `hl` on the tested full-layout path.

### Additional Information:
* The routine can draw the split divider and composite a configured background. Use [BufCpy](BufCpy.md) for a different source buffer.
