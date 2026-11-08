---
title: DrawSprite16bpp
geekdocHidden: true
params:
    address: $021B64
    category: Graphics
    name: DrawSprite16bpp
---

### Address: $021B64

Draws a sprite into 16-bit VRAM using a TI-OS sprite data stream.

### Inputs:
* `hl` points to the sprite data. `de` holds the left X coordinate and `c` holds the top Y coordinate, measured from the LCD’s top-left.
* For a monochrome sprite, use format byte `0`, followed by the width and total pixel count as two little-endian 16-bit values. Then pack the pixels in row order, most significant bit first. Rows can share a byte.
* Keep the sprite within the LCD and supply a nonzero width and a total pixel count divisible by that width.

### Outputs:
* In format `0`, writes black for set bits and white for cleared bits.

### Destroys:
* `af`, `bc`, `de`, `hl`, and scratch RAM at `$D0059C`, `$D0063D`, and `$D0063F`.

### Additional Information:
* The ROM has other sprite formats. Their data layout is still unverified.
