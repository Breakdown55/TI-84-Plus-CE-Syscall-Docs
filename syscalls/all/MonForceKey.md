---
title: MonForceKey
geekdocHidden: true
params:
    address: $020158
    category: System
    name: MonForceKey
---

### Address: $020158

This routine performs very similarly to [`Mon`](Mon.md), with the exception that it allows an initial key to be sent to [`cxMain`](../../memory/all/cxMain.md).

> **Caution.**
>
> If this routine is called, it will not return.

### Inputs:
* `a`: Initial [keypress](../../other/keypad.md) to send.
* [`AppAllowContext`](../../memory/all/flags/APIFlg.md#bit-0---appallowcontext): Set to allow `Mon` to pass context keys, to the [`cxMain`](../../memory/all/cxMain.md) routine.
* [`curLock`](../../memory/all/flags/curFlags.md#bit-4---curlock): Set to lock the cursor off.

### Outputs:
* None.

### Destroys:
* This routine does not return.
