import pyautogui
import time

# Define the image filenames to search for
invite = 'confirm.png'
join = 'join.png'
ready = 'ready.png'
ok = 'ok.png'
mpOK = 'mpOK.png'

# Define the action to perform when the image is found
action = 'click'
click_coords = (100, 200)  # Coordinates for mouse click

state = 0

while True:
    # take a screenshot
    pyautogui.screenshot('screenshot.png')

    # Search for the image on the screen
    image = pyautogui.locateOnScreen(invite)
    if image is not None:
        print('confirm')
        if action == 'click':
            # Get the center coordinates of the image
            image_center_x, image_center_y = pyautogui.center(image)
            # Perform the click action on the center coordinates
            pyautogui.click(image_center_x, image_center_y)
            time.sleep(1)

    # check for join button
    image = pyautogui.locateOnScreen(join)
    if image is not None:
        print('join')
        if action == 'click':
            image_center_x, image_center_y = pyautogui.center(image)
            pyautogui.click(image_center_x, image_center_y)
            time.sleep(1)
    
    # check for ready button
    image = pyautogui.locateOnScreen(ready)
    if image is not None:
        print('ready')
        if action == 'click':
            image_center_x, image_center_y = pyautogui.center(image)
            pyautogui.click(image_center_x, image_center_y)
            time.sleep(1)
    
    # check for ok button
    image = pyautogui.locateOnScreen(ok)
    if image is not None:
        print('ok')
        if action == 'click':
            image_center_x, image_center_y = pyautogui.center(image)
            pyautogui.click(image_center_x, image_center_y)
            time.sleep(1)

    # check for mpOK button
    image = pyautogui.locateOnScreen(mpOK)
    if image is not None:
        print('mpOK')
        if action == 'click':
            image_center_x, image_center_y = pyautogui.center(image)
            pyautogui.click(image_center_x, image_center_y)
            time.sleep(1)

    # If no image is found, meaning in-game, then send 's+a' to keep the game alive
    if image is None:
        print('no image, in-game')