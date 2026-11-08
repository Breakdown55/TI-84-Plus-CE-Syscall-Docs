---
title: CoorMon
geekdocHidden: true
params:
    address: $020150
    category: System
    name: CoorMon
---

This routine performs very similarly to [`Mon`](Mon.md), with the exception that it does the following first:

```asm
res g_style_active, (iy + sGrFlags)
call CursorOff
call CoorDisp
```

Afterwards, [`Mon`](Mon.md) is run.

It appears that this routine is used in menu contexts, such as the programs, math, or catalog menus. It is triggered when the menu is entered or exited, along with when the cursor is moved.

> **Caution.**
>
> If this routine is called, it will not return.

### Address: $020150

### Inputs:
* [`AppAllowContext`](../../memory/all/flags/APIFlg.md#bit-0---appallowcontext): Set to allow [`Mon`](Mon.md) to pass context keys, to the [`cxMain`](../../memory/all/cxMain.md) routine.
* [`curLock`](../../memory/all/flags/curFlags.md#bit-4---curlock): Set to lock the cursor off.
* Possibly more?

### Outputs:
* System monitor takes over the system.

### Destroys:
* This routine does not return.
