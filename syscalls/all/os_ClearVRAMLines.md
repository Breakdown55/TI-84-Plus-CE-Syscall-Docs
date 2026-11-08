---
title: os_ClearVRAMLines
geekdocHidden: true
params:
    address: $021DE0
    category: Graphics
    name: os_ClearVRAMLines
---

### Address: $021DE0

Clears display rows from the OS drawing cursor to the configured lower drawing boundary.

### Inputs:
* Initialize the OS drawing context with [os_InitDrawing](os_InitDrawing.md). Set the first row through [os_SetYDrawLocation](os_SetYDrawLocation.md).
* The drawing context supplies the exclusive ending row, bytes per row, and framebuffer base.

### Outputs:
* Fills the selected rows with white in 16-bit mode, or `$FF` bytes in the OS’s 8-bit mode.

### Destroys:
* `af`, `bc`, `de`, and `hl`. `iy` is loaded with the OS flags base.

### Additional Information:
* The context fields are three bytes each. The first row is at `$D02FD6`, the ending row at `$D02FDC`, the row stride at `$D02FE0`, and the base at `$D02FE3`. Use a first row number smaller than the ending row number.
