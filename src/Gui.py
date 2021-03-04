import sys
import model
from itertools import islice
from model import *
from pynput.mouse import Listener
from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton,QComboBox, QLabel,QApplication, QWidget, QAction, QLineEdit, QPushButton, QListWidget, QCheckBox


class App(QWidget):

    def __init__(self):
        super().__init__()
        
        self.title = "PoE-Helper"
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 410
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
        self.textbox_min.move(100,15)
        self.textbox_min.resize(60,20)

        #Label_Mod
        self.label_mod = QLabel(self)
        self.label_mod.setText("Desired Mod")
        self.label_mod.move(20,50)    

        #Textbox_Mod
        self.textbox_mod = QLineEdit(self)
        self.textbox_mod.move(20,70)
        self.textbox_mod.resize(280,20)

        #Label_Modlist
        self.label_modlist = QLabel(self)
        self.label_modlist.setText("Modlist")
        self.label_modlist.move(20,110)  

        #Textbox_Modlist
        self.modlist = QListWidget(self)
        self.modlist.move(20,130)
        self.modlist.resize(280,150)

        #Save Button
        self.button = QPushButton('Save Mod', self)
        self.button.move(20,300)
        self.button.resize(70,50)
        self.button.setStyleSheet("background-color : rgba(0, 255, 0, 50%)") 
        self.button.clicked.connect(self.on_click_save)

        #Delete Button
        self.button_del = QPushButton('Delete Mod', self)
        self.button_del.move(230,300)
        self.button_del.resize(70,50)
        self.button_del.setStyleSheet("background-color : rgba(255, 0, 0, 50%)") 
        self.button_del.clicked.connect(self.on_click_del)

        self.textbox_min.setText("50")
        self.textbox_mod.setText("to maximum Life")

        #Listener Pushbutton
        self.pushbutton = QPushButton("Activate Listener",self)
        self.pushbutton.setGeometry(200, 150, 100, 40)
        self.pushbutton.setCheckable(True)
        self.pushbutton.clicked.connect(self.changeState)
        self.pushbutton.setStyleSheet("background-color : lightgrey") 
        self.pushbutton.move(110,350)

        self.update()
        self.show()
    
    def changeState(self):

        if self.pushbutton.isChecked():
            self.pushbutton.setStyleSheet("background-color : lightblue") 
            self.listener = Listener(on_click=Model.on_click)
            Model.poe_listener(True, self.listener)
        else:
            self.pushbutton.setStyleSheet("background-color : lightgrey")
            Model.poe_listener(False, self.listener)


    def selectionchange(self,i):
        model.item_depth = i + 1
    
    def on_click_del(self):

        row = self.modlist.currentRow()
        print(row)
        if row != -1:
            self.modlist.takeItem(row)
            del model.requirements[next(islice(model.requirements,row,None))]
        else:
            pass

    def on_click_save(self):
        if self.textbox_mod.text() and self.textbox_min.text():
            textbox_value_mod = self.textbox_mod.text()
            minimum = {"minimum": float(self.textbox_min.text())}

            self.modlist.addItem(str(minimum["minimum"]) +" : " + textbox_value_mod)
            model.requirements[textbox_value_mod] = minimum
            self.textbox_min.setText("")
            self.textbox_mod.setText("")

        elif self.textbox_mod.text() and not self.textbox_min.text():
            textbox_value_mod = self.textbox_mod.text()

            self.modlist.addItem(textbox_value_mod + " (raw)")
            model.requirements[textbox_value_mod] = None
            self.textbox_min.setText("")
            self.textbox_mod.setText("")
        else:
            pass
