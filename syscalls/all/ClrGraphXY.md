---
title: ClrGraphXY
geekdocHidden: true
params:
    address: $0210A8
    category: Graphics
    name: ClrGraphXY
---

### Address: $0210A8

Clears the graph’s coordinate readout using the current solid graph background color.

### Inputs:
* Uses the graph layout and coordinate-readout bounds kept by TI-OS.

### Outputs:
* Fills the readout rectangle and sets `fillRectColor` from `graphBGColor`.

### Destroys:
* `af`, `bc`, `de`, and `hl`.

### Additional Information:
* The ROM reads horizontal bounds from `$D02AB4` and `$D02ABA`. It computes the top row as the byte at `$D01505` plus `16`, and the bottom row as nine rows below that.
