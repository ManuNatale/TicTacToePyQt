
import sys
import globalVars
import buttons
import symbols
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from tictactoeCore import *

class mWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()      

        
    def initUI(self):      

        screen_resolution = app.desktop().screenGeometry()
        self.screen_width= screen_resolution.width()
        self.screen_height = screen_resolution.height()
        print('Screen resolution = {}x{}'.format(self.screen_width, self.screen_height))
        
        # Resolution multiplicator
        if(self.screen_width == 3840 and self.screen_height == 2160):
            self.resMult = 2
        else:
            self.resMult = 1
    
        self.col = QColor(0, 0, 0) 

        # Init layout
        self.grid()
        buttons.button(self)
        symbols.symbol(self)
        self.winLine()
        
###########################################################################       
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        self.statusbar.showMessage('Player X begin')
        
        menubar = self.menuBar()       
        viewMenu = menubar.addMenu('View')       
        resetMenu = menubar.addMenu('Play again')
        
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        
        resetAct = QAction('Play Again', self)
        resetAct.setStatusTip('Play an other game')
        resetAct.triggered.connect(self.playAgain)
        resetAct.setShortcut('R')
        
        viewMenu.addAction(viewStatAct)
        resetMenu.addAction(resetAct)
        
        
###########################################################################        
        self.setGeometry(300*self.resMult, 300*self.resMult, 600*self.resMult, 500*self.resMult)
        self.setWindowTitle('Tic Tac Toe')
        self.show()
    
    def grid(self):
        self.lineA = QFrame(self)
        self.lineA.setGeometry(200*self.resMult, 50*self.resMult, 9*self.resMult, 400*self.resMult)
        self.lineA.setStyleSheet("QWidget { background-color: black }")
        
        self.lineB = QFrame(self)
        self.lineB.setGeometry(400*self.resMult, 50*self.resMult, 9*self.resMult, 400*self.resMult)
        self.lineB.setStyleSheet("QWidget { background-color: black }")
        
        self.lineC = QFrame(self)
        self.lineC.setGeometry(50*self.resMult, 175*self.resMult, 500*self.resMult, 9*self.resMult)
        self.lineC.setStyleSheet("QWidget { background-color: black }")
        
        self.lineD = QFrame(self)
        self.lineD.setGeometry(50*self.resMult, 325*self.resMult, 500*self.resMult, 9*self.resMult)
        self.lineD.setStyleSheet("QWidget { background-color: black }")
        
    def winLine(self):
        self.symbolDiaglineLeft = QLabel(self)
        self.symbolDiaglineLeft.setScaledContents(True)
        self.symbolDiaglineLeft.setPixmap(QPixmap("./symbols/diagonalline.png"))
        self.symbolDiaglineLeft.resize(410*self.resMult, 310*self.resMult)
        self.symbolDiaglineLeft.move(90*self.resMult, 95*self.resMult)
        self.symbolDiaglineLeft.hide()
        
        self.symbolDiaglineRight = QLabel(self)
        self.symbolDiaglineRight.setScaledContents(True)
        self.symbolDiaglineRight.setPixmap(QPixmap("./symbols/diagonalline2.png"))
        self.symbolDiaglineRight.resize(410*self.resMult, 310*self.resMult)
        self.symbolDiaglineRight.move(95*self.resMult, 100*self.resMult)
        self.symbolDiaglineRight.hide()
        
        self.symbolVertilineMiddle = QLabel(self)
        self.symbolVertilineMiddle.setScaledContents(True)
        self.symbolVertilineMiddle.setPixmap(QPixmap("./symbols/verticalline.png"))
        self.symbolVertilineMiddle.resize(480*self.resMult, 410*self.resMult)
        self.symbolVertilineMiddle.move(65*self.resMult, 50*self.resMult)
        self.symbolVertilineMiddle.hide()
        
        self.symbolVertilineLeft = QLabel(self)
        self.symbolVertilineLeft.setScaledContents(True)
        self.symbolVertilineLeft.setPixmap(QPixmap("./symbols/verticalline.png"))
        self.symbolVertilineLeft.resize(480*self.resMult, 410*self.resMult)
        self.symbolVertilineLeft.move(-121*self.resMult, 50*self.resMult)
        self.symbolVertilineLeft.hide()
        
        self.symbolVertilineRight = QLabel(self)
        self.symbolVertilineRight.setScaledContents(True)
        self.symbolVertilineRight.setPixmap(QPixmap("./symbols/verticalline.png"))
        self.symbolVertilineRight.resize(480*self.resMult, 410*self.resMult)
        self.symbolVertilineRight.move(245*self.resMult, 50*self.resMult)
        self.symbolVertilineRight.hide()
        
        self.symbolHorizontallineTop = QLabel(self)
        self.symbolHorizontallineTop.setScaledContents(True)
        self.symbolHorizontallineTop.setPixmap(QPixmap("./symbols/horizontalline.png"))
        self.symbolHorizontallineTop.resize(480*self.resMult, 130*self.resMult)
        self.symbolHorizontallineTop.move(60*self.resMult, 45*self.resMult)
        self.symbolHorizontallineTop.hide()
        
        self.symbolHorizontallineMiddle = QLabel(self)
        self.symbolHorizontallineMiddle.setScaledContents(True)
        self.symbolHorizontallineMiddle.setPixmap(QPixmap("./symbols/horizontalline.png"))
        self.symbolHorizontallineMiddle.resize(480*self.resMult, 130*self.resMult)
        self.symbolHorizontallineMiddle.move(60*self.resMult, 190*self.resMult)
        self.symbolHorizontallineMiddle.hide()
        
        self.symbolHorizontallineBottom = QLabel(self)
        self.symbolHorizontallineBottom.setScaledContents(True)
        self.symbolHorizontallineBottom.setPixmap(QPixmap("./symbols/horizontalline.png"))
        self.symbolHorizontallineBottom.resize(480*self.resMult, 130*self.resMult)
        self.symbolHorizontallineBottom.move(60*self.resMult, 330*self.resMult)
        self.symbolHorizontallineBottom.hide()
        
    def playAgain(self, state):
        print('reset')
        reset(self)
    
    def toggleMenu(self, state):
        
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
           
    def buttonInput(self, pressed):
    
        source = self.sender()

        # X turn
        if globalVars.playerXTurn == True:
            if source.text() == 'A' and globalVars.caseInfo[0] == '':
                globalVars.playerOTurn = True
                xTurn(self, source.text())
                globalVars.playerXTurn = False
            if source.text() == 'B' and globalVars.caseInfo[1] == '':
                globalVars.playerOTurn = True
                xTurn(self, source.text())
                globalVars.playerXTurn = False
            if source.text() == 'C' and globalVars.caseInfo[2] == '':
                globalVars.playerOTurn = True
                xTurn(self, source.text())
                globalVars.playerXTurn = False
            if source.text() == 'D' and globalVars.caseInfo[3] == '':
                globalVars.playerOTurn = True
                xTurn(self, source.text())
                globalVars.playerXTurn = False
            if source.text() == 'E' and globalVars.caseInfo[4] == '':
                globalVars.playerOTurn = True
                xTurn(self, source.text())
                globalVars.playerXTurn = False
            if source.text() == 'F' and globalVars.caseInfo[5] == '':
                globalVars.playerOTurn = True
                xTurn(self, source.text())
                globalVars.playerXTurn = False
            if source.text() == 'G' and globalVars.caseInfo[6] == '':
                globalVars.playerOTurn = True
                xTurn(self, source.text())
                globalVars.playerXTurn = False
            if source.text() == 'H' and globalVars.caseInfo[7] == '':
                globalVars.playerOTurn = True
                xTurn(self, source.text())
                globalVars.playerXTurn = False
            if source.text() == 'I' and globalVars.caseInfo[8] == '':
                globalVars.playerOTurn = True
                xTurn(self, source.text())
                globalVars.playerXTurn = False
        
        # O turn
        if globalVars.playerOTurn == True:
            if source.text() == 'A' and globalVars.caseInfo[0] == '':
                globalVars.playerXTurn = True
                oTurn(self, source.text())
                globalVars.playerOTurn = False
            if source.text() == 'B' and globalVars.caseInfo[1] == '':
                globalVars.playerXTurn = True
                oTurn(self, source.text())
                globalVars.playerOTurn = False
            if source.text() == 'C' and globalVars.caseInfo[2] == '':
                globalVars.playerXTurn = True
                oTurn(self, source.text())
                globalVars.playerOTurn = False
            if source.text() == 'D' and globalVars.caseInfo[3] == '':
                globalVars.playerXTurn = True
                oTurn(self, source.text())
                globalVars.playerOTurn = False 
            if source.text() == 'E' and globalVars.caseInfo[4] == '':
                globalVars.playerXTurn = True
                oTurn(self, source.text())
                globalVars.playerOTurn = False
            if source.text() == 'F' and globalVars.caseInfo[5] == '':
                globalVars.playerXTurn = True
                oTurn(self, source.text())
                globalVars.playerOTurn = False 
            if source.text() == 'G' and globalVars.caseInfo[6] == '':
                globalVars.playerXTurn = True
                oTurn(self, source.text())
                globalVars.playerOTurn = False
            if source.text() == 'H' and globalVars.caseInfo[7] == '':
                globalVars.playerXTurn = True
                oTurn(self, source.text())
                globalVars.playerOTurn = False 
            if source.text() == 'I' and globalVars.caseInfo[8] == '':
                globalVars.playerXTurn = True
                oTurn(self, source.text())
                globalVars.playerOTurn = False
                
        print('Player turn : X{} O{}'.format(globalVars.playerXTurn, globalVars.playerOTurn))        
        

# Global var Init
globalVars.globalVar()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    mW = mWindow()
    sys.exit(app.exec_())
