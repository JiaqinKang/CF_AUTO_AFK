import threading
import keyboard
import time

# This variable will keep track of whether the scripts are paused
paused = True

def toggle_scripts_state():
    global paused
    paused = not paused

# Define the action that you want to take place
def type_s():
    keyboard.press('s')
    time.sleep(0.5)
    keyboard.release('s')
    keyboard.press('a')
    time.sleep(0.25)
    keyboard.release('a')

def run_cf_script():
    import pyautogui
    import time
    from multiprocessing import Pool
    import gc

    # Define the image filenames to search for
    images_to_search = [
        'blacklist.png',
        'confirm.png',
        'runaway.png',
        'cancel2.png',
        'join.png',
        'ready.png',
        'ok.png',
        'ok1.png',
        'ok2.png',
        'mpOK.png',
        'achievement.png',
        'close.png',
        'close2.png',
        'levelup.png',
        'error.png',
        'x.png',
    ]

    # Define the action to perform when the image is found
    action = 'click'

    def find_and_click(image):
        # Search for the image on the screen
        loc = pyautogui.locateOnScreen(image, confidence=0.725)
        if loc is not None:
            # print(f'{image} found')
            if action == 'click':
                # Get the center coordinates of the image
                center = pyautogui.center(loc)
                if image == 'blacklist.png':
                    pyautogui.click(center)  # click
                    pyautogui.click(center)  # twice
                    time.sleep(1)
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
        global paused
        paused = False
        print("Detection started")

    def stop_detection(e):
        global paused
        paused = True
        print("Detection paused")

    if __name__ == "__main__":
        # Register hotkeys
        keyboard.on_press_key("f10", start_detection)
        keyboard.on_press_key("f12", stop_detection)

        while True:
            if not paused:
                for image in images_to_search:
                    find_and_click(image)
            time.sleep(0.1)  # This prevents your while loop from hogging all the CPU power

def run_move_script():
    while True:
        if not paused:
            type_s()
        time.sleep(0.1)

# Create the threads
thread1 = threading.Thread(target=run_cf_script)
thread2 = threading.Thread(target=run_move_script)

# Register hotkeys to control both scripts together
keyboard.on_press_key('f10', lambda _: toggle_scripts_state())
keyboard.on_press_key('f12', lambda _: toggle_scripts_state())

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()