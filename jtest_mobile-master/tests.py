'''
This file hosts the test cases that will be run on the devices.
To add a test, simply create a new function with the name of the test you'd like it to be.
Then write any basic Selenium test.
'''

from concurrent import futures
from time import sleep


# GLOBAL VARIABLES
url = 'http://www.google.com/'
devices = {}

# This function sets the target devices and must be run before the tests will work.
def test_on(target_devices):
    global devices
    devices = target_devices
    print('\nSetup Complete\nReady for testing')

# This function will allow you to set any url
def set_url(desired_url):
    global url
    if 'http' not in desired_url:
        url = 'http://' + desired_url

# This function refreshes the webdriver for a device
def refresh(device):
    devices[device]['driver'].refresh()

# MAIN FUNCTION
# This function takes the name of a test function and runs that function asyncronysly on all the target devices.
def test(func_name, *optional_params):
    ex = futures.ThreadPoolExecutor()
    if optional_params:
        for result in ex.map(func_name, list(devices), optional_params):
            print(result)
    else:
        for result in ex.map(func_name, list(devices)):
            print(result)


# TESTS
# Below are the test functions

def go_to_site(device, quiet=False):
    sleep(2)
    if not quiet:
        print('Navigating to ', url, ' on ', devices[device]['deviceName'])
    devices[device]['driver'].get(url)
    return True

def perform_search(device, search_term):
    sleep(2)
    print('Navigating to ', url, ' on ', devices[device]['deviceName'])
    driver = devices[device]['driver']
    search_field = driver.find_element_by_name('q')
    search_field.send_keys(search_term)
    driver.find_element_by_id('tsbb').click()

# BELOW IS EXAMPLES THAT DO NOT WORK WITH THIS VERSION OF THE CODE
# MORE TESTS WERE REMOVED WHEN MAKING THIS CODE GENERIC FOR SHARING
# JUST HERE FOR EXAMPLE
#
# def accept_site_agreement(device):
#     sleep(2)
#     print('Accepting site agreement on ', devices[device]['deviceName'])
#     agree_button = devices[device]['driver'].find_element_by_id('close_entrance_terms')
#     agree_button.click()
#     devices[device]['driver'].refresh() # need to refresh or sometimes the pictures dont load
#     return True
#
# def decline_site_agreement(device):
#     sleep(2)
#     print('Declining site agreement on ', devices[device]['deviceName'])
#     exit_button = devices[device]['driver'].find_element_by_id('et-exit')
#     exit_button.click()
#     return True
#
# def login(device):
#     sleep(2)
#     print('Logging in as ', username, ' on ', devices[device]['deviceName'])
#     driver = devices[device]['driver']
#     nav_menu_button = driver.find_element_by_id('mmnav')
#     nav_menu_button.click()
#     nav_menu = driver.find_element_by_class_name('pushmenu')
#     nav_menu_items = nav_menu.find_elements_by_tag_name('li')
#     for item in nav_menu_items:
#         link = item.find_element_by_tag_name('a')
#         if link.get_attribute('innerHTML') == 'Login':
#             link.click()
#             break
#     username_field = driver.find_element_by_id('id_username')
#     pw_field = driver.find_element_by_id('id_password')
#     sleep(1)
#     buttons = driver.find_elements_by_class_name('submit')
#     username_field.send_keys(username)
#     pw_field.send_keys(userpw)
#     buttons[0].click()
#     sleep(2)
#     return True


if __name__ == '__main__':
    print('\nTests initialized')
