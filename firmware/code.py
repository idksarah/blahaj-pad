import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D7, board.D8, board.D9]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
        [KC.MACRO( # skull
            Press(KC.LGUI),    
            Tap(KC.DOT),        
            Release(KC.LGUI),
            Release(KC.DOT),
            Tap(KC.S),
            Tap(KC.K),  
            Tap(KC.U),  
            Tap(KC.L),    
            Tap(KC.L),
            Tap(KC.ENTER),  
            Tap(KC.ESC)
        ), KC.MACRO( # broken heart
            Press(KC.LGUI),    
            Tap(KC.DOT),        
            Release(KC.LGUI),
            Release(KC.DOT),
            Tap(KC.B),
            Tap(KC.R),  
            Tap(KC.O),  
            Tap(KC.K),
            Tap(KC.ENTER),  
            Tap(KC.ESC)
        ), KC.MACRO( #pray
            Press(KC.LGUI),    
            Tap(KC.DOT),        
            Release(KC.LGUI),
            Release(KC.DOT),
            Tap(KC.P),
            Tap(KC.R),  
            Tap(KC.A),  
            Tap(KC.Y),    
            Tap(KC.ENTER),  
            Tap(KC.ESC)
        )]
]

# Start kmk!
if __name__ == '__main__':
    print("kmk startidng")
    keyboard.go()