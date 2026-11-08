---
title: SaveScreen
geekdocHidden: true
params:
    address: $020E1C
    category: Graphics
    name: SaveScreen
---

### Address: $020E1C

Saves TI-OS screen context for a later [RetScreen](RetScreen.md) or [RetScreenErr](RetScreenErr.md).

### Inputs:
* Uses the current text-window, app, cursor, and display state.

### Outputs:
* Saves window and cursor metadata and copies `appFlags` and `cursorFlags` into their backup bytes.
* Clears bits 1 and 5 of `appFlags`.

### Destroys:
* `af` and `hl`.

### Additional Information:
* This is a context save. The ROM stores metadata rather than a copy of LCD pixel data.
