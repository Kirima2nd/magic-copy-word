# --------------------------------------------
#              Unscrambler Word
# --------------------------------------------
# Just copy your scrambled word and
# This code will replace your scrambled word
# with unscrambled one
#
# Thanks for tinmarr for the code which you
# can found it below: 
# https://github.com/tinmarr/Word-Unscrambler
#
# --------------------------------------------


import time
import mouse
import keyboard
import pyperclip

import scrambler

# Always toggle the key false to prevent
# unnecessary things happend
toggleKeys = False

print('------------------------------')
print('      Unscrambler Word        ')
print('------------------------------')
print('                              ')
print('Keys List:                    ')
print(' * F4      - Toggle ON/OFF    ')
print(' * CTRL+C  - Word Unscrambler ')
print(' * F10     - Exit Application ')
print('------------------------------')

while True:
    if keyboard.is_pressed('f4'):
        if toggleKeys == False:
            toggleKeys = True
            print('Key Toggled: ON')

        elif toggleKeys == True:
            toggleKeys = False
            print('Key Toggled: OFF')
        pass
    elif keyboard.is_pressed('ctrl+c') and toggleKeys:
        # Why sleep? because without this, pyperclip
        # cannot grab the copied text on windows
        # thats why i'm delaying the script to
        # pyperclip being able to get your copied text
        time.sleep(1.5)

        copy_word = pyperclip.paste()
        result = scrambler.Unscramble(copy_word)
        tmp = ''.join(result)
        pyperclip.copy(tmp)

        print(f'Word unscrambled, the result is: {tmp}')
        pass
    if keyboard.is_pressed('f10'):
        print('Exiting Application!')
        break
