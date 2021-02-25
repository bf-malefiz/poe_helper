import sys
import model
from itertools import islice
from model import *
from pynput.mouse import Listener
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QLineEdit, QPushButton, QListWidget, QCheckBox


class App(QWidget):

    def __init__(self):
        super().__init__()
        
        self.title = "PoE-Helper"
        self.left = 100
        self.top = 100
        self.width = 450
        self.height = 700
        self.listener = Listener(on_click=Model.on_click)
        self.model = Model()
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
        self.button.resize(70,50)
        self.button.clicked.connect(self.on_click)

        #Delete Button
        self.button_del = QPushButton('Delete Mod', self)
        self.button_del.move(160,550)
        self.button_del.resize(70,50)
        self.button_del.clicked.connect(self.on_click_del)

        self.textbox_min.setText("1")
        self.textbox_max.setText("10")
        self.textbox_mod.setText("to maximum Life")

        #Checkbox
        self.checkbox = QCheckBox("Activate Listener",self)
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.clickBox)
        self.checkbox.move(20,620)

        self.show()

    def clickBox(self, state):
        
        if state == QtCore.Qt.Checked:
            self.listener = Listener(on_click=Model.on_click)
            Model.poe_listener(True, self.listener)
        else:
            Model.poe_listener(False, self.listener)
    
    
    def on_click_del(self):
        row = self.modlist.currentRow()
        self.modlist.takeItem(row)
        del model.requirements[next(islice(model.requirements,row,None))]
        print(model.requirements)

    def on_click(self):

        textbox_value_mod = self.textbox_mod.text()
        min_max = {"minimum": float(self.textbox_min.text()), "maximum": float(self.textbox_max.text())}

        self.modlist.addItem(str(min_max["minimum"]) +" - "+  str(min_max["maximum"]) +" : " + textbox_value_mod)
        model.requirements[textbox_value_mod] = min_max
        self.textbox_min.setText("")
        self.textbox_max.setText("")
        self.textbox_mod.setText("")
