---
title: Rst20Handler
geekdocHidden: true
params:
    address: $020118
    category: System
    name: Rst20Handler
---

### Address: $020118

This routine is jumped to following `di \ rsmix` as a result of the [`rst 20`](../../instructions/processor-control.md#rst) instruction.

> **Warning.**
>
> Using this call will cause a crash.

### Inputs:
* None.

### Outputs:
* Causes the calculator to crash.

### Destroys:
* All RAM is reset.
