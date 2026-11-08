---
title: SetDrawFGColorA
geekdocHidden: true
params:
    address: $021A28
    category: Graphics
    name: SetDrawFGColorA
---

### Address: $021A28

Sets the drawing foreground color and its graph color code from a palette index.

### Inputs:
* `a` holds the palette index. Use `1` through `15` for the named colors below.

### Outputs:
* Sets [`drawFGColor`](../../memory/all/drawFGColor.md) to the palette color and returns the same RGB565 value in `de`.
* Sets `drawColorCode` (`$D026AE`) to the input index.

### Destroys:
* CPU flags in `f`.

### Additional Information:
These are the assembly indices. TI-BASIC uses color numbers `10` through `24` in the same order. [TI color reference](https://education.ti.com/html/eguides/graphing/84plusce/en/content/eg_84prgm/m_prgm_ctl/m_prgmcontrol.HTML)

| `a` | Color | RGB565 |
| ---: | --- | --- |
| 1 | Blue | `$001F` |
| 2 | Red | `$F800` |
| 3 | Black | `$0000` |
| 4 | Magenta | `$F81F` |
| 5 | Green | `$04E0` |
| 6 | Orange | `$FC64` |
| 7 | Brown | `$B100` |
| 8 | Navy | `$0010` |
| 9 | Light blue | `$049F` |
| 10 | Yellow | `$FFE0` |
| 11 | White | `$FFFF` |
| 12 | Light gray | `$E71C` |
| 13 | Medium gray | `$C618` |
| 14 | Gray | `$8C51` |
| 15 | Dark gray | `$52AA` |

Index `0` also sets the foreground RGB565 value to white, but stores code zero. Use index `11` when a graph point needs a nonzero white color code.
