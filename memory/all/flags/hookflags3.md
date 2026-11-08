---
title: hookflags3
geekdocHidden: true
params:
    address: $D000B5 (ti.flags + $35)
    name: hookflags3
---

### Address: $D000B5 (ti.flags + $35)

### Size: 1 byte

### Bit 0 - tokenHookActive:
Set if a token hook is active, reset otherwise.

### Bit 1 - localizeHookActive:
Set if a localize hook is active, reset otherwise.

### Bit 2 - windowHookActive:
Set if a window hook is active, reset otherwise.

### Bit 3 - graphHookActive:
Set if a graph hook is active, reset otherwise.

### Bit 4 - yEquHookActive:
Set if a Y= hook is active, reset otherwise.

### Bit 5 - fontHookActive:
Set if a font hook is active, reset otherwise.

### Bit 6 - regraphHookActive:
Set if a regraph hook is active, reset otherwise.

### Bit 7 - drawingHookActive:
Set if a drawing hook is active, reset otherwise.
