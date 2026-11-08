---
title: ScreenScrollPixelsUp
geekdocHidden: true
params:
    address: $020EB0
    category: Graphics
    name: ScreenScrollPixelsUp
---

### Address: $020EB0

Scrolls a region of the TI-OS text display upward by 20 LCD rows.

### Inputs:
* `ix` points to a two-byte descriptor for the current text window. The routine reads bytes at offsets `0` and `1` as line indices.

### Outputs:
* Copies pixel rows upward and updates the text shadow for that region.

### Destroys:
* `af`, `bc`, `de`, and `hl` on the tested text-scroll path.

### Additional Information:
* A descriptor containing `1, 4` copied LCD rows `77–116` to rows `57–96`. The full valid descriptor range and context requirements are still unverified.
