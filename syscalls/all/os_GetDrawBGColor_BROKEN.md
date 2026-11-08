---
title: os_GetDrawBGColor_BROKEN
geekdocHidden: true
params:
    address: $021EE4
    category: Graphics
    name: os_GetDrawBGColor_BROKEN
---

### Address: $021EE4

Returns the current drawing background color. The CE toolchain names this call `os_GetDrawBGColor`.

### Inputs:
* None.

### Outputs:
* `hl` holds the 16-bit `drawBGColor` from `$D026AA`, zero-extended on OS 5.8.2.

### Destroys:
* None besides the output in `hl`.

### Additional Information:
* The [CE toolchain screen API](https://ce-programming.github.io/toolchain/headers/ti/screen.html) documents availability from OS 5.2.
