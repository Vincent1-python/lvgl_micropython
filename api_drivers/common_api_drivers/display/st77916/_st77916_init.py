import time
import lvgl as lv  # NOQA
from display_driver_framework import BYTE_ORDER_BGR

_CSC1 = const(0xF0)
_CSC2 = const(0xF1)
_CSC3 = const(0xF2)
_CSC4 = const(0xF3)
_SPIOR = const(0xF4)

# command table 1
_SLPOUT = const(0x11)
_TEOFF = const(0x34)
_INVON = const(0x21)
_RASET = const(0x2B)
_CASET = const(0x2A)
_RAMCLACT = const(0x4C)
_RAMCLSETR = const(0x4D)
_RAMCLSETG = const(0x4E)
_RAMCLSETB = const(0x4F)
_DISPON = const(0x29)
_MADCTL = const(0x36)
_COLMOD = const(0x3A)

# command table 2
_VRHPS = const(0xB0)
_VRHNS = const(0xB1)
_VCOMS = const(0xB2)
_GAMOPPS = const(0xB4)
_STEP14S = const(0xB5)
_STEP23S = const(0xB6)
_SBSTS = const(0xB7)
_TCONS = const(0xBA)
_RGBVBP = const(0xBB)
_RGBHBP = const(0xBC)
_RGBSET = const(0xBD)
_FRCTRA1 = const(0xC0)
_FRCTRA2 = const(0xC1)
_FRCTRA3 = const(0xC2)
_FRCTRB1 = const(0xC3)
_FRCTRB2 = const(0xC4)
_FRCTRB3 = const(0xC5)
_PWRCTRA1 = const(0xC6)
_PWRCTRA2 = const(0xC7)
_PWRCTRA3 = const(0xC8)
_PWRCTRB1 = const(0xC9)
_PWRCTRB2 = const(0xCA)
_PWRCTRB3 = const(0xCB)
_RESSET1 = const(0xD0)
_RESSET2 = const(0xD1)
_RESSET3 = const(0xD2)
_VCMOFSET = const(0xDD)
_VCMOFNSET = const(0xDE)
_GAMCTRP1 = const(0xE0)
_GAMCTRN1 = const(0xE1)

lcd_init_cmds = [
    (0xF0, bytes([0x28]), 1, 0), # CSC1
    (0xF2, bytes([0x28]), 1, 0), # CSC3
    (0x73, bytes([0xF0]), 1, 0), # unknown
    (0x7C, bytes([0xD1]), 1, 0), # unknown
    (0x83, bytes([0xE0]), 1, 0), # unknown
    (0x84, bytes([0x61]), 1, 0),
    (0xF2, bytes([0x82]), 1, 0), # CSC3
    (0xF0, bytes([0x00]), 1, 0), # CSC1
    (0xF0, bytes([0x01]), 1, 0), # CSC1
    (0xF1, bytes([0x01]), 1, 0), # CSC2
    (0xB0, bytes([0x56]), 1, 0), # VRHPS
    (0xB1, bytes([0x4D]), 1, 0), # VRHNS
    (0xB2, bytes([0x24]), 1, 0), # VCOMS
    (0xB4, bytes([0x87]), 1, 0), # GAMOPPS
    (0xB5, bytes([0x44]), 1, 0), # STEP14S
    (0xB6, bytes([0x8B]), 1, 0), # STEP23S
    (0xB7, bytes([0x40]), 1, 0), # SBSTS
    (0xB8, bytes([0x86]), 1, 0), # unknown
    (0xBA, bytes([0x00]), 1, 0), # TCONS
    (0xBB, bytes([0x08]), 1, 0), # RGBVBP
    (0xBC, bytes([0x08]), 1, 0), # RGBHBP
    (0xBD, bytes([0x00]), 1, 0), # RGBSET
    (0xC0, bytes([0x80]), 1, 0), # FRCTRA1
    (0xC1, bytes([0x10]), 1, 0), # FRCTRA2
    (0xC2, bytes([0x37]), 1, 0), # FRCTRA3
    (0xC3, bytes([0x80]), 1, 0), # FRCTRB1
    (0xC4, bytes([0x10]), 1, 0), # FRCTRB2
    (0xC5, bytes([0x37]), 1, 0), # FRCTRB3
    (0xC6, bytes([0xA9]), 1, 0), # PWRCTRA1
    (0xC7, bytes([0x41]), 1, 0), # PWRCTRA2
    (0xC8, bytes([0x01]), 1, 0), # PWRCTRA3
    (0xC9, bytes([0xA9]), 1, 0), # PWRCTRB1
    (0xCA, bytes([0x41]), 1, 0), # PWRCTRB2
    (0xCB, bytes([0x01]), 1, 0), # PWRCTRB3
    (0xD0, bytes([0x91]), 1, 0), # RESSET1
    (0xD1, bytes([0x68]), 1, 0), # RESSET2
    (0xD2, bytes([0x68]), 1, 0), # RESSET3
    (0xF5, bytes([0x00, 0xA5]), 2, 0), # unknown
    (0xDD, bytes([0x4F]), 1, 0), # VCMOFSET
    (0xDE, bytes([0x4F]), 1, 0), # VCMOFNSET
    (0xF1, bytes([0x10]), 1, 0), # CSC2
    (0xF0, bytes([0x00]), 1, 0), # CSC1
    (0xF0, bytes([0x02]), 1, 0), # CSC1
    (0xE0, bytes([0xF0, 0x0A, 0x10, 0x09, 0x09, 0x36, 0x35, 0x33, 0x4A, 0x29, 0x15, 0x15, 0x2E, 0x34]), 14, 0), # GAMCTRP1
    (0xE1, bytes([0xF0, 0x0A, 0x0F, 0x08, 0x08, 0x05, 0x34, 0x33, 0x4A, 0x39, 0x15, 0x15, 0x2D, 0x33]), 14, 0), # GAMCTRN1
    (0xF0, bytes([0x10]), 1, 0), # CSC1
    (0xF3, bytes([0x10]), 1, 0), # CSC4
    (0xE0, bytes([0x07]), 1, 0), # GAMCTRP1
    (0xE1, bytes([0x00]), 1, 0), # GAMCTRN1
    (0xE2, bytes([0x00]), 1, 0), 
    (0xE3, bytes([0x00]), 1, 0),
    (0xE4, bytes([0xE0]), 1, 0),
    (0xE5, bytes([0x06]), 1, 0),
    (0xE6, bytes([0x21]), 1, 0),
    (0xE7, bytes([0x01]), 1, 0),
    (0xE8, bytes([0x05]), 1, 0),
    (0xE9, bytes([0x02]), 1, 0),
    (0xEA, bytes([0xDA]), 1, 0),
    (0xEB, bytes([0x00]), 1, 0),
    (0xEC, bytes([0x00]), 1, 0),
    (0xED, bytes([0x0F]), 1, 0),
    (0xEE, bytes([0x00]), 1, 0),
    (0xEF, bytes([0x00]), 1, 0),
    (0xF8, bytes([0x00]), 1, 0),
    (0xF9, bytes([0x00]), 1, 0),
    (0xFA, bytes([0x00]), 1, 0),
    (0xFB, bytes([0x00]), 1, 0),
    (0xFC, bytes([0x00]), 1, 0),
    (0xFD, bytes([0x00]), 1, 0),
    (0xFE, bytes([0x00]), 1, 0),
    (0xFF, bytes([0x00]), 1, 0),
    (0x60, bytes([0x40]), 1, 0), 
    (0x61, bytes([0x04]), 1, 0),
    (0x62, bytes([0x00]), 1, 0),
    (0x63, bytes([0x42]), 1, 0),
    (0x64, bytes([0xD9]), 1, 0),
    (0x65, bytes([0x00]), 1, 0),
    (0x66, bytes([0x00]), 1, 0),
    (0x67, bytes([0x00]), 1, 0),
    (0x68, bytes([0x00]), 1, 0),
    (0x69, bytes([0x00]), 1, 0),
    (0x6A, bytes([0x00]), 1, 0),
    (0x6B, bytes([0x00]), 1, 0),
    (0x70, bytes([0x40]), 1, 0),
    (0x71, bytes([0x03]), 1, 0),
    (0x72, bytes([0x00]), 1, 0),
    (0x73, bytes([0x42]), 1, 0),
    (0x74, bytes([0xD8]), 1, 0),
    (0x75, bytes([0x00]), 1, 0),
    (0x76, bytes([0x00]), 1, 0),
    (0x77, bytes([0x00]), 1, 0),
    (0x78, bytes([0x00]), 1, 0),
    (0x79, bytes([0x00]), 1, 0),
    (0x7A, bytes([0x00]), 1, 0),
    (0x7B, bytes([0x00]), 1, 0),
    (0x80, bytes([0x48]), 1, 0),
    (0x81, bytes([0x00]), 1, 0),
    (0x82, bytes([0x06]), 1, 0),
    (0x83, bytes([0x02]), 1, 0),
    (0x84, bytes([0xD6]), 1, 0),
    (0x85, bytes([0x04]), 1, 0),
    (0x86, bytes([0x00]), 1, 0),
    (0x87, bytes([0x00]), 1, 0),
    (0x88, bytes([0x48]), 1, 0),
    (0x89, bytes([0x00]), 1, 0),
    (0x8A, bytes([0x08]), 1, 0),
    (0x8B, bytes([0x02]), 1, 0),
    (0x8C, bytes([0xD8]), 1, 0),
    (0x8D, bytes([0x04]), 1, 0),
    (0x8E, bytes([0x00]), 1, 0),
    (0x8F, bytes([0x00]), 1, 0),
    (0x90, bytes([0x48]), 1, 0),
    (0x91, bytes([0x00]), 1, 0),
    (0x92, bytes([0x0A]), 1, 0),
    (0x93, bytes([0x02]), 1, 0),
    (0x94, bytes([0xDA]), 1, 0),
    (0x95, bytes([0x04]), 1, 0),
    (0x96, bytes([0x00]), 1, 0),
    (0x97, bytes([0x00]), 1, 0),
    (0x98, bytes([0x48]), 1, 0),
    (0x99, bytes([0x00]), 1, 0),
    (0x9A, bytes([0x0C]), 1, 0),
    (0x9B, bytes([0x02]), 1, 0),
    (0x9C, bytes([0xDC]), 1, 0),
    (0x9D, bytes([0x04]), 1, 0),
    (0x9E, bytes([0x00]), 1, 0),
    (0x9F, bytes([0x00]), 1, 0),
    (0xA0, bytes([0x48]), 1, 0),
    (0xA1, bytes([0x00]), 1, 0),
    (0xA2, bytes([0x05]), 1, 0),
    (0xA3, bytes([0x02]), 1, 0),
    (0xA4, bytes([0xD5]), 1, 0),
    (0xA5, bytes([0x04]), 1, 0),
    (0xA6, bytes([0x00]), 1, 0),
    (0xA7, bytes([0x00]), 1, 0),
    (0xA8, bytes([0x48]), 1, 0),
    (0xA9, bytes([0x00]), 1, 0),
    (0xAA, bytes([0x07]), 1, 0),
    (0xAB, bytes([0x02]), 1, 0),
    (0xAC, bytes([0xD7]), 1, 0),
    (0xAD, bytes([0x04]), 1, 0),
    (0xAE, bytes([0x00]), 1, 0),
    (0xAF, bytes([0x00]), 1, 0),
    (0xB0, bytes([0x48]), 1, 0),
    (0xB1, bytes([0x00]), 1, 0),
    (0xB2, bytes([0x09]), 1, 0),
    (0xB3, bytes([0x02]), 1, 0),
    (0xB4, bytes([0xD9]), 1, 0),
    (0xB5, bytes([0x04]), 1, 0),
    (0xB6, bytes([0x00]), 1, 0),
    (0xB7, bytes([0x00]), 1, 0),
    (0xB8, bytes([0x48]), 1, 0),
    (0xB9, bytes([0x00]), 1, 0),
    (0xBA, bytes([0x0B]), 1, 0),
    (0xBB, bytes([0x02]), 1, 0),
    (0xBC, bytes([0xDB]), 1, 0),
    (0xBD, bytes([0x04]), 1, 0),
    (0xBE, bytes([0x00]), 1, 0),
    (0xBF, bytes([0x00]), 1, 0),
    (0xC0, bytes([0x10]), 1, 0),
    (0xC1, bytes([0x47]), 1, 0),
    (0xC2, bytes([0x56]), 1, 0),
    (0xC3, bytes([0x65]), 1, 0),
    (0xC4, bytes([0x74]), 1, 0),
    (0xC5, bytes([0x88]), 1, 0),
    (0xC6, bytes([0x99]), 1, 0),
    (0xC7, bytes([0x01]), 1, 0),
    (0xC8, bytes([0xBB]), 1, 0),
    (0xC9, bytes([0xAA]), 1, 0),
    (0xD0, bytes([0x10]), 1, 0),
    (0xD1, bytes([0x47]), 1, 0),
    (0xD2, bytes([0x56]), 1, 0),
    (0xD3, bytes([0x65]), 1, 0),
    (0xD4, bytes([0x74]), 1, 0),
    (0xD5, bytes([0x88]), 1, 0),
    (0xD6, bytes([0x99]), 1, 0),
    (0xD7, bytes([0x01]), 1, 0),
    (0xD8, bytes([0xBB]), 1, 0),
    (0xD9, bytes([0xAA]), 1, 0),
    (0xF3, bytes([0x01]), 1, 0), # CSC4
    (0xF0, bytes([0x00]), 1, 0), # CSC1
    (0x21, bytes([0x00]), 1, 0), # INVON: invert display colors
    (0x11, bytes([0x00]), 1, 120), # SLPOUT: sleep out, delay 120ms
    (0x29, bytes([0x00]), 1, 0), # DISPON: turn on display
]

def init(self):
    print("Initializing Waveshare ESP32-S3 1.8 inch knob display - ST77916")

    param_buf = bytearray(14)
    param_mv = memoryview(param_buf)

    for cmd, params, param_len, delay in lcd_init_cmds:
        param_buf[:param_len] = params

        self.set_params(cmd, param_mv[:param_len])
        if delay:
            time.sleep_ms(delay)

    color_size = lv.color_format_get_size(self._color_space)
    if color_size == 2:  # NOQA
        pixel_format = 0x55
    elif color_size == 3:
        pixel_format = 0x66
    else:
        raise RuntimeError(
            'IC only supports '
            'lv.COLOR_FORMAT.RGB565 or lv.COLOR_FORMAT.RGB888'
        )

    param_buf[0] = pixel_format
    self.set_params(_COLMOD, param_mv[:1])

    # Set MADCTL for RGB/BGR
    if self._color_byte_order == BYTE_ORDER_BGR \
        and self._color_space == lv.COLOR_FORMAT.RGB888:
        madctl_param = 0x08  # BGR
    else:
        madctl_param = 0x00  # RGB

    param_buf[0] = madctl_param
    self.set_params(_MADCTL, param_mv[:1])

