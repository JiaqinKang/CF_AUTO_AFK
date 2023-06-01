import pyautogui
import time
from multiprocessing import Pool
import gc
import keyboard 

# Define the image filenames to search for
images_to_search = [ 
                    'blacklist.png',
                    'wrongpos.png', 'wrongpos2.png','confirm.png', 
                    'runaway.png','cancel2.png',
                    'join.png','ready.png', 'ok.png', 
                    'ok1.png', 'ok2.png', 'mpOK.png',  
                    'achievement.png',  'close.png', 
                    'close2.png','levelup.png','error.png'
                    ]

# Define the action to perform when the image is found
action = 'click'
click_coords = (100, 200)  # Coordinates for mouse click

pause = True  # Control variable

def find_and_click(image):
    # Search for the image on the screen
    loc = pyautogui.locateOnScreen(image, confidence=0.75)
    if loc is not None:
        print(f'{image} found')
        if action == 'click':
            
            # Get the center coordinates of the image
            center = pyautogui.center(loc)
            if image == 'blacklist.png':
                pyautogui.click(center)  # click
                pyautogui.click(center)  # twice
                time.sleep(1)
                
            # Check if the image is 'error.png'
            elif image == 'error.png':
                pyautogui.click(center)  # click once
                pyautogui.click(center)  # click once
                keyboard.press('esc')
                keyboard.release('esc')
                time.sleep(1)
                keyboard.press('enter')
                keyboard.release('enter')
                time.sleep(1)
                keyboard.press('enter')
                keyboard.release('enter')
                time.sleep(15)
                return
            
            else:
                # Perform the click action on the center coordinates
                pyautogui.click(center)  # click once
    gc.collect()

def start_detection(e):
    global pause
    pause = False
    print("Detection started")

def stop_detection(e):
    global pause
    pause = True
    print("Detection paused")

if __name__ == "__main__":
    # Register hotkeys
    keyboard.on_press_key("f10", start_detection)
    keyboard.on_press_key("f12", stop_detection)

    # Start the multiprocessing pool
    pool = Pool(processes=1)

    while True:
        if not pause:
            pool.map(find_and_click, images_to_search)
        time.sleep(0.1)  # This prevents your while loop from hogging all the CPU power
