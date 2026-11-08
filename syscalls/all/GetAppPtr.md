---
title: GetAppPtr
geekdocHidden: true
params:
    address: $022224
    category: Apps
    name: GetAppPtr
---

### Address: $022224

Gets the pointer of an app with the name specified in [`progCurrent + 1`](../../memory/all/progCurrent.md). It is likely that the first byte of [`progCurrent`](../../memory/all/progCurrent.md) will be `ti.AppObj`, though this call doesn't care about it.

> **Caution.**
>
> This call expects the name to be zero terminated, but the name in [`progCurrent`](../../memory/all/progCurrent.md) will not always be zero terminated if it is 8 bytes long. It is recommended to load [`progCurrent + 9`](../../memory/all/progCurrent.md) with 0 just to be safe.

### Inputs:
* [`progCurrent + 1`](../../memory/all/progCurrent.md): Name of app to find pointer for.

### Outputs:
* `hl`: Contains pointer to app if found, otherwise 0.
* [Carry Flag](../../instructions/flags.md#c-carry): Reset if app is found, set otherwise.

### Destroys:
* `af`, `bc`, `de`, `hl`.
