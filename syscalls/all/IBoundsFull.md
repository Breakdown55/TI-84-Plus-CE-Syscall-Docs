---
title: IBoundsFull
geekdocHidden: true
params:
    address: $02125C
    category: Graphics
    name: IBoundsFull
---

### Address: $02125C

Checks a pixel coordinate against the full 320 × 240 LCD.

### Inputs:
* `de` holds X and `c` holds Y.

### Outputs:
* Carry is clear for X in `0–319` and Y in `0–239`. Carry is set outside those bounds.

### Destroys:
* CPU flags in `f`.

### Additional Information:
* Uses full-LCD bounds regardless of `fullScrnDraw`. See [IBounds](IBounds.md) for graph-area bounds.
