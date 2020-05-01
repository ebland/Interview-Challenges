'''
This file manages the emulators
'''

from pyautogui import typewrite, hotkey
import time
import subprocess
import sys


# These are the names of the devices I created in Android Studio. Named after Android version.
emulators = ('@7.0', '@6.0', '@5.1', '@4.4')


# This is a helper function for stopping the emulators when testing is finished.
def stop_emulators():
    hotkey('command', 'space')
    typewrite('iterm\n')
    hotkey('command', 'q')
    typewrite('\n')


# This is the function that runs when the user types "run emulators" and can be the initial starting point
# if using emulators only. It uses iTerminal so that it can be cleaned up more easily when finished testing
# by simply closing down iTerminal and thusly all the emulators.
def main(argv):
    if len(argv) <= 1:
        num_emulators = 1
    else:
        num_emulators = int(argv[1])
    print('\nStarting {} {} emulators\n'.format(str(num_emulators), 'Android'))
    print('Please be patient')
    print('This may take several minutes\n')
    hotkey('command', 'space')
    typewrite('iterm\n')
    time.sleep(2)
    for i in range(num_emulators):
        typewrite('cd ~/Library/Android/sdk/emulator\n')
        typewrite('emulator ' + emulators[i] + '\n')
        time.sleep(20)
        if i == num_emulators - 1:
            break
        else:
            hotkey('command', 'space')
            typewrite('iterm\n')
            hotkey('command', 't')
    time.sleep(5 * num_emulators)
    hotkey('command', 'space')
    typewrite('terminal\n')
    time.sleep(1)
    typewrite('run tools\n\n')

if __name__ == '__main__':
    subprocess.call('clear')
    main(sys.argv)
