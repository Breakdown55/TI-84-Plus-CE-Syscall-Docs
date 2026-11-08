---
title: Rst10Handler
geekdocHidden: true
params:
    address: $020110
    category: System
    name: Rst10Handler
---

### Address: $020110

This routine is jumped to following `di \ rsmix` as a result of the [`rst 10`](../../instructions/processor-control.md#rst) instruction.

> **Warning.**
>
> Using this call will cause a crash.

### Inputs:
* None.

### Outputs:
* Causes the calculator to crash.

### Destroys:
* All RAM is reset.
