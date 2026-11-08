---
title: SetGraphicsHook
geekdocHidden: true
params:
    address: $0214AC
    category: Graphics
    name: SetGraphicsHook
---

### Address: $0214AC

Installs and enables a drawing hook.

### Inputs:
* `hl` points to a hook record beginning with the signature byte `$83`. The hook code follows that byte.

### Outputs:
* Stores the pointer in `graphicsHookPtr` (`$D025F3`) and sets [`drawingHookActive`](../../memory/all/flags/hookflags3.md#bit-7---drawinghookactive).

### Destroys:
* None.

### Additional Information:
* [IPoint](IPoint.md) and [ILine](ILine.md) allow normal drawing when the hook returns with the CPU zero flag set. Clearing that CPU flag on return cancels the draw.
