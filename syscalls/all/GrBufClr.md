---
title: GrBufClr
geekdocHidden: true
params:
    address: $02109C
    category: Graphics
    name: GrBufClr
---

### Address: $02109C

Zeros the portion of [`plotSScreen`](../../memory/all/plotSScreen.md) used by the current graph layout.

### Inputs:
* None.

### Outputs:
* Normally zeros all 21,945 bytes (`$55B9`) of `plotSScreen`, starting at `$D09466`. VRAM and `saveSScreen` retain their contents.
* `bc` is zero. `hl` points to the last byte cleared and `de` points to the next byte.

### Destroys:
* `af`.

### Additional Information:
* If [`grfSplit`](../../memory/all/flags/sGrFlags.md#bit-0---grfsplit) is set and [`grfSplitOverride`](../../memory/all/flags/sGrFlags.md#bit-3---grfsplitoverride) is reset, clears the first 10,773 bytes (`$2A15`).
* Otherwise, if [`vertSplit`](../../memory/all/flags/sGrFlags.md#bit-1---vertsplit) is set, clears the first 13,485 bytes (`$34AD`).
