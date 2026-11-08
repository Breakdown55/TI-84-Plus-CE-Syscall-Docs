---
title: DrawGraphBackground
geekdocHidden: true
params:
    address: $021A38
    category: Graphics
    name: DrawGraphBackground
---

### Address: $021A38

Draws the TI-OS background in the LCD region used for graphing.

### Inputs:
* Uses the current graph layout and background configuration. The solid fill color comes from `graphBGColor` at `$D02A98`.

### Outputs:
* Fills the graph display area and updates `fillRectColor`. The routine can also draw the configured background image.

### Destroys:
* `af`, `bc`, `de`, and `hl` on the tested solid-fill path.

### Additional Information:
* The image and split-layout branches have additional OS state requirements. Their full calling conditions are still unverified.
