---
title: ClrLCD
geekdocHidden: true
params:
    address: $02080C
    category: Graphics
    name: ClrLCD
---

### Address: $02080C

Clears the area below the status bar to white. In split mode it can clear just the graph pane or just the text pane.

### Inputs:
* None.

### Outputs:
* Normally fills LCD rows `30` through `239` with white, measured from the top of the LCD.
* Sets [`fillRectColor`](../../memory/all/fillRectColor.md) to `$FFFF`.

### Destroys:
* `af`, `bc`, `de`, and `hl`.

### Additional Information:
* If [`grfSplit`](../../memory/all/flags/sGrFlags.md#bit-0---grfsplit) is set and [`grfSplitOverride`](../../memory/all/flags/sGrFlags.md#bit-3---grfsplitoverride) is reset, [`plotDisp`](../../memory/all/flags/plotFlags.md#bit-2---plotdisp) selects the rows to clear. Set it for graph rows `30` through `154` or reset it for text rows `155` through `239`.
* In the 8-bit drawing path, writes `$FF` per pixel to the LCD's configured framebuffer.
