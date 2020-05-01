'''
This file manages creating the array of devices for use in the async testing
It also sets the browser and timeout settings
'''

import device_db


# This function takes the user choice of devices from the found devices and
# creates an array of devices
def set_target_devices(user_input, found_devices):
    target_devices = {}
    if user_input.lower() == 'all':
        return found_devices
    elif ',' not in user_input:
        targets = [user_input]
    else:
        targets = user_input.split(',')
    for target in targets:
        target_devices[target] = found_devices[int(target)]
    return target_devices


# This function sets the browser settings for the devices
def set_browser(target_devices):
    for device in target_devices:
        target_devices[device]['browserName'] = device_db.browsers[0]
        target_devices[device]['newCommandTimeout'] = 0
    return target_devices



