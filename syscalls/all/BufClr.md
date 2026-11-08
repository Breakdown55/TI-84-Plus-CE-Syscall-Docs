---
title: BufClr
geekdocHidden: true
params:
    address: $021504
    category: Graphics
    name: BufClr
---

### Address: $021504

Clears LCD strips used for the table or graph-side display.

### Inputs:
* Uses the OS text and graph pane layout.

### Outputs:
* Clears the strips using the graph background color. In the tested layout it cleared ten strips, each 293 pixels wide and 14 rows apart.

### Destroys:
* `af`, `bc`, `de`, and `hl` on the tested path.

### Additional Information:
* The full split-layout inputs are unverified. [GrBufClr](GrBufClr.md) is the entry point for zeroing `plotSScreen`.
