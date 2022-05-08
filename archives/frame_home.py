import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class FrameHome():
    pass

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.window_definitions()
        self.registerUserData()

    def window_definitions(self):
        self.setWindowTitle('Oficina do Corpo em Movimento')
        self.resize(1080, 720)

if __name__ == '__main__':
    main_window = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(main_window.exec_())
