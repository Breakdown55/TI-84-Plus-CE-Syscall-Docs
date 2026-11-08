---
title: PPutawayPrompt
geekdocHidden: true
params:
    address: $020174
    category: Context
    name: PPutawayPrompt
---

### Address: $020174

This routine calls the current context's [Partial PutAway](../../memory/all/cxPPutAway.md) vector, [PutAway](../../memory/all/cxPutAway.md) vector, and then resets the `promptEdit` flag. It is equivalent to this:

```asm
call PPutAway
call PutAway
res promptEdit, (iy + promptFlags)
```

### Inputs:
* [`cxPPutAway`](../../memory/all/cxPPutAway.md): Context's current Partial PutAway vector.
* [`cxPutAway`](../../memory/all/cxPutAway.md): Context's current PutAway vector.

### Outputs:
* Calls the listed vectors and resets `prompEdit`.

### Destroys:
* Depends on vectors.
