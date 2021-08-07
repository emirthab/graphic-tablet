from pynput.keyboard import Key, Listener
import pyautogui

pressed = False

def on_release(key):
    print('{0} release'.format(
        key))
    if str(key) == "<63>":
        global pressed
        if pressed == False:
            pyautogui.mouseDown(button="left")
            pressed = True
        else:
            pyautogui.mouseUp(button="left")
            pressed = False
        
    if key == Key.esc:
        return False

with Listener(
    
        on_release=on_release) as listener:
    listener.join()