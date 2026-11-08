---
title: ILineNoHook
geekdocHidden: true
params:
    address: $0214B8
    category: Graphics
    name: ILineNoHook
---

### Address: $0214B8

Draws, erases, or toggles a pixel-coordinate line without the initial graphics-hook dispatch.

### Inputs:
* `de` and `c` hold the starting X and Y coordinates.
* `hl` and `b` hold the ending X and Y coordinates.
* `a` selects `0` to erase, `1` to draw, or `2` to toggle.
* Uses the coordinate, color, and destination inputs of [ILine](ILine.md).

### Outputs:
* Processes the line using the supplied mode.

### Destroys:
* `ix` receives the incoming `bc` on the ordinary line path.

### Additional Information:
* Later drawing hooks can still run and suppress drawing. This entry only bypasses the initial hook check in [ILine](ILine.md).
