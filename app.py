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

import mouse
import keyboard
import pyperclip
import asyncio

import scrambler

async def main():
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
            await asyncio.sleep(1.0)

            if toggleKeys == False:
                toggleKeys = True
                print('Key Toggled: ON')

            elif toggleKeys == True:
                toggleKeys = False
                print('Key Toggled: OFF')
            pass

        elif keyboard.is_pressed('ctrl+c') and toggleKeys:
            await asyncio.sleep(1.0)

            copy_word = pyperclip.paste()
            result = scrambler.Unscramble(copy_word)

            if result == 'Nothing was found.': 
                result = await scrambler.Guess(copy_word)

            pyperclip.copy(result)

            print(f'Word unscrambled, the result is: {result}')
            pass

        if keyboard.is_pressed('f10'):
            print('Exiting Application!')
            break

asyncio.run(main())
