---
title: GraphBGColorToDrawBGColor
geekdocHidden: true
params:
    address: $021BC4
    category: Graphics
    name: GraphBGColorToDrawBGColor
---

### Address: $021BC4

Copies the current solid graph background color into the drawing background color.

### Inputs:
* `graphBGColor` (`$D02A98`) contains the 16-bit source color.

### Outputs:
* Copies the color to `drawBGColor` (`$D026AA`) and returns it in `hl`.

### Destroys:
* None besides the output in `hl`.
