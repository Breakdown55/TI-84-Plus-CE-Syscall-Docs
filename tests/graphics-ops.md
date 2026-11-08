# Graphics operand audit

Headless CEmu ran the TI-OS 5.8.2 entries listed below. The runner watched each byte from `$D005F8` through `$D00639`, covering all 11 bytes of each of `OP1` through `OP6`, including extension bytes. It also compared those bytes before the call and after return.

Reads and writes are the union of the tested paths. A write can occur even if the bytes at return match the input. `None` means the tested calls did not show that access or change. Graph hooks, split layouts, sprite formats, and other OS-dependent paths can have different effects.

Run the audit after building the headless runner as described in [Graphics syscall tests](README.md).

```powershell
python manual/tests/graphics_op_audit.py
```

| Routine | Calls | OP reads | OP writes | OP contents changed at return |
| --- | ---: | --- | --- | --- |
| BufClr | 1 | None | None | None |
| BufCpy | 1 | None | None | None |
| BufIPoint | 1 | None | None | None |
| ClearRect | 1 | None | None | None |
| CLine | 1 | OP1, OP2, OP3, OP4, OP5, OP6 | OP1, OP2, OP3, OP5, OP6 | OP1, OP2, OP3, OP6 |
| CLines | 1 | OP1, OP2, OP3, OP5, OP6 | OP1, OP2, OP3, OP5, OP6 | OP1, OP2, OP3, OP6 |
| ClrGraphicsHook | 1 | None | None | None |
| ClrGraphXY | 1 | None | None | None |
| ClrLCD | 1 | None | None | None |
| ClrLCDAll | 1 | None | None | None |
| ClrLCDFull | 1 | None | None | None |
| CPoint | 3 | OP1, OP2, OP3 | OP1, OP2, OP3 | OP1, OP2, OP3 |
| CPointS | 3 | OP1, OP2, OP3 | OP1, OP2, OP3 | OP1, OP2, OP3 |
| DarkLine | 1 | None | None | None |
| DarkPnt | 3 | OP1, OP2, OP3 | OP1, OP2, OP3 | OP1, OP2, OP3 |
| DrawAxes | 1 | OP1, OP2, OP3, OP4, OP5 | OP1, OP2, OP3, OP4, OP5 | OP1, OP2, OP3, OP4, OP5 |
| DrawCirc | 8 | OP1, OP2, OP3, OP4, OP5, OP6 | OP1, OP2, OP3, OP4, OP5, OP6 | OP1, OP2, OP3, OP4, OP5, OP6 |
| DrawGraphBackground | 1 | None | None | None |
| DrawRectBorder | 1 | None | None | None |
| DrawRectBorderClear | 2 | None | None | None |
| DrawSplitLine | 1 | None | None | None |
| DrawSPlot | 1 | OP1 | OP1 | OP1 |
| DrawSprite16bpp | 3 | None | None | None |
| DrawThickRectBorder | 1 | None | None | None |
| DrawTILogo | 1 | OP1, OP2 | OP1 | OP1 |
| EraseRectBorder | 2 | None | None | None |
| FillRect | 1 | None | None | None |
| FillRectPattern | 1 | OP1, OP2, OP3, OP4, OP5, OP6 | OP1, OP2, OP3, OP4, OP5, OP6 | OP1, OP2, OP3, OP4, OP5 |
| GetColorValue | 16 | None | None | None |
| GraphBGColorToDrawBGColor | 1 | None | None | None |
| GraphLine | 1 | OP1, OP2, OP3, OP4, OP5, OP6 | OP1, OP2, OP3, OP4, OP5, OP6 | OP1, OP2, OP3, OP4, OP5, OP6 |
| GrBufClr | 1 | None | None | None |
| GrBufCpy | 1 | None | None | None |
| GrBufCpyV | 1 | None | None | None |
| GrphCirc | 8 | OP1, OP2, OP3, OP4, OP5, OP6 | OP1, OP2, OP3, OP4, OP5, OP6 | OP1, OP2, OP3, OP4, OP5, OP6 |
| HighlightRect | 1 | None | None | None |
| HorizontalLine | 1 | None | None | None |
| IBounds | 60 | None | None | None |
| IBoundsFull | 60 | None | None | None |
| ILine | 1 | None | None | None |
| ILineNoGraphicsHook | 6 | None | None | None |
| ILineNoHook | 6 | None | None | None |
| InvertRect | 1 | None | None | None |
| IOffset | 48 | None | None | None |
| IPoint | 2 | None | None | None |
| os_ClearVRAMLines | 4 | None | None | None |
| os_GetDrawBGColor_BROKEN | 4 | None | None | None |
| os_GetDrawFGColor | 4 | None | None | None |
| os_GetYDrawLocation | 4 | None | None | None |
| os_InitDrawing | 2 | None | None | None |
| os_SetDrawBGColor | 4 | None | None | None |
| os_SetDrawFGColor | 4 | None | None | None |
| os_SetYDrawLocation | 4 | None | None | None |
| PlotPt | 1 | OP1, OP2, OP3, OP4, OP5, OP6 | OP1, OP2, OP3, OP5, OP6 | OP1, OP2, OP3, OP6 |
| PointOn | 1 | None | None | None |
| RetScreen | 1 | None | None | None |
| RetScreenErr | 1 | None | None | None |
| SaveScreen | 1 | None | None | None |
| ScreenScrollPixelsUp | 1 | None | None | None |
| SetDrawFGColorA | 1 | None | None | None |
| SetGraphicsHook | 7 | None | None | None |
| SetWhiteDrawBGColor | 1 | None | None | None |
| UCLines | 1 | OP1, OP2, OP3, OP5, OP6 | OP1, OP2, OP3, OP5, OP6 | OP1, OP2, OP3, OP6 |
| UnhighlightRect | 1 | None | None | None |
| VerticalLine | 1 | None | None | None |

Total: 308 calls across 65 entries.
