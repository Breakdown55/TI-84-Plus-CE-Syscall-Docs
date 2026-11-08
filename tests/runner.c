#include <stdbool.h>
#include <stdarg.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "cpu.h"
#include "emu.h"
#include "interrupt.h"
#include "mem.h"

enum { RAM_BASE = 0xD00000, ENTRY = 0xD1C000, STACK = 0xD23F00 };

void gui_console_clear(void) {}
void gui_console_printf(const char *format, ...) { (void)format; }
void gui_console_err_printf(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vfprintf(stderr, format, args);
    va_end(args);
}
asic_rev_t gui_handle_reset(const boot_ver_t *version, asic_rev_t loaded,
                           asic_rev_t fallback, bool *python) {
    (void)version;
    (void)loaded;
    (void)python;
    return fallback;
}

__declspec(dllexport) uint8_t *load_state(const char *image) {
    if (emu_load(EMU_DATA_IMAGE, image) != EMU_STATE_VALID || !emu_set_run_rate(1000)) return NULL;
    return mem.ram.block;
}

/* Input and output arrays use AF, BC, DE, HL, IX, IY, alternate AF/BC/DE/HL,
   and the interrupt-enable state. Verify that each call returns to the harness. */
__declspec(dllexport) uint32_t invoke(uint32_t address, uint32_t *regs, uint32_t lcd_base) {
    const uint8_t code[] = {0xCD, address, address >> 8, address >> 16, 0x76};
    memcpy(mem.ram.block + ENTRY - RAM_BASE, code, sizeof code);
    mem_poke_long(0xE30010, lcd_base);
    cpu.registers.AF = regs[0];
    cpu.registers.BC = regs[1];
    cpu.registers.DE = regs[2];
    cpu.registers.HL = regs[3];
    cpu.registers.IX = regs[4];
    cpu.registers.IY = regs[5];
    cpu.registers._AF = regs[6];
    cpu.registers._BC = regs[7];
    cpu.registers._DE = regs[8];
    cpu.registers._HL = regs[9];
    cpu.registers.SPL = STACK;
    cpu.registers.SPS = 0xAA32;
    cpu.registers.MBASE = 0xD0;
    cpu.registers.I = 0x12;
    intrpt[0].enabled = intrpt[1].enabled = 0;
    cpu.IEF1 = cpu.IEF2 = regs[10] != 0;
    cpu.IEF_wait = cpu.halted = false;
    cpu_flush(ENTRY, true);
    for (unsigned i = 0; i < 50 && !cpu.halted; ++i) emu_run(2);
    if (!cpu.halted || cpu.registers.PC != ENTRY + sizeof code || cpu.registers.SPL != STACK ||
        cpu.registers.SPS != 0xAA32 || !cpu.ADL) return cpu.registers.PC | 0x1000000;
    regs[0] = cpu.registers.AF;
    regs[1] = cpu.registers.BC;
    regs[2] = cpu.registers.DE;
    regs[3] = cpu.registers.HL;
    regs[4] = cpu.registers.IX;
    regs[5] = cpu.registers.IY;
    regs[6] = cpu.registers._AF;
    regs[7] = cpu.registers._BC;
    regs[8] = cpu.registers._DE;
    regs[9] = cpu.registers._HL;
    regs[10] = cpu.IEF1 | ((uint32_t)cpu.IEF2 << 1);
    return 0;
}
