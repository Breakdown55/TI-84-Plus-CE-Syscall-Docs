# Syscall index

Each link opens the register and flag reference for that call.

## Apps

| Call | Address |
| --- | --- |
| [AppSetup](all/AppSetup.md) | `$021148` |
| [GetAppPtr](all/GetAppPtr.md) | `$022224` |

## Arithmetic

| Call | Address |
| --- | --- |
| [AbsO1PAbsO2](all/AbsO1PAbsO2.md) | `$0201A0` |
| [CpHLDE](all/CpHLDE.md) | `$02013C` |
| [DivHLBy10_s](all/DivHLBy10_s.md) | `$020140` |
| [DivHLByA_s](all/DivHLByA_s.md) | `$020144` |

## Context

| Call | Address |
| --- | --- |
| [AppInit](all/AppInit.md) | `$020190` |
| [CallMain](all/CallMain.md) | `$020188` |
| [ErrorEP](all/ErrorEP.md) | `$020184` |
| [PPutAway](all/PPutAway.md) | `$020178` |
| [PPutawayPrompt](all/PPutawayPrompt.md) | `$020174` |
| [PutAway](all/PutAway.md) | `$02017C` |
| [SizeWind](all/SizeWind.md) | `$020180` |

## Graphics

[OP1–OP6 access audit](../tests/graphics-ops.md) for the graphics calls listed here.

| Call | Address |
| --- | --- |
| [BufClr](all/BufClr.md) | `$021504` |
| [BufCpy](all/BufCpy.md) | `$021F50` |
| [BufIPoint](all/BufIPoint.md) | `$021A14` |
| [ClearRect](all/ClearRect.md) | `$021218` |
| [CLine](all/CLine.md) | `$020B18` |
| [CLines](all/CLines.md) | `$020B1C` |
| [ClrGraphicsHook](all/ClrGraphicsHook.md) | `$0214B0` |
| [ClrGraphXY](all/ClrGraphXY.md) | `$0210A8` |
| [ClrLCD](all/ClrLCD.md) | `$02080C` |
| [ClrLCDAll](all/ClrLCDAll.md) | `$021A10` |
| [ClrLCDFull](all/ClrLCDFull.md) | `$020808` |
| [CPoint](all/CPoint.md) | `$021268` |
| [CPointS](all/CPointS.md) | `$020B94` |
| [DarkLine](all/DarkLine.md) | `$020B74` |
| [DarkPnt](all/DarkPnt.md) | `$020B90` |
| [DrawAxes](all/DrawAxes.md) | `$0210B8` |
| [DrawCirc](all/DrawCirc.md) | `$021114` |
| [DrawGraphBackground](all/DrawGraphBackground.md) | `$021A38` |
| [DrawRectBorder](all/DrawRectBorder.md) | `$02123C` |
| [DrawRectBorderClear](all/DrawRectBorderClear.md) | `$021250` |
| [DrawSplitLine](all/DrawSplitLine.md) | `$020C34` |
| [DrawSPlot](all/DrawSPlot.md) | `$020B30` |
| [DrawSprite16bpp](all/DrawSprite16bpp.md) | `$021B64` |
| [DrawThickRectBorder](all/DrawThickRectBorder.md) | `$021B04` |
| [DrawTILogo](all/DrawTILogo.md) | `$021B00` |
| [EraseRectBorder](all/EraseRectBorder.md) | `$021248` |
| [FillRect](all/FillRect.md) | `$021220` |
| [FillRectPattern](all/FillRectPattern.md) | `$02124C` |
| [GetColorValue](all/GetColorValue.md) | `$021BAC` |
| [GraphBGColorToDrawBGColor](all/GraphBGColorToDrawBGColor.md) | `$021BC4` |
| [GraphLine](all/GraphLine.md) | `$021730` |
| [GrBufClr](all/GrBufClr.md) | `$02109C` |
| [GrBufCpy](all/GrBufCpy.md) | `$020C30` |
| [GrBufCpyV](all/GrBufCpyV.md) | `$0210A0` |
| [GrphCirc](all/GrphCirc.md) | `$020B6C` |
| [HighlightRect](all/HighlightRect.md) | `$0219D0` |
| [HorizontalLine](all/HorizontalLine.md) | `$02132C` |
| [IBounds](all/IBounds.md) | `$02110C` |
| [IBoundsFull](all/IBoundsFull.md) | `$02125C` |
| [ILine](all/ILine.md) | `$020B78` |
| [ILineNoGraphicsHook](all/ILineNoGraphicsHook.md) | `$0214B4` |
| [ILineNoHook](all/ILineNoHook.md) | `$0214B8` |
| [InvertRect](all/InvertRect.md) | `$02121C` |
| [IOffset](all/IOffset.md) | `$021110` |
| [IPoint](all/IPoint.md) | `$020B7C` |
| [os_ClearVRAMLines](all/os_ClearVRAMLines.md) | `$021DE0` |
| [os_GetDrawBGColor_BROKEN](all/os_GetDrawBGColor_BROKEN.md) | `$021EE4` |
| [os_GetDrawFGColor](all/os_GetDrawFGColor.md) | `$021EE8` |
| [os_GetYDrawLocation](all/os_GetYDrawLocation.md) | `$022090` |
| [os_InitDrawing](all/os_InitDrawing.md) | `$021E1C` |
| [os_SetDrawBGColor](all/os_SetDrawBGColor.md) | `$021E20` |
| [os_SetDrawFGColor](all/os_SetDrawFGColor.md) | `$021E24` |
| [os_SetYDrawLocation](all/os_SetYDrawLocation.md) | `$022094` |
| [PlotPt](all/PlotPt.md) | `$0210B0` |
| [PointOn](all/PointOn.md) | `$0210E4` |
| [RetScreen](all/RetScreen.md) | `$020E20` |
| [RetScreenErr](all/RetScreenErr.md) | `$020E24` |
| [SaveScreen](all/SaveScreen.md) | `$020E1C` |
| [ScreenScrollPixelsUp](all/ScreenScrollPixelsUp.md) | `$020EB0` |
| [SetDrawFGColorA](all/SetDrawFGColorA.md) | `$021A28` |
| [SetGraphicsHook](all/SetGraphicsHook.md) | `$0214AC` |
| [SetWhiteDrawBGColor](all/SetWhiteDrawBGColor.md) | `$021BC8` |
| [UCLines](all/UCLines.md) | `$020B14` |
| [UnhighlightRect](all/UnhighlightRect.md) | `$0219CC` |
| [VerticalLine](all/VerticalLine.md) | `$021258` |

## Hooks

| Call | Address |
| --- | --- |
| [CallFontHook](all/CallFontHook.md) | `$020130` |
| [CallLocalizeHook](all/CallLocalizeHook.md) | `$020134` |

## Keyboard

| Call | Address |
| --- | --- |
| [GetCSC](all/GetCSC.md) | `$02014C` |
| [KbdScan](all/KbdScan.md) | `$020148` |

## Load

| Call | Address |
| --- | --- |
| [LoadHLInd_s](all/LoadHLInd_s.md) | `$020138` |

## System

| Call | Address |
| --- | --- |
| [AdjMath](all/AdjMath.md) | `$020578` |
| [ApdSetup](all/ApdSetup.md) | `$021144` |
| [ArcChk](all/ArcChk.md) | `$022040` |
| [BootOS](all/BootOS.md) | `$020108` |
| [CoorMon](all/CoorMon.md) | `$020150` |
| [JErrorNo](all/JErrorNo.md) | `$02012C` |
| [Mon](all/Mon.md) | `$020154` |
| [MonForceKey](all/MonForceKey.md) | `$020158` |
| [Rst10Handler](all/Rst10Handler.md) | `$020110` |
| [Rst18Handler](all/Rst18Handler.md) | `$020114` |
| [Rst20Handler](all/Rst20Handler.md) | `$020118` |
| [Rst28Handler](all/Rst28Handler.md) | `$02011C` |
| [Rst30Handler](all/Rst30Handler.md) | `$020120` |
| [SendKPress](all/SendKPress.md) | `$02015C` |

## Variables

| Call | Address |
| --- | --- |
| [AnsName](all/AnsName.md) | `$020FF4` |
| [Arc_Unarc](all/Arc_Unarc.md) | `$021448` |
| [ArchiveVar](all/ArchiveVar.md) | `$02144C` |
