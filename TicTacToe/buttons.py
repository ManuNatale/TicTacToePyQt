
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def button(self):
        self.Abtn = QPushButton('A', self)
        self.Abtn.setStyleSheet("* { color: rgba(0, 0, 0, 0); background-color: rgba(0, 0, 0, 0); }")
        self.Abtn.setCheckable(True)
        self.Abtn.move(60*self.resMult, 60*self.resMult)
        self.Abtn.resize(120*self.resMult, 100*self.resMult)
        self.Abtn.clicked[bool].connect(self.buttonInput)

        self.Bbtn = QPushButton('B', self)
        self.Bbtn.setStyleSheet("* { color: rgba(0, 0, 0, 0); background-color: rgba(0, 0, 0, 0);}")
        self.Bbtn.setCheckable(True)
        self.Bbtn.move(245*self.resMult, 60*self.resMult)
        self.Bbtn.resize(120*self.resMult, 100*self.resMult)            
        self.Bbtn.clicked[bool].connect(self.buttonInput)

        self.Cbtn = QPushButton('C', self)
        self.Cbtn.setStyleSheet("* { color: rgba(0, 0, 0, 0); background-color: rgba(0, 0, 0, 0);}")
        self.Cbtn.setCheckable(True)
        self.Cbtn.move(425*self.resMult, 60*self.resMult)  
        self.Cbtn.resize(120*self.resMult, 100*self.resMult)          
        self.Cbtn.clicked[bool].connect(self.buttonInput)
        
        self.Dbtn = QPushButton('D', self)
        self.Dbtn.setStyleSheet("* { color: rgba(0, 0, 0, 0); background-color: rgba(0, 0, 0, 0);}")
        self.Dbtn.setCheckable(True)
        self.Dbtn.move(60*self.resMult, 205*self.resMult)  
        self.Dbtn.resize(120*self.resMult, 100*self.resMult)          
        self.Dbtn.clicked[bool].connect(self.buttonInput)
        
        self.Ebtn = QPushButton('E', self)
        self.Ebtn.setStyleSheet("* { color: rgba(0, 0, 0, 0); background-color: rgba(0, 0, 0, 0);}")
        self.Ebtn.setCheckable(True)
        self.Ebtn.move(245*self.resMult, 205*self.resMult)  
        self.Ebtn.resize(120*self.resMult, 100*self.resMult)          
        self.Ebtn.clicked[bool].connect(self.buttonInput)
        
        self.Fbtn = QPushButton('F', self)
        self.Fbtn.setStyleSheet("* { color: rgba(0, 0, 0, 0); background-color: rgba(0, 0, 0, 0);}")
        self.Fbtn.setCheckable(True)
        self.Fbtn.move(425*self.resMult, 205*self.resMult)  
        self.Fbtn.resize(120*self.resMult, 100*self.resMult)          
        self.Fbtn.clicked[bool].connect(self.buttonInput)
        
        self.Gbtn = QPushButton('G', self)
        self.Gbtn.setStyleSheet("* { color: rgba(0, 0, 0, 0); background-color: rgba(0, 0, 0, 0);}")
        self.Gbtn.setCheckable(True)
        self.Gbtn.move(60*self.resMult, 350*self.resMult)  
        self.Gbtn.resize(120*self.resMult, 100*self.resMult)          
        self.Gbtn.clicked[bool].connect(self.buttonInput)
        
        self.Hbtn = QPushButton('H', self)
        self.Hbtn.setStyleSheet("* { color: rgba(0, 0, 0, 0); background-color: rgba(0, 0, 0, 0);}")
        self.Hbtn.setCheckable(True)
        self.Hbtn.move(245*self.resMult, 350*self.resMult)  
        self.Hbtn.resize(120*self.resMult, 100*self.resMult)          
        self.Hbtn.clicked[bool].connect(self.buttonInput)
        
        self.Ibtn = QPushButton('I', self)
        self.Ibtn.setStyleSheet("* { color: rgba(0, 0, 0, 0); background-color: rgba(0, 0, 0, 0);}")
        self.Ibtn.setCheckable(True)
        self.Ibtn.move(425*self.resMult, 350*self.resMult)  
        self.Ibtn.resize(120*self.resMult, 100*self.resMult)          
        self.Ibtn.clicked[bool].connect(self.buttonInput)
        
        