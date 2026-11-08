---
title: GetColorValue
geekdocHidden: true
params:
    address: $021BAC
    category: Graphics
    name: GetColorValue
---

### Address: $021BAC

Looks up a 16-bit drawing color by its internal palette index.

### Inputs:
* `a` holds the index. Use `0` through `15` for the palette documented under [SetDrawFGColorA](SetDrawFGColorA.md).

### Outputs:
* `de` holds the 16-bit color, with its upper byte cleared.

### Destroys:
* CPU flags in `f`.

### Additional Information:
* This entry reads the palette value without setting `drawFGColor` or `drawColorCode`.
