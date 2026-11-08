---
title: os_SetDrawFGColor
geekdocHidden: true
params:
    address: $021E24
    category: Graphics
    name: os_SetDrawFGColor
---

### Address: $021E24

Sets the 16-bit drawing foreground color.

### Inputs:
* The first stack argument is a three-byte slot containing the color in its low 16 bits.

### Outputs:
* Stores those 16 bits in [`drawFGColor`](../../memory/all/drawFGColor.md).

### Destroys:
* `hl` and CPU flags in `f`.

### Additional Information:
* The caller removes the argument after return. [SetDrawFGColorA](SetDrawFGColorA.md) also sets the corresponding graph color code when using a palette index. See the [CE toolchain screen API](https://ce-programming.github.io/toolchain/headers/ti/screen.html).
