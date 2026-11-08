---
title: GetCSC
geekdocHidden: true
params:
    address: $02014C
    category: Keyboard
    name: GetCSC
---

### Address: $02014C

This routine loads the current keyboard scancode from [`kbdScanCode`](../../memory/all/kbdScanCode.md) into `a`, then clears [`kbdScanCode`](../../memory/all/kbdScanCode.md). If no key is pressed, `a` is loaded with $00. Note that calling this routine will also enable interrupts. An interactive keypad with all key values (including scan codes) can be found [here](../../other/keypad.md).

### Inputs:
* None.

### Outputs:
* `a`: Current scancode.
* `hl`: [`kbdScanCode`](../../memory/all/kbdScanCode.md) address.
* [`kbdScanCode`](../../memory/all/kbdScanCode.md): Loaded with $00.
* [`kbdSCR`](../../memory/all/flags/kbdFlags.md#bit-3---kbdscr) flag reset.

### Destroys:
* `a`, `hl`
