# Copyright (c) 2024 - 2025 Kevin G. Schlosser

import time


def init(self):
    param_buf = bytearray(16)
    param_mv = memoryview(param_buf)

    self.reset()

    # ------------------------------------------------------------------
    #  ST7365P initialization —— rewritten into the required format
    # ------------------------------------------------------------------

    # Pump ratio control (F7h)
    param_buf[:4] = bytearray([0xA9, 0x51, 0x2C, 0x82])
    self.set_params(0xF7, param_mv[:4])

    # Power control 2 (C0h)
    param_buf[:2] = bytearray([0x11, 0x09])
    self.set_params(0xC0, param_mv[:2])

    # Power control 3 (C1h)
    param_buf[0] = 0x41
    self.set_params(0xC1, param_mv[:1])

    # VCOM control 2 (C5h)
    param_buf[:3] = bytearray([0x00, 0x0A, 0x80])
    self.set_params(0xC5, param_mv[:3])

    # Frame rate control (B1h)
    param_buf[:2] = bytearray([0xB0, 0x11])
    self.set_params(0xB1, param_mv[:2])

    # Display inversion control (B4h)
    param_buf[0] = 0x02
    self.set_params(0xB4, param_mv[:1])

    # Display function control (B6h)
    param_buf[:2] = bytearray([0x02, 0x22])
    self.set_params(0xB6, param_mv[:2])

    # Entry mode set (B7h)
    param_buf[0] = 0xC6
    self.set_params(0xB7, param_mv[:1])

    # VCOM control 1 (BEh)
    param_buf[:2] = bytearray([0x00, 0x04])
    self.set_params(0xBE, param_mv[:2])

    # Power control A (E9h)
    param_buf[0] = 0x00
    self.set_params(0xE9, param_mv[:1])

    # Memory data access control (36h)
    param_buf[0] = 0x08
    self.set_params(0x36, param_mv[:1])

    # Interface pixel format (3Ah) -> 18-bit/pixel
    param_buf[0] = 0x66
    self.set_params(0x3A, param_mv[:1])

    # Positive gamma correction (E0h) – 15 bytes
    param_buf[:15] = bytearray([
        0x00, 0x07, 0x10, 0x09, 0x17, 0x0B, 0x41, 0x89,
        0x4B, 0x0A, 0x0C, 0x0E, 0x18, 0x1B, 0x0F
    ])
    self.set_params(0xE0, param_mv[:15])

    # Negative gamma correction (E1h) – 15 bytes
    param_buf[:15] = bytearray([
        0x00, 0x17, 0x1A, 0x04, 0x0E, 0x06, 0x2F, 0x45,
        0x43, 0x02, 0x0A, 0x09, 0x32, 0x36, 0x0F
    ])
    self.set_params(0xE1, param_mv[:15])

    # Sleep out (11h)
    self.set_params(0x11)
    time.sleep_ms(120)

    # Display on (29h)
    self.set_params(0x29)
