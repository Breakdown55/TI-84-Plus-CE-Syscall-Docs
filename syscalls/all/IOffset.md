---
title: IOffset
geekdocHidden: true
params:
    address: $021110
    category: Graphics
    name: IOffset
---

### Address: $021110

Computes a byte offset and nibble mask for packed point data.

### Inputs:
* `de` holds X and `c` holds Y. Y increases upward. Supply an in-bounds point.

### Outputs:
* `hl` holds the byte offset. In the ordinary graph layout it is `(pixWideP - 1 - y) * 133 + floor(x / 2)`.
* `a` is `$F0` for even X or `$0F` for odd X.

### Destroys:
* CPU flags in `f`.

### Additional Information:
* With [`fullScrnDraw`](../../memory/all/flags/apiFlg4.md#bit-2---fullscrndraw) set, uses row `239 - y` and a 160-byte stride.
* [`vertSplit`](../../memory/all/flags/sGrFlags.md#bit-1---vertsplit) selects a 93-byte stride when `fullScrnDraw` is reset.
