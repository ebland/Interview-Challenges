'''
This file handles setting up the testing functionality as well as cleaning up when finished.
'''

import pyautogui
from time import sleep
import device_finder, device_manager, appium_manager
from concurrent import futures
from emulators import stop_emulators


# This variable needs to be global so that everything can access it after being set.
target_devices = {}

# This function manages the user input and runs the background processes to initialize everything
# using the other files. Finally, it sets the target devices as the global variable so that the user
# can use them for testing with the tests.py file
def start_tools():
    global target_devices
    found_devices = device_finder.list_connected_devices()
    user_input = input('Desired devices (eg. 1,2,3, all): ')
    print('\nSetup started\n')
    target_devices = device_manager.set_target_devices(user_input, found_devices)
    print('Launching Appium servers\n')
    target_devices = appium_manager.tie_devices_to_ports(target_devices)
    print('\nStarting webdrivers')
    print('Please be patient')
    sleep(3 * len(target_devices))
    target_devices = device_manager.set_browser(target_devices)

# This function initializes cleanup of everything. Closes emulators, shuts down Appium servers and closes
# any additional windows that were created during setup
def stop_tools():
    global target_devices
    print('\nStopping webdrivers')
    print('please be patient')
    pyautogui.hotkey('alt', 'command', '2')
    for device in target_devices:
        try:
            print('Stopping webdriver on ', target_devices[device]['deviceName'])
            target_devices[device]['driver'].quit()
        except Exception as err:
            print('Swallowing Error: ', err)
            continue
    for index, device in enumerate(target_devices):
        if index == len(target_devices) and len(target_devices) > 1:
            break
        else:
            pyautogui.hotkey('command', '2')
            pyautogui.hotkey('command', 'w')
            pyautogui.hotkey('return')
    print('Shutdown complete')

# This function calls the stop_tools function and closes any emulators if they were also being used
# Also, this is quicker to type than stop_tools so it's somewhat of a wrapper method
def cleanup():
    stop_tools()
    try:
        stop_emulators()
    except Exception as e:
        pass

# This function will list the test information.
# This can most likely be done in a more elegant way in the future.
def info():
    print('''====================MOBILE TOOLS INFO=====================
    
                     AVAILABLE TESTS
                     
       to use, replace with name of desired test: 
                 example: test(TEST NAME)
                 
             TEST NAME: TEST DESCRIPTION
 accept_site_agreement: accepts the site agreement when visible
decline_site_agreement: declines the site agreement when visible
 view_first_listed_cam: views the broadcast of the current top cam
                 login: logs in
                 
==========================================================
    ''')

# This function continutes initialization and greets the user with further instructions
def main():
    global target_devices
    start_tools()
    ex = futures.ThreadPoolExecutor()
    raw_results = ex.map(appium_manager.start_webdriver, list(target_devices.values()))
    print('This can take a moment')
    results = list(raw_results)
    for index, device in enumerate(target_devices):
        target_devices[device]['driver'] = results[index]
    print('\nSetup complete\n')
    print('''=====================INSTRUCTIONS=========================
1. "run tests" to load mobile tests

2. "test_on(target_devices)" to begin testing

3. "info()" to view available tests and related information
    
4. "cleanup()" when done testing
==========================================================''')


if __name__ == '__main__':
    main()
