$ErrorActionPreference = 'Stop'
$core = Join-Path $PSScriptRoot '../../iline-tests/cemu-source/core'
$sources = Get-ChildItem -LiteralPath $core -Recurse -Filter '*.c' |
    Where-Object { $_.FullName -notmatch '[\\/]arm[\\/]' -and $_.Name -ne 'os-linux.c' }
gcc -O2 -std=gnu11 -shared -static-libgcc -DDEBUG_SUPPORT -I $core -o (Join-Path $PSScriptRoot 'runner.dll') (Join-Path $PSScriptRoot 'runner.c') @($sources.FullName)
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
