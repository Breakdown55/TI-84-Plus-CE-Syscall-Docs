---
title: hookflags2
geekdocHidden: true
params:
    address: $D000B4 (ti.flags + $34)
    name: hookflags2
---

### Address: $D000B4 (ti.flags + $34)

### Size: 1 byte

### Bit 0 - getCSCHookActive:
Set if a GetCSC hook is active, reset otherwise.

### Bit 1 - libraryHookActive:
Set if a library hook is active, reset otherwise.

### Bit 2 - noHookActive:
Appears to be unused.

### Bit 4 - homescreenHookActive:
Set if a homescreen hook is active, reset otherwise.

### Bit 5 - rawKeyHookActive:
Set if a raw key hook is active, reset otherwise.

### Bit 6 - catalog2HookActive:
Set if a catalog 2 hook is active, reset otherwise.

### Bit 7 - cursorHookActive:
Set if a cursor hook is active, reset otherwise.
