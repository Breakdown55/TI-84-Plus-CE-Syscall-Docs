---
title: UnhighlightRect
geekdocHidden: true
params:
    address: $0219CC
    category: Graphics
    name: UnhighlightRect
---

### Address: $0219CC

Changes pixels that match `fillRectColor` to white (`$FFFF`). See also [HighlightRect](HighlightRect.md).

### Inputs:
* `hl`: Top-left X coordinate of the area to un-highlight.
* `de`: Bottom-right X coordinate of the area to un-highlight.
* `b`: Top-left Y coordinate of the area to un-highlight.
* `c`: Bottom-right Y coordinate of the area to un-highlight.
* Value at [`fillRectColor`](../../memory/all/fillRectColor.md) contains the 16-bit color to replace.

### Outputs:
* Draws to the screen.

### Destroys:
* `af`
