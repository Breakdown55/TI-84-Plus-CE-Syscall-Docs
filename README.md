# TI-84 Plus CE Assembly Manual

This Markdown reference covers TI-OS syscalls for eZ80 assembly programs. Each entry lists what to load before the call, what the call changes, and which registers to save. For graphics calls, VRAM holds the LCD pixels. `plotSScreen` and `saveSScreen` hold graph color codes separately.

- [Syscall index](syscalls/README.md)
- [Graphics entries](syscalls/README.md#graphics)
- [Graphics test coverage and results](tests/README.md)
- [Graphics OP1–OP6 read and write audit](tests/graphics-ops.md)

The manual imports the syscall pages and linked reference material from the [eZ80 docs](https://github.com/EzCE/ez80-docs) checkout. The imported material retains its [AGPL-3.0 license](LICENSE). Links and Hugo shortcodes were adapted for standalone Markdown. A few source references have no matching page in the checkout and appear as plain text.

New entries are based on the TI-OS 5.8.2 ROM and headless CEmu tests. **Additional Information** records less common choices that matter to callers, such as using a drawing hook or clearing one pane in split mode.
