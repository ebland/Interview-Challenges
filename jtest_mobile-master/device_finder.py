'''
This file gets the devices that are recognized by ADB.
It recognizes them using the devices.py file and then
lists the devices to the user.
'''

import subprocess
import device_db
from copy import copy


# This function gets the devices from ADB and creates a list of attached devices
def get_devices_from_adb():
    subprocess.call(('adb', 'devices'))
    subprocess.call('clear')
    output = subprocess.check_output(('adb', 'devices'))
    chunks = output.split(b' ')
    for chunk in chunks:
        if b'\n' in chunk:
            id_data = chunk
            break
    ids = id_data.splitlines()
    device_ids = []
    for id in ids:
        id = id.decode()
        if 'device' in id:
            id = id.replace('device', '')
            id = id.strip(' \t')
            device_ids.append(id)
    return device_ids


# This function lists the known devices and creates an array of them for use later
def list_connected_devices():
    found_devices = {}
    device_ids = get_devices_from_adb()
    print('Connected devices: ')
    for i, id in enumerate(device_ids):
        if 'emulator' in id:
            found_devices[i + 1] = copy(device_db.test_android)
            found_devices[i + 1]['platformVersion'] = device_db.emulator_version[i]
            found_devices[i + 1]['udid'] = id
            print(str(i + 1), ': ', found_devices[i + 1]['deviceName'], found_devices[i + 1]['platformVersion'], str(id))
        else:
            for device in device_db.devices:
                if device.get('udid') == id:
                    print(str(i + 1), ': ', device['deviceName'])
                    found_devices[i + 1] = copy(device) # need to copy object or everything gets the same
                    break
            else:
                print(str(i + 1), ': Unknown device: ', str(id))
    return found_devices
