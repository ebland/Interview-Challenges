# jtest_mobile
**This is a work in progress and is not intended for general distribution at this time.

***Due to the desires of the company this was written at, there were not initially comments.

***Comments have been added after the fact when uploading generic version to github for sharing






A Mac specific Python framework for running concurrent tests on websites using multiple physical Android devices or emulators. (Chrome only for now)

Requires the following to operate:
- Mac OS
- iTerminal
- Android SDK
- Appium
- Pyautogui
- iPython

Written in Python 3 but should be compatible with Python 2 systems.

To Use:
1. Open Terminal and navigate to the containing folder.
2. Start up iPython.
3. Type "run emulators" (to run more than one emulator you may add an integer as a parameter indicating the number of emulators you'd like. By default, 1 will be started.
NOTE: AFTER ISSUING A COMMAND, PLEASE WAIT FOR COMMAND TO FINISH. USING YOUR COMPUTER WILL CAUSE THE AUTOMATION TO GO HAYWIRE
4. Next, in Terminal, type "run tools". (You may start with this step if you do not wish to use emulators. Just make sure that your physical devices are plugged in via usb before you run tools)
5. You may select whichever devices you would like to run the tests on (separated by commas) or just type "all" to run tests on all available devices.
6. After Appium is finished setting up you will be met with instructions. Basically, the next two things you will do is "run tests" followed by "test_on(target_devices)"
7. At this point you may run a test by issuing the test command with the name of the desired test case as a parameter like "test(test_name)" where test_name is the name of the desired test case function in the tests.py file.
