---
title: ILineNoGraphicsHook
geekdocHidden: true
params:
    address: $0214B4
    category: Graphics
    name: ILineNoGraphicsHook
---

### Address: $0214B4

Enters the internal point drawing body after the graphics-hook check.

### Inputs:
* `de` and `c` hold the X and Y coordinates for the point path.
* For the ordinary point path, set `$D02AD4` to zero and store the mode at `$D02AC8`. Use `0` to erase, `1` to draw, or `2` to toggle.

### Outputs:
* Draws, erases, or toggles the point using the stored mode.

### Destroys:
* None on the tested ordinary point path. The register effects of other drawing contexts are unverified.

### Additional Information:
* The entry skips the initial hook check. A hook can still run later in the point path.
* This entry bypasses the setup at [IPoint](IPoint.md) and [ILine](ILine.md). Use those entry points when supplying the mode in `a`.
