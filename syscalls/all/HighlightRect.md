---
title: HighlightRect
geekdocHidden: true
params:
    address: $0219D0
    category: Graphics
    name: HighlightRect
---

### Address: $0219D0

Highlights a rectangular area of the screen by changing white pixels (`$FFFF`) to `fillRectColor`. The light cyan color used by TI-OS when highlighting memory entries is `$7FFE`. See also [UnhighlightRect](UnhighlightRect.md).

### Inputs:
* `hl`: Top-left X coordinate of the area to highlight.
* `de`: Bottom-right X coordinate of the area to highlight.
* `b`: Top-left Y coordinate of the area to highlight.
* `c`: Bottom-right Y coordinate of the area to highlight.
* Value at [`fillRectColor`](../../memory/all/fillRectColor.md) contains 16-bit color to highlight with.

### Outputs:
* Draws to the screen.

### Destroys:
* `af`
