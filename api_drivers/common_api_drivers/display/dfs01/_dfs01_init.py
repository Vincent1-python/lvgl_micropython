# Copyright (c) 2024 - 2025 Kevin G. Schlosser

from micropython import const  # NOQA
import time

def init(self):
    self.reset()

    self.set_params(0x11)
    time.sleep_ms(120) # NOQA

    self.set_params(0x29)
    time.sleep_ms(20) # NOQA
