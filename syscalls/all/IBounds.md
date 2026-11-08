---
title: IBounds
geekdocHidden: true
params:
    address: $02110C
    category: Graphics
    name: IBounds
---

### Address: $02110C

Checks whether a pixel coordinate is within the selected drawing area.

### Inputs:
* `de` holds X and `c` holds Y.
* [`fullScrnDraw`](../../memory/all/flags/apiFlg4.md#bit-2---fullscrndraw) selects full-LCD bounds when set.

### Outputs:
* Carry is clear if the point is inside. Carry is set if it is outside.
* In graph mode, accepts X from `0` through `pixWide_m_2` and Y from `0` through `pixWideP - 1`. In full-LCD mode, accepts X from `0` through `319` and Y from `0` through `239`.

### Destroys:
* CPU flags in `f`.

### Additional Information:
* [IBoundsFull](IBoundsFull.md) always checks the full LCD.
