---
title: plotSScreen
geekdocHidden: true
params:
    address: $D09466
    name: plotSScreen
---

### Address: $D09466

### Size: 21,945 bytes in the full graph layout

Stores 4-bit color codes for points in the graph area. A code of zero represents an erased point. The visible pixels live separately in VRAM.

[IPoint](../../syscalls/all/IPoint.md) and [ILine](../../syscalls/all/ILine.md) use this area when their drawing flags allow a graph buffer write and bit 3 of `plotFlag3` is reset. With bit 3 set, those routines normally use `saveSScreen` at `$D0EA1F`. [GrBufClr](../../syscalls/all/GrBufClr.md) always clears starting at `plotSScreen`.
