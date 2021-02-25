import sys
import pyperclip
import Gui
from item_data import item_data
#from pynput import keyboard
#from pynput.mouse import Listener
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController
from PyQt5.QtWidgets import QMessageBox
import winsound

keyboard = KeyboardController()
mouse = MouseController()
requirements = {}

class Model():
   
    def __init__(self):
        self.item_enum = 6

    def poe_listener(active, listener):
        if active:
            listener.start()
        else:
            listener.stop()
    
    def block_input():
        print("block")
        mouse.move(200,200)
        

    def test_mod_values(mod_dict, values):
        if mod_dict["minimum"] <= values:
            Model.block_input()
            winsound.Beep(440, 1000)
        else:
            pass

 

    def on_click(x, y, button, pressed):
        if pressed:
            pyperclip.copy("")
            keyboard.press(Key.ctrl)
            keyboard.press("c")
            keyboard.release("c")
            keyboard.release(Key.ctrl)
        else:
            try:
                data = item_data()
                data.process_item_data()
                for i in data.mods:
                    tmp_mod = " ".join(i)
                    if tmp_mod in requirements:
                        Model.test_mod_values(requirements[tmp_mod], data.values[int(list(requirements.keys()).index(tmp_mod))][0])

            except IndexError: # thrown by empty/none poe clipboards not satiesfied requirements
                print("Error")









