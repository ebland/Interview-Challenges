'''
This file manages the Appium servers and attaching devices to them.
'''

import subprocess
from time import sleep
from pyautogui import typewrite, hotkey
from appium import webdriver


# This function opens an additional terminal window and as many tabs as there are devices being tested.
# Each tab holds an Appium server tied to a unique port
def start_appium_servers(number_of_servers, starting_port=4703):
    port = starting_port
    used_ports = []
    subprocess.Popen(('open', '-a', 'Terminal', '/'))
    for x in range(number_of_servers):
        port += 20
        sleep(1)
        typewrite('appium' + ' --port ' + str(port) + '\n')
        used_ports.append(port)
        if x == number_of_servers - 1:
            break
        hotkey('command', 't')
    hotkey('command', '1')
    hotkey('alt', 'command', '1')
    return used_ports


# This function ties the devices to the Appium servers. There can only be 1 device per server.
def tie_devices_to_ports(target_devices):
    appium_ports = start_appium_servers(len(target_devices))
    print('Attaching devices to server ports')
    for index, device in enumerate(target_devices):
        target_devices[device]['port'] = appium_ports[index]
        print(target_devices[device]['deviceName'], ' attached to server port ', str(target_devices[device]['port']))
    return target_devices


# This function starts the webdrivers on each Appium server
def start_webdriver(device):
    try:
        print('Starting webdriver for ', device['deviceName'])
        return webdriver.Remote('http://localhost:' + str(device['port']) + '/wd/hub', device)
    except Exception as err:
        print('Error starting webdriver for ', device['deviceName'], err)
