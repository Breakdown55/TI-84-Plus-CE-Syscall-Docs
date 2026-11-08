---
title: os_SetYDrawLocation
geekdocHidden: true
params:
    address: $022094
    category: Graphics
    name: os_SetYDrawLocation
---

### Address: $022094

Sets the Y position of the TI-OS drawing cursor.

### Inputs:
* The first stack argument is the three-byte Y position, in LCD rows measured from the top.

### Outputs:
* Writes the argument to `gCurYLoc` (`$D02FD6`).

### Destroys:
* `hl` and CPU flags in `f`.

### Additional Information:
* The caller removes the argument after return. Supply a valid row for the drawing call that will use this position.
