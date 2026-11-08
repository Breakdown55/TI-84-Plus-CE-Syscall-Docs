---
title: DrawRectBorder
geekdocHidden: true
params:
    address: $02123C
    category: Graphics
    name: DrawRectBorder
---

### Address: $02123C

Draws a one-pixel rectangular border to the screen, using a specified color. See also [DrawThickRectBorder](DrawThickRectBorder.md). Note that calling this routine also disables interrupts.

> **Note.**
>
> The top-left LCD pixel is (0, 0). X increases to the right and Y increases downward. Pass ordered corners (hl, b) and (de, c) with hl ≤ de and b ≤ c. Reversed coordinates can cause drawing artifacts or screen corruption.

`_DrawRectBorder_` (`$0216DC`) and `_DrawRectBorder__` (`$021BE0`) jump to the same implementation as `_DrawRectBorder`.

### Inputs:
* `hl`: Top-left X coordinate of the rectangle.
* `de`: Bottom-right X coordinate of the rectangle.
* `b`: Top-left Y coordinate of the rectangle.
* `c`: Bottom-right Y coordinate of the rectangle.
* Value at [`drawFGColor`](../../memory/all/drawFGColor.md) contains the 16-bit color to draw with.

### Outputs:
* Draws to the screen.
* [`plotLoc`](../../memory/all/flags/plotFlags.md#bit-1---plotloc) flag set.
* [`g_style_active`](../../memory/all/flags/sGrFlags.md#bit-5---g_style_active) flag reset.

### Destroys:
* `af`

> **Note.**
>
> With `bufferOnly` set, no writes to the LCD framebuffer, `plotSScreen`, or `saveSScreen` were observed.
