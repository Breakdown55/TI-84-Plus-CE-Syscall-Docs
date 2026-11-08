---
title: RetScreenErr
geekdocHidden: true
params:
    address: $020E24
    category: Graphics
    name: RetScreenErr
---

### Address: $020E24

Restores saved display context for the TI-OS error path.

### Inputs:
* Uses the saved state established by [SaveScreen](SaveScreen.md).

### Outputs:
* Runs the error-display restoration path and restores saved app and cursor flags.

### Destroys:
* `hl` on the tested text path. Clobbers for all redraw paths are unverified.

### Additional Information:
* Use [RetScreen](RetScreen.md) for ordinary restoration.
