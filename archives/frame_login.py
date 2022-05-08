import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QPushButton, QLineEdit, QLabel, QMainWindow, QApplication, QFrame

class FrameLogin():
    def frame_login(self):
        self.login_frame = QFrame(self)
        self.login_frame.setGeometry(0, 0, 1080, 720)
        self.login_frame.setStyleSheet(
            '''
                QFrame{
                    background-image: url(../images/secondPageImages/bg2.jpg);
                    font-size: 15px;
                    color: white;
                    font: bold 'Gotham';
                }
            '''
        )
        self.login_frame.show()
        
        self.login_frame_labels()
        self.login_frame_entrys()
        self.login_frame_buttons()

    def login_frame_labels(self):
        self.logo_frame_login = QLabel(self.login_frame)
        self.logo_frame_login.setGeometry(15, 15, 200, 50)
        self.logo_frame_login.setStyleSheet(
            '''
                QLabel{
                    background-image: url(../images/secondPageImages/logo2.png);
                    background-repeat: no-repeat;
                }
            '''
        )
        self.logo_frame_login.show()

        self.white_logo_frame_login = QLabel(self.login_frame)
        self.white_logo_frame_login.setGeometry(20, 250, 200, 200)
        self.white_logo_frame_login.setStyleSheet(
            '''
                QLabel{
                    background-image: url(../images/secondPageImages/whitelogo2.png);
                    background-repeat: no-repeat;
                }
            '''
        )
        self.white_logo_frame_login.show()

        self.title = QLabel('L O G I N', self.login_frame)
        self.title.setGeometry(350, 200, 150, 50)
        self.title.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    font: bold 'Gotham';
                    font-size: 30px;
                }
            '''
        )

    def login_frame_entrys(self):
        self.email_login = QLineEdit(self.login_frame)
        self.email_login.setGeometry(250, 290, 330, 50)
        self.email_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.email_login.setMaxLength(100)
        self.email_login.setPlaceholderText('E-mail')
        self.email_login.setStyleSheet(
            '''
                QLineEdit{
                    background: rgba(0, 0, 0, 0);
                    color: #808080;
                    font-size: 18px;
                    border-radius: 25px;
                    border-width: 2px;
                    border-style: solid;
                    border-color: #03d3e0;
                }
                QLineEdit:pressed{
                    color: #ffffff;
                }
            '''
        )
        self.email_login.show()

        self.password_login = QLineEdit(self.login_frame)
        self.password_login.setGeometry(250, 360, 330, 50)
        self.password_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_login.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_login.setMaxLength(8)
        self.password_login.setPlaceholderText('Senha')
        self.password_login.setStyleSheet(
            '''
                QLineEdit{
                    background: rgba(0, 0, 0, 0);
                    color: #808080;
                    font-size: 18px;
                    border-radius: 25px;
                    border-width: 2px;
                    border-style: solid;
                    border-color: #03d3e0;
                }
                QLineEdit:pressed{
                    color: #ffffff;
                }
            '''
        )
        self.password_login.show()

    def login_frame_buttons(self):
        self.about_us = QPushButton(self.frame_login)
        self.about_us.setText('SOBRE NÓS')
        self.about_us.setGeometry(15, 600, 100, 100)
        self.about_us.setStyleSheet(
            '''
                QPushButton{
                    background: none;
                    border-radius: 2px;
                    color: #ffffff;
                }
        ''')
        self.about_us.show()

class Window(QMainWindow, FrameLogin):
    def __init__(self):
        super(Window, self).__init__()
        self.window_definitions()
        self.frame_login()

    def window_definitions(self):
        self.setWindowTitle('Oficina do Corpo em Movimento')
        self.resize(1080, 720)

if __name__ == '__main__':
    main_window = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(main_window.exec())
