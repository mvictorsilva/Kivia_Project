import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.loadMainWindow()

    def loadMainWindow (self):
        self.setWindowTitle('Oficina do Corpo em Movimento')
        self.resize(1080, 720)
        self.setMinimumSize(1080, 720)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    