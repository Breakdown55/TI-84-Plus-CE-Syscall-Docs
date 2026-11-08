---
title: os_SetDrawBGColor
geekdocHidden: true
params:
    address: $021E20
    category: Graphics
    name: os_SetDrawBGColor
---

### Address: $021E20

Sets the 16-bit drawing background color.

### Inputs:
* The first stack argument is a three-byte slot containing the color in its low 16 bits.

### Outputs:
* Stores those 16 bits in `drawBGColor` at `$D026AA`.

### Destroys:
* `hl` and CPU flags in `f`.

### Additional Information:
* The caller removes the argument after return. See the [CE toolchain screen API](https://ce-programming.github.io/toolchain/headers/ti/screen.html).
