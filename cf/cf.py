import pyautogui
import time
from multiprocessing import Pool, cpu_count
import gc
import keyboard 

# Define the image filenames to search for
images_to_search = ['confirm.png', 'join.png', 'ready.png', 'ok.png', 'ok1.png', 'ok2.png', 
                    'mpOK.png', 'blacklist.png', 'achievement.png', 'cancel.png', 'close.png', 
                    'close2.png',]

# Define the action to perform when the image is found
action = 'click'
click_coords = (100, 200)  # Coordinates for mouse click

pause = True  # Control variable

def find_and_click(image):
    # Search for the image on the screen
    loc = pyautogui.locateOnScreen(image, confidence=0.8)
    if loc is not None:
        print(f'{image} found')
        if action == 'click':
            # Get the center coordinates of the image
            center = pyautogui.center(loc)
            # Perform the click action on the center coordinates
            pyautogui.click(center)
    else:
        print(f'{image} not found')
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

    # Using multiprocessing pool to parallelize the process
    pool = Pool(processes=cpu_count())

    while True:
        if not pause:
            pool.map(find_and_click, images_to_search)
        time.sleep(0.1)  # This prevents your while loop from hogging all the CPU power
