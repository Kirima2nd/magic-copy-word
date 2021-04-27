# -----------------------------------------------------
#                Kirima2nd Magic Copy
# -----------------------------------------------------
# Toggle and just copy your text and this code
# will replace your scrambled word with unscrambled one
#
# Thanks for tinmarr, stackoverflow, vegaseat, zx9 <3
#
# -----------------------------------------------------

import keyboard
import pyperclip
import asyncio

import worker

async def main():
    toggleKeys = False
    reversedKeys = False
        
    print('----------------------------------')
    print('       Kirima2nd Magic Copy       ')
    print('----------------------------------')
    print('                                  ')
    print('Keys List:                        ')
    print(' * F4      - Toggle ON/OFF        ')
    print(' * F5      - Toggle Reversed      ')
    print(' * CTRL+C  - To do the magic      ')
    print(' * F10     - Exit Application     ')
    print('----------------------------------')

    while True:
        if keyboard.is_pressed('f4'):
            await asyncio.sleep(1.0)

            if reversedKeys == True:
                print('Disable Reversed Keys first!')
            elif toggleKeys == False:
                toggleKeys = True
                print('[App]: Key Toggled: ON')

            elif toggleKeys == True:
                toggleKeys = False
                print('[App]: Key Toggled: OFF')
            pass
        elif keyboard.is_pressed('f5'):
            await asyncio.sleep(1.0)

            if toggleKeys == True:
                toggleKeys = False
            
            if reversedKeys == False:
                reversedKeys = True
                print('[App]: Reversed Keys: ON')

            elif reversedKeys == True:
                reversedKeys = False
                print('[App]: Reversed Keys: OFF')
            pass
        elif keyboard.is_pressed('ctrl+c') and toggleKeys:
            await asyncio.sleep(1.0)

            copy_word = pyperclip.paste()

            if copy_word.count('_') < 2 or copy_word.count('?') < 2:
                result = worker.Unscramble(copy_word)
            else:
                result = worker.Guess(copy_word)

            pyperclip.copy(result)

            print(f'[App]: Word unscrambled, the result is: {result}')
            pass
        elif keyboard.is_pressed('ctrl+c') and reversedKeys:
            await asyncio.sleep(1.0)

            copy_word = pyperclip.paste()
            
            result = worker.Reverse(copy_word)
            pyperclip.copy(result)
            print(f'[App]: Word reversed, the result is: {result}')
            pass
        elif keyboard.is_pressed('f10'):
            print('[App]: Exiting Application!')
            break


if __name__ == "__main__":
    asyncio.run(main())
