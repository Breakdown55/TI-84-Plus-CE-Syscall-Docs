---
title: ClrGraphicsHook
geekdocHidden: true
params:
    address: $0214B0
    category: Graphics
    name: ClrGraphicsHook
---

### Address: $0214B0

Disables the current drawing hook.

### Inputs:
* None.

### Outputs:
* Resets [`drawingHookActive`](../../memory/all/flags/hookflags3.md#bit-7---drawinghookactive).

### Destroys:
* None.

### Additional Information:
* Use [SetGraphicsHook](SetGraphicsHook.md) to install or re-enable a hook.
