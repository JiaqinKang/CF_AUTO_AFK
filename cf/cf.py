import pyautogui
import time

# Define the image filenames to search for
invite = 'confirm.png'
join = 'join.png'
ready = 'ready.png'
ok = 'ok.png'
ok1='ok1.png'
ok2='ok2.png'
mpOK = 'mpOK.png'
blacklist = 'blacklist.png'
achievement = 'achievement.png'
cancel = 'cancel.png'

# Define the action to perform when the image is found
action = 'click'
click_coords = (100, 200)  # Coordinates for mouse click

state = 0

while True:        
    if state == 0:
        # take a screenshot
        pyautogui.screenshot('screenshot.png')
        
        # check for ok button
        image = pyautogui.locateOnScreen(ok)
        if image is not None:
            print('ok')
            if action == 'click':
                image_center_x, image_center_y = pyautogui.center(image)
                pyautogui.click(image_center_x, image_center_y)

        # check for ok1 button
        image = pyautogui.locateOnScreen(ok1)
        if image is not None:
            print('ok1')
            if action == 'click':
                image_center_x, image_center_y = pyautogui.center(image)
                pyautogui.click(image_center_x, image_center_y)

        # check for ok2 button
        image = pyautogui.locateOnScreen(ok2)
        if image is not None:
            print('ok2')
            if action == 'click':
                image_center_x, image_center_y = pyautogui.center(image)
                pyautogui.click(image_center_x, image_center_y)

        # check for mpOK button
        image = pyautogui.locateOnScreen(mpOK)
        if image is not None:
            print('mpOK')
            if action == 'click':
                image_center_x, image_center_y = pyautogui.center(image)
                pyautogui.click(image_center_x, image_center_y)

        # check for achievement
        image = pyautogui.locateOnScreen(achievement)
        if image is not None:
            print('achievement')
            if action == 'click':
                image_center_x, image_center_y = pyautogui.center(image)
                pyautogui.click(image_center_x, image_center_y)
        
        # Search for the image on the screen
        image = pyautogui.locateOnScreen(invite)
        if image is not None:
            print('confirm')
            if action == 'click':
                # Get the center coordinates of the image
                image_center_x, image_center_y = pyautogui.center(image)
                # Perform the click action on the center coordinates
                pyautogui.click(image_center_x, image_center_y)
                state = 1
                print('enter state 1')

    if state == 1:
        print('state 1')
        # take a screenshot
        pyautogui.screenshot('screenshot.png')
        # check chose black list
        image = pyautogui.locateOnScreen(blacklist)
        if image is not None:
            print('black list')
            if action == 'click':
                image_center_x, image_center_y = pyautogui.center(image)
                pyautogui.click(image_center_x, image_center_y)
                state = 2
                print('enter state 2')


    if state == 2:
        print('state 2')
        # take a screenshot
        pyautogui.screenshot('screenshot.png')
        # check for join button
        image = pyautogui.locateOnScreen(join)
        if image is not None:
            print('join')
            if action == 'click':
                image_center_x, image_center_y = pyautogui.center(image)
                pyautogui.click(image_center_x, image_center_y)
                state = 0
                print('enter state 3')
        
        # check for ready button
        image = pyautogui.locateOnScreen(ready)
        if image is not None:
            print('ready')
            if action == 'click':
                image_center_x, image_center_y = pyautogui.center(image)
                pyautogui.click(image_center_x, image_center_y)
                state = 0
                print('enter state 3')
        
        # check for cancel button
        image = pyautogui.locateOnScreen(cancel)
        if image is not None:
            print('cancel')
            if action == 'click':
                image_center_x, image_center_y = pyautogui.center(image)
                pyautogui.click(image_center_x, image_center_y)
                state = 0
                print('enter state 3')
        
        else:
            state = 2

