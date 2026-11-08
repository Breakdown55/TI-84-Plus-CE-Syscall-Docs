---
title: os_GetYDrawLocation
geekdocHidden: true
params:
    address: $022090
    category: Graphics
    name: os_GetYDrawLocation
---

### Address: $022090

Reads the Y position of the TI-OS drawing cursor.

### Inputs:
* None.

### Outputs:
* `hl` holds the three-byte value at `gCurYLoc` (`$D02FD6`).

### Destroys:
* None besides the output in `hl`.
