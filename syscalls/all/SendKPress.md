---
title: SendKPress
geekdocHidden: true
params:
    address: $02015C
    category: System
    name: SendKPress
---

### Address: $02015C

This routine performs very similarly to [`Mon`](Mon.md), with the exception that it allows an initial key to be sent to [`cxMain`](../../memory/all/cxMain.md). Unlike [`MonForceKey`](MonForceKey.md), which handles special keys and runs through the raw key hook, `SendKPress` passes the keypress directly to `cxMain`.

> **Caution.**
>
> If this routine is called, it will not return.

### Inputs:
* `a`: [Keypress](../../other/keypad.md) to simulate.
* [`AppAllowContext`](../../memory/all/flags/APIFlg.md#bit-0---appallowcontext): Set to allow [`Mon`](Mon.md) to pass context keys, to the [`cxMain`](../../memory/all/cxMain.md) routine.
* [`curLock`](../../memory/all/flags/curFlags.md#bit-4---curlock): Set to lock the cursor off.

### Outputs:
* None.

### Destroys:
* This routine does not return.
