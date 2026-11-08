---
title: os_GetDrawFGColor
geekdocHidden: true
params:
    address: $021EE8
    category: Graphics
    name: os_GetDrawFGColor
---

### Address: $021EE8

Returns the current drawing foreground color.

### Inputs:
* None.

### Outputs:
* `hl` holds the 16-bit [`drawFGColor`](../../memory/all/drawFGColor.md) with its upper byte cleared.

### Destroys:
* CPU flags in `f`.

### Additional Information:
* See the [CE toolchain screen API](https://ce-programming.github.io/toolchain/headers/ti/screen.html).
