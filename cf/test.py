import ctypes
import keyboard


def run_test():
    # use window api to move the mouse up 10 pixels
    ctypes.windll.user32.mouse_event(0x0001, 0, -10, 0, 0)
    # use window api to move the mouse down 10 pixels
    
# Callback function for F10 key press
def on_key_press(event):
    if event.name == 'f10':
        print('f10 pressed')
        run_test()

# Register the callback function for key press events
keyboard.on_press(on_key_press)

# Keep the script running until interrupted
keyboard.wait('esc')
