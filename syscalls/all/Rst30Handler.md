---
title: Rst30Handler
geekdocHidden: true
params:
    address: $020120
    category: System
    name: Rst30Handler
---

### Address: $020120

This routine is jumped to following `di \ rsmix` as a result of the [`rst 30`](../../instructions/processor-control.md#rst) instruction.

> **Warning.**
>
> Using this call will cause a crash.

### Inputs:
* None.

### Outputs:
* Causes the calculator to crash.

### Destroys:
* All RAM is reset.
