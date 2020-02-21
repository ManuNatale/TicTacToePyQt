
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import globalVars

def checkWin(self):   

    # Check win X
    if(globalVars.caseInfo[0] == 'X' and globalVars.caseInfo[1] == 'X' and globalVars.caseInfo[2] == 'X'):
        self.statusbar.showMessage('PLAYER X WIN !')
        self.symbolHorizontallineTop.show()
        return True
    if(globalVars.caseInfo[3] == 'X' and globalVars.caseInfo[4] == 'X' and globalVars.caseInfo[5] == 'X'):
        self.statusbar.showMessage('PLAYER X WIN !')
        self.symbolHorizontallineMiddle.show()
        return True
    if(globalVars.caseInfo[6] == 'X' and globalVars.caseInfo[7] == 'X' and globalVars.caseInfo[8] == 'X'):
        self.statusbar.showMessage('PLAYER X WIN !')
        self.symbolHorizontallineBottom.show()
        return True
    if(globalVars.caseInfo[0] == 'X' and globalVars.caseInfo[3] == 'X' and globalVars.caseInfo[6] == 'X'):
        self.statusbar.showMessage('PLAYER X WIN !')
        self.symbolVertilineLeft.show()
        return True  
    if(globalVars.caseInfo[1] == 'X' and globalVars.caseInfo[4] == 'X' and globalVars.caseInfo[7] == 'X'):
        self.statusbar.showMessage('PLAYER X WIN !')
        self.symbolVertilineMiddle.show()
        return True
    if(globalVars.caseInfo[2] == 'X' and globalVars.caseInfo[5] == 'X' and globalVars.caseInfo[8] == 'X'):
        self.statusbar.showMessage('PLAYER X WIN !')
        self.symbolVertilineRight.show()
        return True    
    if(globalVars.caseInfo[0] == 'X' and globalVars.caseInfo[4] == 'X' and globalVars.caseInfo[8] == 'X'):
        self.statusbar.showMessage('PLAYER X WIN !')
        self.symbolDiaglineLeft.show()
        return True
    if(globalVars.caseInfo[2] == 'X' and globalVars.caseInfo[4] == 'X' and globalVars.caseInfo[6] == 'X'):
        self.statusbar.showMessage('PLAYER X WIN !')
        self.symbolDiaglineRight.show()
        return True
        
    # Check win O
    if(globalVars.caseInfo[0] == 'O' and globalVars.caseInfo[1] == 'O' and globalVars.caseInfo[2] == 'O'):
        self.statusbar.showMessage('PLAYER O WIN !')
        self.symbolHorizontallineTop.show()
        return True
    if(globalVars.caseInfo[3] == 'O' and globalVars.caseInfo[4] == 'O' and globalVars.caseInfo[5] == 'O'):
        self.statusbar.showMessage('PLAYER O WIN !')
        self.symbolHorizontallineMiddle.show()
        return True
    if(globalVars.caseInfo[6] == 'O' and globalVars.caseInfo[7] == 'O' and globalVars.caseInfo[8] == 'O'):
        self.statusbar.showMessage('PLAYER O WIN !')
        self.symbolHorizontallineBottom.show()
        return True
    if(globalVars.caseInfo[0] == 'O' and globalVars.caseInfo[3] == 'O' and globalVars.caseInfo[6] == 'O'):
        self.statusbar.showMessage('PLAYER O WIN !')
        self.symbolVertilineLeft.show()
        return True  
    if(globalVars.caseInfo[1] == 'O' and globalVars.caseInfo[4] == 'O' and globalVars.caseInfo[7] == 'O'):
        self.statusbar.showMessage('PLAYER O WIN !')
        self.symbolVertilineMiddle.show()
        return True
    if(globalVars.caseInfo[2] == 'O' and globalVars.caseInfo[5] == 'O' and globalVars.caseInfo[8] == 'O'):
        self.statusbar.showMessage('PLAYER O WIN !')
        self.symbolVertilineRight.show()
        return True    
    if(globalVars.caseInfo[0] == 'O' and globalVars.caseInfo[4] == 'O' and globalVars.caseInfo[8] == 'O'):
        self.statusbar.showMessage('PLAYER O WIN !')
        self.symbolDiaglineLeft.show()
        return True
    if(globalVars.caseInfo[2] == 'O' and globalVars.caseInfo[4] == 'O' and globalVars.caseInfo[6] == 'O'):
        self.statusbar.showMessage('PLAYER O WIN !')
        self.symbolDiaglineRight.show()
        return True
        
    # draw
    if(globalVars.caseInfo[0] != '' and globalVars.caseInfo[1] != '' and globalVars.caseInfo[2] != '' and
        globalVars.caseInfo[3] != '' and globalVars.caseInfo[4] != '' and globalVars.caseInfo[5] != '' and
        globalVars.caseInfo[6] != '' and globalVars.caseInfo[7] != '' and globalVars.caseInfo[8] != ''):
        self.statusbar.showMessage('Match ended in a draw')
        return True
    
    
    
    
    