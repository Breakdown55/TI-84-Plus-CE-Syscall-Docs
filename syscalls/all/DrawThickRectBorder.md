---
title: DrawThickRectBorder
geekdocHidden: true
params:
    address: $021B04
    category: Graphics
    name: DrawThickRectBorder
---

### Address: $021B04

Draws a two-pixel rectangular border by drawing the specified outline and a second outline one pixel farther out on each side. See also [DrawRectBorder](DrawRectBorder.md). Note that calling this routine also disables interrupts.

> **Note.**
>
> The top-left LCD pixel is (0, 0). X increases to the right and Y increases downward. Pass ordered corners (hl, b) and (de, c) with hl ≤ de and b ≤ c. Reversed coordinates can cause drawing artifacts or screen corruption.

### Inputs:
* `hl`: Top-left X coordinate of the inner rectangle.
* `de`: Bottom-right X coordinate of the inner rectangle.
* `b`: Top-left Y coordinate of the inner rectangle.
* `c`: Bottom-right Y coordinate of the inner rectangle.
* Value at [`drawFGColor`](../../memory/all/drawFGColor.md) contains the 16-bit color to draw with.

### Outputs:
* Draws to the screen.
* `hl` and `b` are decremented by one.
* `de` and `c` are incremented by one.
* [`plotLoc`](../../memory/all/flags/plotFlags.md#bit-1---plotloc) flag set.
* [`g_style_active`](../../memory/all/flags/sGrFlags.md#bit-5---g_style_active) flag reset.

### Destroys:
* `af`

> **Note.**
>
> With `bufferOnly` set, no writes to the LCD framebuffer, `plotSScreen`, or `saveSScreen` were observed.
