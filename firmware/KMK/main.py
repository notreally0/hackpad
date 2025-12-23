import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Tap
from kmk.extensions.neopixel import NeoPixel

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.matrix = KeysScanner(
    pins=[
        board.GP3,   # SW1
        board.GP4,   # SW2
        board.GP2,   # SW3
        board.GP1,   # SW4
        board.GP26,  # SW5
        board.GP27,  # SW6
    ],
    value_when_pressed=False,
)

# Macros
COPY = KC.LCTL(KC.C)
CUT = KC.LCTL(KC.X)
UNDO = KC.LCTL(KC.Z)
ALT_TAB = KC.LALT(KC.TAB)
TERMINAL = KC.LCTL(KC.LALT(KC.T))

GIT_STATUS = KC.MACRO(
    Tap(KC.G), Tap(KC.I), Tap(KC.T),
    Tap(KC.SPACE),
    Tap(KC.S), Tap(KC.T), Tap(KC.A),
    Tap(KC.T), Tap(KC.U), Tap(KC.S),
)
keyboard.keymap = [[
    COPY,        # SW1
    CUT,         # SW2
    UNDO,        # SW3
    ALT_TAB,     # SW4
    TERMINAL,    # SW5
    GIT_STATUS,  # SW6
]]

neopixel = NeoPixel(
    pin=board.GP28,
    num_pixels=1,
    brightness=0.3,
)

keyboard.extensions.append(neopixel)

keyboard.go()
