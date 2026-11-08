---
title: DrawSplitLine
geekdocHidden: true
params:
    address: $020C34
    category: Graphics
    name: DrawSplitLine
---

### Address: $020C34

Draws the horizontal divider for the split graph and text layout.

### Inputs:
* Set [`grfSplit`](../../memory/all/flags/sGrFlags.md#bit-0---grfsplit) and use a split layout that passes the OS split check.
* [`bufferOnly`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly) can suppress the LCD write.

### Outputs:
* Draws across LCD row `154` in the tested split layout. The routine restores the caller’s foreground color.

### Destroys:
* `af`, `bc`, and `hl` on the tested path.

### Additional Information:
* The routine temporarily sets `fullScrnDraw` and `plotLoc` for the divider and restores both on return.
