---
title: Rst28Handler
geekdocHidden: true
params:
    address: $02011C
    category: System
    name: Rst28Handler
---

### Address: $02011C

This routine is jumped to following `di \ rsmix` as a result of the [`rst 28`](../../instructions/processor-control.md#rst) instruction.

> **Warning.**
>
> Using this call will cause a crash.

### Inputs:
* None.

### Outputs:
* Causes the calculator to crash.

### Destroys:
* All RAM is reset.
