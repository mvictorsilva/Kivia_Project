import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MainFrame(QWidget):
    def __init__(self):
        super().__init__()

        self.loadMainWindow()
        self.menuBar()
        self.mainFrame_one()

    def loadMainWindow (self):
        self.setWindowTitle('Oficina do Corpo em Movimento')
        self.resize(1200, 720)
        self.setMinimumSize(1080, 720)
        self.show()

    def menuBar(self):
        self.menuBarFrame = QFrame(self)
        self.menuBarFrame.setGeometry(0, 0, 1200, 720)
        self.menuBarFrame.setStyleSheet(
            '''
                QFrame{
                    background-color: qlineargradient(spread:pad, x1:0.484, y1:0, x2:0.521, y2:1, stop:0 rgba(0, 37, 42, 255), stop:1 rgba(0, 56, 62, 255));;
                }
            '''
        )
        self.menuBarFrame.show()

        self.logoImage = QLabel(self.menuBarFrame)
        self.logoImage.setStyleSheet(
            '''
                QLabel{
                    background-image: url(images/menuFrames/whitelogo2.png);
                    background-color: rgba(0, 0, 0, 0);
                    background-repeat: none;
                }
            '''
        )
        self.logoImage.setGeometry(0, 0, 268, 194)
        self.logoImage.show()
        
        self.buttonBegin = QPushButton(self.menuBarFrame)
        self.buttonBegin.setGeometry(0, 200, 100, 100)
        self.buttonBegin.setStyleSheet(
            '''
                QPushButton{
                    background-color: rgba(0, 0, 0, 0);
                    background-image: url(images/menuFrames/Inicio.png);
                    background-repeat: none;
                }
            '''
        )
        self.buttonBegin.show()

    def mainFrame_one(self):
        self.mainframe = QFrame(self.menuBarFrame)
        self.mainframe.setGeometry(250, 10, 940, 700)
        self.mainframe.setStyleSheet(
            '''
                QFrame{
                    border-radius: 30px;
                    background-color: #f7f7f7;
                }
            '''
        )
        self.mainframe.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainFrame()
    window.show()
    sys.exit(app.exec())
