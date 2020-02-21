
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def symbol(self):

        # Cross
        self.symbolAX = QLabel(self)
        self.symbolAX.setScaledContents(True)
        self.symbolAX.setPixmap(QPixmap("./symbols/cross.png"))
        self.symbolAX.resize(120*self.resMult, 120*self.resMult)
        self.symbolAX.move(60*self.resMult, 50*self.resMult)
        self.symbolAX.hide()

        self.symbolBX = QLabel(self)
        self.symbolBX.setScaledContents(True)
        self.symbolBX.setPixmap(QPixmap("./symbols/cross.png"))
        self.symbolBX.resize(120*self.resMult, 120*self.resMult)
        self.symbolBX.move(245*self.resMult, 50*self.resMult)
        self.symbolBX.hide()
        
        self.symbolCX = QLabel(self)
        self.symbolCX.setScaledContents(True)
        self.symbolCX.setPixmap(QPixmap("./symbols/cross.png"))
        self.symbolCX.resize(120*self.resMult, 120*self.resMult)
        self.symbolCX.move(425*self.resMult, 50*self.resMult)
        self.symbolCX.hide()
        
        self.symbolDX = QLabel(self)
        self.symbolDX.setScaledContents(True)
        self.symbolDX.setPixmap(QPixmap("./symbols/cross.png"))
        self.symbolDX.resize(120*self.resMult, 120*self.resMult)
        self.symbolDX.move(60*self.resMult, 195*self.resMult)
        self.symbolDX.hide()
        
        self.symbolEX = QLabel(self)
        self.symbolEX.setScaledContents(True)
        self.symbolEX.setPixmap(QPixmap("./symbols/cross.png"))
        self.symbolEX.resize(120*self.resMult, 120*self.resMult)
        self.symbolEX.move(245*self.resMult, 195*self.resMult)
        self.symbolEX.hide()
        
        self.symbolFX = QLabel(self)
        self.symbolFX.setScaledContents(True)
        self.symbolFX.setPixmap(QPixmap("./symbols/cross.png"))
        self.symbolFX.resize(120*self.resMult, 120*self.resMult)
        self.symbolFX.move(425*self.resMult, 195*self.resMult)
        self.symbolFX.hide()
        
        self.symbolGX = QLabel(self)
        self.symbolGX.setScaledContents(True)
        self.symbolGX.setPixmap(QPixmap("./symbols/cross.png"))
        self.symbolGX.resize(120*self.resMult, 120*self.resMult)
        self.symbolGX.move(60*self.resMult, 340*self.resMult)
        self.symbolGX.hide()
        
        self.symbolHX = QLabel(self)
        self.symbolHX.setScaledContents(True)
        self.symbolHX.setPixmap(QPixmap("./symbols/cross.png"))
        self.symbolHX.resize(120*self.resMult, 120*self.resMult)
        self.symbolHX.move(245*self.resMult, 340*self.resMult)
        self.symbolHX.hide()
        
        self.symbolIX = QLabel(self)
        self.symbolIX.setScaledContents(True)
        self.symbolIX.setPixmap(QPixmap("./symbols/cross.png"))
        self.symbolIX.resize(120*self.resMult, 120*self.resMult)
        self.symbolIX.move(425*self.resMult, 340*self.resMult)
        self.symbolIX.hide()
        
        # Circle
        self.symbolAO = QLabel(self)
        self.symbolAO.setScaledContents(True)
        self.symbolAO.setPixmap(QPixmap("./symbols/circle.png"))
        self.symbolAO.resize(120*self.resMult, 120*self.resMult)
        self.symbolAO.move(60*self.resMult, 50*self.resMult)
        self.symbolAO.hide()

        self.symbolBO = QLabel(self)
        self.symbolBO.setScaledContents(True)
        self.symbolBO.setPixmap(QPixmap("./symbols/circle.png"))
        self.symbolBO.resize(120*self.resMult, 120*self.resMult)
        self.symbolBO.move(245*self.resMult, 50*self.resMult)
        self.symbolBO.hide()
                    
        self.symbolCO = QLabel(self)
        self.symbolCO.setScaledContents(True)
        self.symbolCO.setPixmap(QPixmap("./symbols/circle.png"))
        self.symbolCO.resize(120*self.resMult, 120*self.resMult)
        self.symbolCO.move(425*self.resMult, 50*self.resMult)
        self.symbolCO.hide()
                    
        self.symbolDO = QLabel(self)
        self.symbolDO.setScaledContents(True)
        self.symbolDO.setPixmap(QPixmap("./symbols/circle.png"))
        self.symbolDO.resize(120*self.resMult, 120*self.resMult)
        self.symbolDO.move(60*self.resMult, 195*self.resMult)
        self.symbolDO.hide()
                    
        self.symbolEO = QLabel(self)
        self.symbolEO.setScaledContents(True)
        self.symbolEO.setPixmap(QPixmap("./symbols/circle.png"))
        self.symbolEO.resize(120*self.resMult, 120*self.resMult)
        self.symbolEO.move(245*self.resMult, 195*self.resMult)
        self.symbolEO.hide()
                    
        self.symbolFO = QLabel(self)
        self.symbolFO.setScaledContents(True)
        self.symbolFO.setPixmap(QPixmap("./symbols/circle.png"))
        self.symbolFO.resize(120*self.resMult, 120*self.resMult)
        self.symbolFO.move(425*self.resMult, 195*self.resMult)
        self.symbolFO.hide()
                    
        self.symbolGO = QLabel(self)
        self.symbolGO.setScaledContents(True)
        self.symbolGO.setPixmap(QPixmap("./symbols/circle.png"))
        self.symbolGO.resize(120*self.resMult, 120*self.resMult)
        self.symbolGO.move(60*self.resMult, 340*self.resMult)
        self.symbolGO.hide()
                    
        self.symbolHO = QLabel(self)
        self.symbolHO.setScaledContents(True)
        self.symbolHO.setPixmap(QPixmap("./symbols/circle.png"))
        self.symbolHO.resize(120*self.resMult, 120*self.resMult)
        self.symbolHO.move(245*self.resMult, 340*self.resMult)
        self.symbolHO.hide()
                    
        self.symbolIO = QLabel(self)
        self.symbolIO.setScaledContents(True)
        self.symbolIO.setPixmap(QPixmap("./symbols/circle.png"))
        self.symbolIO.resize(120*self.resMult, 120*self.resMult)
        self.symbolIO.move(425*self.resMult, 340*self.resMult)
        self.symbolIO.hide()
        
        
        
        