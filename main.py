import sys
import pyperclip
import Gui
from pynput.mouse import Listener
#pyperclip.copy('Hello, world!')

def get_item_clipboard():
    s = pyperclip.paste()
    s2 = s.split("--------")[1]
    s3 = s2.split("\r\n")[1:-1]
    s4 = [i.split("%") for i in s3]

    for count,value in enumerate(s4):
        s4[count][0] = int(s4[count][0])


def poe_listener(active, listener):
    if active:
        listener.start()
    else:
        listener.stop()

def on_click(x, y, button, pressed):
    if pressed:
        print ('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def block_input():
    pass

def highlight_screen():
    pass








def main():
    app = Gui.QApplication(sys.argv)
    ex = Gui.App()
    ex.show()

    sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()