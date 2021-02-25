import sys
from main import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QLineEdit, QPushButton, QListWidget, QCheckBox


class App(QWidget):

    def __init__(self):
        super().__init__()
        
        self.title = "PoE-Helper"
        self.mods = {}
        self.left = 100
        self.top = 100
        self.width = 450
        self.height = 700
        self.listener = Listener(on_click=on_click)
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        #Range_Min_Textbox
        self.textbox_min = QLineEdit(self)
        self.textbox_min.move(20,60)
        self.textbox_min.resize(60,20)

        #Range_Max_Textbox
        self.textbox_max = QLineEdit(self)
        self.textbox_max.move(20,90)
        self.textbox_max.resize(60,20)

        #Mod_Textbox
        self.textbox_mod = QLineEdit(self)
        self.textbox_mod.move(20,120)
        self.textbox_mod.resize(280,40)

        #Modlist
        self.modlist = QListWidget(self)
        self.modlist.move(20,200)
        self.modlist.resize(280,300)

        #Save Button
        self.button = QPushButton('Save Mod', self)
        self.button.move(20,550)
        self.button.resize(280,50)
        self.button.clicked.connect(self.on_click)


        #Checkbox
        self.checkbox = QCheckBox("Activate Listener",self)
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.clickBox)
        self.checkbox.move(20,620)
        self.button.resize(280,50)

        self.show()

    def clickBox(self, state):
        
        if state == QtCore.Qt.Checked:
            self.listener = Listener(on_click=on_click)
            poe_listener(True, self.listener)
        else:
            poe_listener(False, self.listener)

    #@pyqtSlot
    def on_click(self):
        textbox_value_mod = self.textbox_mod.text()

        min_max = {min: self.textbox_min.text(), max: self.textbox_max.text()}

        self.modlist.addItem(min_max[min] +" - "+  min_max[max] +" : " + textbox_value_mod)
        self.mods[textbox_value_mod] = min_max

        self.textbox_min.setText("")
        self.textbox_max.setText("")
        self.textbox_mod.setText("")







if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())