---
title: AppSetup
geekdocHidden: true
params:
    address: $021148
    category: Apps
    name: AppSetup
---

### Address: $021148

Cleans up flags and hooks before running a flash application.

### Inputs:
* Set bit in [`hookflags2Override`](../../memory/all/flags/hookflags2Override.md), [`hookflags3Override`](../../memory/all/flags/hookflags3Override.md), or [`hookflags4Override`](../../memory/all/flags/hookflags4Override.md) corresponding to a [`hookflags2`](../../memory/all/flags/hookflags2.md), [`hookflags3`](../../memory/all/flags/hookflags3.md), or [`hookflags4`](../../memory/all/flags/hookflags4.md) hook to uninstall that hook.

### Outputs:
* Reset [`bufferOnly, (flags + plotFlag3)`](../../memory/all/flags/plotFlag3.md#bit-0---bufferonly).
* Reset [`appRunning, (flags + APIFlg)`](../../memory/all/flags/APIFlg.md#bit-4---apprunning).
* Zeroes out [`textFlags`](../../memory/all/flags/textFlags.md), [`apiFlg2`](../../memory/all/flags/apiFlg2.md), [`apiFlg3`](../../memory/all/flags/apiFlg3.md), [`apiFlg4`](../../memory/all/flags/apiFlg4.md), [`hookflags2Override`](../../memory/all/flags/hookflags2Override.md), [`hookflags3Override`](../../memory/all/flags/hookflags3Override.md), and [`hookflags4Override`](../../memory/all/flags/hookflags4Override.md).

### Destroys:
* `af`, `hl`
