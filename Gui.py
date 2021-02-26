import sys
import model
from itertools import islice
from model import *
from pynput.mouse import Listener
from PyQt5 import QtCore
from PyQt5.QtWidgets import QComboBox, QLabel,QApplication, QWidget, QAction, QLineEdit, QPushButton, QListWidget, QCheckBox


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

        #Label_Min
        self.label_min = QLabel(self)
        self.label_min.setText("Minimum")
        self.label_min.move(20,20)    

        #Textbox_Min
        self.textbox_min = QLineEdit(self)
        self.textbox_min.move(20,40)
        self.textbox_min.resize(60,20)

        #Label_Depth
        self.label_depth = QLabel(self)
        self.label_depth.setText("Depth")
        self.label_depth.move(20,80)    
        
        #Textbox_Depth
        self.comb_depth = QComboBox(self)
        self.comb_depth.addItems(["1","2","3","4","5","6","7"])
        self.comb_depth.currentIndexChanged.connect(self.selectionchange)
        self.comb_depth.move(20,100)
        self.comb_depth.resize(60,20)

        #Label_Mod
        self.label_mod = QLabel(self)
        self.label_mod.setText("Desired Mod")
        self.label_mod.move(20,140)    

        #Textbox_Mod
        self.textbox_mod = QLineEdit(self)
        self.textbox_mod.move(20,160)
        self.textbox_mod.resize(280,20)

        #Label_Modlist
        self.label_modlist = QLabel(self)
        self.label_modlist.setText("Modlist")
        self.label_modlist.move(20,200)  

        #Textbox_Modlist
        self.modlist = QListWidget(self)
        self.modlist.move(20,220)
        self.modlist.resize(280,300)

        #Save Button
        self.button = QPushButton('Save Mod', self)
        self.button.move(20,550)
        self.button.resize(70,50)
        self.button.clicked.connect(self.on_click_save)

        #Delete Button
        self.button_del = QPushButton('Delete Mod', self)
        self.button_del.move(160,550)
        self.button_del.resize(70,50)
        self.button_del.clicked.connect(self.on_click_del)

        self.textbox_min.setText("1")
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
    
    def selectionchange(self,i):
        model.item_depth = i + 1
    
    def on_click_del(self):
        row = self.modlist.currentRow()
        self.modlist.takeItem(row)
        del model.requirements[next(islice(model.requirements,row,None))]
        print(model.requirements)

    def on_click_save(self):
        if self.textbox_mod.text():
            textbox_value_mod = self.textbox_mod.text()
            minimum = {"minimum": float(self.textbox_min.text())}

            self.modlist.addItem(str(minimum["minimum"]) +" : " + textbox_value_mod)
            model.requirements[textbox_value_mod] = minimum
            self.textbox_min.setText("")
            self.textbox_mod.setText("")
        else:
            pass
