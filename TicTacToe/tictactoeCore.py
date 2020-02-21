
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from buttons import *
from symbols import *
from tictactoe import *
from globalVars import *
import globalVars
import checkWin

caseInfo = ['', '', '', '', '', '', '', '', '']

def reset(self):
    i = 0
    while(i < len(caseInfo)):
        globalVars.caseInfo[i] = ''
        i += 1
        
    self.symbolDiaglineLeft.hide()
    self.symbolDiaglineRight.hide()
    self.symbolVertilineMiddle.hide()
    self.symbolVertilineLeft.hide()
    self.symbolVertilineRight.hide()
    self.symbolHorizontallineTop.hide()
    self.symbolHorizontallineMiddle.hide()
    self.symbolHorizontallineBottom.hide()
        
    self.symbolAX.hide()
    self.symbolBX.hide()
    self.symbolCX.hide()
    self.symbolDX.hide()
    self.symbolEX.hide()
    self.symbolFX.hide()
    self.symbolGX.hide()
    self.symbolHX.hide()
    self.symbolIX.hide()
    
    self.symbolAO.hide()
    self.symbolBO.hide()
    self.symbolCO.hide()
    self.symbolDO.hide()
    self.symbolEO.hide()
    self.symbolFO.hide()
    self.symbolGO.hide()
    self.symbolHO.hide()
    self.symbolIO.hide()
    
    self.Abtn.setEnabled(True)
    self.Abtn.setCheckable(False)
    self.Bbtn.setEnabled(True)
    self.Bbtn.setCheckable(False)
    self.Cbtn.setEnabled(True)
    self.Cbtn.setCheckable(False)
    self.Dbtn.setEnabled(True)
    self.Dbtn.setCheckable(False)
    self.Ebtn.setEnabled(True)
    self.Ebtn.setCheckable(False)
    self.Fbtn.setEnabled(True)
    self.Fbtn.setCheckable(False)
    self.Gbtn.setEnabled(True)
    self.Gbtn.setCheckable(False)
    self.Hbtn.setEnabled(True)
    self.Hbtn.setCheckable(False)
    self.Ibtn.setEnabled(True)
    self.Ibtn.setCheckable(False)
    
    self.Abtn.show()
    self.Bbtn.show()
    self.Cbtn.show()
    self.Dbtn.show()
    self.Ebtn.show()
    self.Fbtn.show()
    self.Gbtn.show()
    self.Hbtn.show()
    self.Ibtn.show()
    
    globalVars.playerXTurn = True
    globalVars.playerOTurn = False
    
    

    
def xTurn(self,caseLocation):
    source = self.sender()

    if caseLocation == 'A':
        self.Abtn.hide()
        self.Abtn.setEnabled(False)
        globalVars.playerOTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[0] = 'X'
        self.symbolAX.show()
        
    if caseLocation == 'B':
        self.Bbtn.hide()
        globalVars.playerOTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[1] = 'X'
        self.symbolBX.show()
        
    if caseLocation == 'C':
        self.Cbtn.hide()
        globalVars.playerOTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[2] = 'X'
        self.symbolCX.show()
        
    if caseLocation == 'D':
        self.Dbtn.hide()
        globalVars.playerOTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[3] = 'X'
        self.symbolDX.show()
        
    if caseLocation == 'E':
        self.Ebtn.hide()
        globalVars.playerOTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[4] = 'X'
        self.symbolEX.show()
        
    if caseLocation == 'F':
        self.Fbtn.hide()
        globalVars.playerOTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[5] = 'X'
        self.symbolFX.show()
        
    if caseLocation == 'G':
        self.Gbtn.hide()
        globalVars.playerOTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[6] = 'X'
        self.symbolGX.show()
        
    if caseLocation == 'H':
        self.Hbtn.hide()
        globalVars.playerOTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[7] = 'X'
        self.symbolHX.show()
        
    if caseLocation == 'I':
        self.Ibtn.hide()
        globalVars.playerOTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[8] = 'X'
        self.symbolIX.show()
        
    globalVars.playerOTurn = True
    print(globalVars.caseInfo)
    if(checkWin.checkWin(self) == True):
        hideAll(self)
    else:
        self.statusbar.showMessage('Player O turn')
    
def oTurn(self,caseLocation):
    source = self.sender()

    if caseLocation == 'A':
        self.Abtn.hide()
        globalVars.playerXTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[0] = 'O'
        self.symbolAO.show()
        
    if caseLocation == 'B':
        self.Bbtn.hide()
        globalVars.playerXTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[1] = 'O'
        self.symbolBO.show()
        
    if caseLocation == 'C':
        self.Cbtn.hide()
        globalVars.playerXTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[2] = 'O'
        self.symbolCO.show()
        
    if caseLocation == 'D':
        self.Dbtn.hide()
        globalVars.playerXTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[3] = 'O'
        self.symbolDO.show()
        
    if caseLocation == 'E':
        self.Ebtn.hide()
        globalVars.playerXTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[4] = 'O'
        self.symbolEO.show()
        
    if caseLocation == 'F':
        self.Fbtn.hide()
        globalVars.playerXTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[5] = 'O'
        self.symbolFO.show()
        
    if caseLocation == 'G':
        self.Gbtn.hide()
        globalVars.playerXTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[6] = 'O'
        self.symbolGO.show()
        
    if caseLocation == 'H':
        self.Hbtn.hide()
        globalVars.playerXTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[7] = 'O'
        self.symbolHO.show()
        
    if caseLocation == 'I':
        self.Ibtn.hide()
        globalVars.playerXTurn = True
        self.statusbar.showMessage('Clicked : {}'.format(source.text()))
        globalVars.caseInfo[8] = 'O'
        self.symbolIO.show()
        
    globalVars.playerXTurn = True
    print(globalVars.caseInfo)
    if(checkWin.checkWin(self) == True):
        hideAll(self)
    else:
        self.statusbar.showMessage('Player X turn')

def hideAll(self):
    self.Abtn.hide()
    self.Bbtn.hide()
    self.Cbtn.hide()
    self.Dbtn.hide()
    self.Ebtn.hide()
    self.Fbtn.hide()
    self.Gbtn.hide()
    self.Hbtn.hide()
    self.Ibtn.hide()
        
        