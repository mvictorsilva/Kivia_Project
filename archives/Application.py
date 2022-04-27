###Imports window
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import QtGui
from PyQt6.QtGui import QIcon

###Import DataBase
import mysql.connector

###Import gerate code and send email verification
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random

class SendEmail():
    def gerate_number(self):
        self.code_verification = random.randrange(0, 9999)

    def frame_confirmation_email(self):
        self.frame_email = QFrame(self.cadastre_frame)
        self.cadastreFrame.move(0, 0)
        self.cadastreFrame.setGeometry(0, 0, 1080, 720)
        self.cadastreFrame.show()

    def send_mail(self):
        self.gerate_number()
        self.variables_cadastre()
        ###Varianble email

        try:
            self.email = self.emailEntry.text()


            self.msg = MIMEMultipart()
            self.message = (f'Olá {self.name}!\n\nSeu código de verificação é ' + f'{self.code_verification}.')

            self.password = 'steelseries'
            self.msg['From'] = 'testiktok111@gmail.com'
            self.msg['To'] = f'{self.email}'
            self.msg['Subject'] = 'Código de verifição Oficina Corpo e Movimento'

            self.msg.attach(MIMEText(self.message, 'plain'))
            self.server = smtplib.SMTP('smtp.gmail.com', port=587)
            self.server.starttls()
            self.server.login(self.msg['From'], self.password)
            self.server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
            self.server.quit()
        except:
            print('error')

class DataBase(SendEmail):
    def connect_db(self):
        self.connect = mysql.connector.connect(
            host = 'localhost',
            database = 'projeto_kivia_testes',
            user = 'root'
        )
        self.cursor = self.connect.cursor()

    def disconnect_db(self):
        self.connect.close()

    def variables_cadastre(self):
        self.name = self.nameEntry.text()
        self.surname = self.surnameEntry.text()
        self.email = self.emailEntry.text()
        self.password = self.passwordEntry.text()

    def variables_login(self):
        self.email_login = self.emailEntry_login.text()
        self.password_login = self.passwordEntry_login_frame.text()

    def clear_entrys_cadastre(self):
        self.nameEntry.clear()
        self.surnameEntry.clear()
        self.emailEntry.clear()
        self.passwordEntry.clear()

    def clear_entrys_login(self):
        self.emailEntry_login.clear()
        self.passwordEntry_login_frame.clear()

    def create_user(self):
        self.connect_db()
        self.variables_cadastre()

        if self.name == '':
            print('escreva alguma coisa')

        elif self.surname == '':
            print('escreva alguma coisa')

        elif self.email == '':
            print('escreva alguma coisa')

        elif self.password == '':
            print('escreva alguma coisa')

        else:

            self.cursor.execute("""
                insert into clientes(nome_cliente, sobrenome_cliente, email, senha)
                values(%s, %s, %s, %s)
            """,
            (
                self.name,
                self.surname,
                self.email,
                self.password
            ))

            self.send_mail()
            self.clear_entrys_cadastre()
            self.connect.commit()
        self.disconnect_db()

    def confirmation_user(self):
        self.connect_db()
        self.variables_login()

        if self.email_login == '':
            print('user and password incorrect')
            self.clear_entrys_login()
        elif self.password_login == '':
            print('user and password incorrect')
            self.clear_entrys_login()
        else:
        
            self.cursor.execute(f"""
                select senha from clientes where email = '{self.email_login}'
            """)
            self.passaword_db = self.cursor.fetchall()

            if self.password_login == self.passaword_db[0][0]:
                print('cadastro')
            else:
                print('no user')

            self.clear_entrys_login()
            self.connect.commit()
        self.disconnect_db()

class MainWindow(QWidget, DataBase):

    def __init__(self):
        super().__init__()

        self.cadastrePageFrame()

        ###################################
        #     Load The Cadastre Frame     #
        ###################################
        self.loadEveryThingInCadastreFrame()

        ###################################
        #      Load The Login Frame       #
        ###################################
        self.loadEveryThingInLoginFrame()

        ###################################
        #     Load The Wellcome Frame     #
        ###################################
        self.loadEveryThingInWellcomeFrame()

        ###################################
        # Load Main Window Configurations #
        ###################################

        self.loadMainWindow()

    def loadEveryThingInWellcomeFrame (self):

        ###################################
        #   Load Wellcome Frame Labels    #
        ###################################
        self.wellcomeFrameLabels()

        ###################################
        #   Load Wellcome Frame Buttons   #
        ###################################
        self.wellcomeFrameButtons()
    
    def loadEveryThingInLoginFrame (self):

        ###################################
        #     Load Login Frame Labels     #
        ###################################
        self.loginPageLabels()
        
        ###################################
        #     Load Login Frame Entrys     #
        ###################################
        self.loginPageEntrys()

        ###################################
        #     Load Login Frame Buttons    #
        ###################################
        self.loginPageButtons()

    def loadEveryThingInCadastreFrame (self):

        '''
        ###################################
        #    Load Cadastre Frame Entrys   #
        ###################################
        self.cadastrePageEntrys()
        '''

        ###################################
        #    Load Cadastre Frame Labels   #
        ###################################
        self.cadastrePageLabels()

        ###################################
        #    Load Cadastre Frame Buttons  #
        ###################################
        self.cadastrePageButtons()

    def wellcomePageFrame (self):

        ##############################
        # Main Window Wellcome Frame #
        ##############################
        self.wellcomeFrame = QFrame(self)
        self.wellcomeFrame.move(0, 0)
        self.wellcomeFrame.setGeometry(0, 0, 1080, 720)

    def loginPageFrame (self):

        ##############################
        #  Main Window Login Frame  #
        ##############################
        self.loginFrame = QFrame(self)
        self.loginFrame.move(0, 0)
        self.loginFrame.setGeometry(0, 0, 1080, 720)
        self.loginFrame.show()

    def cadastrePageFrame (self):

        ##############################
        # Main Window Cadastre Frame #
        ##############################
        self.cadastreFrame = QFrame(self)
        self.cadastreFrame.move(0, 0)
        self.cadastreFrame.setGeometry(0, 0, 1080, 720)
        self.cadastreFrame.show()

    #######################################################
    #                  First Page Things                  #
    #######################################################
    def wellcomeFrameLabels (self):
        
        ##############################
        # Loading The Wellcome Frame #
        ##############################
        self.wellcomePageFrame()

        ##############################
        #  Label For The Background  #
        ##############################
        self.backgroundLabel = QLabel(self.wellcomeFrame)
        self.backgroundLabel.setGeometry(0, 0, 1080, 720)
        self.backgroundLabel.setPixmap(QtGui.QPixmap('../images/firstPageImages/bg.png'))

        ##############################
        #  Label For The Green Logo  #
        ##############################
        self.logoLabel = QLabel(self.wellcomeFrame)
        self.logoLabel.setGeometry(20, 20, 200, 50)
        self.logoLabel.setStyleSheet('background: none;')
        self.logoLabel.setPixmap(QtGui.QPixmap('../images/firstPageImages/logo.png'))

        ##############################
        # Label For The Wellcome     #
        # Phrase                     #
        ##############################
        self.wellcomePhraseLabel = QLabel(self.wellcomeFrame)
        self.wellcomePhraseLabel.setText('BEM VINDO A OFICINA')
        self.wellcomePhraseLabel.setGeometry(200, 320, 700, 100)
        self.wellcomePhraseLabel.setStyleSheet('font-family: gotham; font-weight: bold; font-size: 55px; background: none; color: #00f0ff;')

        ##############################
        #  Label For The White Logo  #
        ##############################
        self.whiteLogoLabel = QLabel(self.wellcomeFrame)
        self.whiteLogoLabel.setGeometry(400, 420, 400, 70)
        self.whiteLogoLabel.setStyleSheet('background: none;')
        self.whiteLogoLabel.setPixmap(QtGui.QPixmap('../images/firstPageImages/whitelogo.png'))

    def wellcomeFrameButtons (self):

        ##############################
        #  Button For The About Us   #
        ##############################
        self.aboutUsButton = QPushButton(self.wellcomeFrame)
        self.aboutUsButton.setText('SOBRE NÓS')
        self.aboutUsButton.setGeometry(850, 10, 200, 50)
        self.aboutUsButton.setStyleSheet('background: none; border-radius: 5px; color: white; font-family: gotham;')

        ##############################
        #    Button For The Menu     #
        ##############################
        self.menuButton = QPushButton(self.wellcomeFrame)
        self.menuButton.setGeometry(1024, 7, 50, 50)
        self.menuButton.setStyleSheet('background: none; border-radius: 5px; background-image: url( ../images/firstPageImages/menu.png); background-repeat: none;')

        ##############################
        #  Button For The Next Page  #
        ##############################
        self.nextButton = QPushButton(self.wellcomeFrame)
        self.nextButton.setText('SIGN IN')
        self.nextButton.setGeometry(470, 520, 170, 50)
        self.nextButton.clicked.connect(self.loadLoginPage)
        self.nextButton.setStyleSheet('background-color: #12555c; border-radius: 12px; color: white; font: bold gotham; font-size: 17px;')

    def loadLoginPage (self):

        ##############################
        # Delete The Wellcome Frame  #
        ##############################
        self.wellcomeFrame.deleteLater()

    #######################################################
    #                 Second Page Things                  #
    #######################################################
    def loginPageLabels (self):

        self.loginPageFrame()

        ##############################
        #  Label For The Background  #
        ##############################
        self.backgroundLabel = QLabel(self.loginFrame)
        self.backgroundLabel.setGeometry(0, 0, 1080, 720)
        self.backgroundLabel.setPixmap(QtGui.QPixmap('../images/secondPageImages/bg2.jpg'))
        self.backgroundLabel.show()

        ##############################
        #  Label For The Green Logo  #
        ##############################
        self.logoLabel = QLabel(self.loginFrame)
        self.logoLabel.setGeometry(20, 20, 200, 50)
        self.logoLabel.setStyleSheet('background: none;')
        self.logoLabel.setPixmap(QtGui.QPixmap('../images/secondPageImages/logo2.png'))
        self.logoLabel.show()

        ##############################
        #  Label For The White Logo  #
        ##############################
        self.whiteLogoLabel = QLabel(self.loginFrame)
        self.whiteLogoLabel.setGeometry(50, 250, 400, 200)
        self.whiteLogoLabel.setStyleSheet('background: none;')
        self.whiteLogoLabel.setPixmap(QtGui.QPixmap('../images/secondPageImages/whitelogo2.png'))
        self.whiteLogoLabel.show()

        ##############################
        #   Label For Login Title    #
        ##############################
        self.loginTitleLabel = QLabel(self.loginFrame)
        self.loginTitleLabel.setText('User Login')
        self.loginTitleLabel.setGeometry(320, 180, 250, 50)
        self.loginTitleLabel.setStyleSheet('background: none; font-family: gotham; font-weight: bold; font-size: 40px; color: white;')
        self.loginTitleLabel.show()

    def loginPageEntrys (self):

        ##############################
        #  Login Page E-Mail Entry   #
        ##############################
        self.emailEntry_login = QLineEdit(self.loginFrame)
        self.emailEntry_login.setGeometry(285, 265, 300, 40)
        self.emailEntry_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emailEntry_login.setMaxLength(100)
        self.emailEntry_login.setPlaceholderText('E-mail')
        self.emailEntry_login.setStyleSheet('background-color: rgba(0, 0, 0, 0); border: 2px solid #00f0ff; border-radius: 20px; color: gray;')
        self.emailEntry_login.show()

        ##############################
        # Login Page Password Entry  #
        ##############################
        self.passwordEntry_login_frame = QLineEdit(self.loginFrame)
        self.passwordEntry_login_frame.setGeometry(285, 335, 300, 40)
        self.passwordEntry_login_frame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.passwordEntry_login_frame.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEntry_login_frame.setMaxLength(8)
        self.passwordEntry_login_frame.setPlaceholderText('Senha')
        self.passwordEntry_login_frame.setStyleSheet('background-color: rgba(0, 0, 0, 0); border: 2px solid #00f0ff; border-radius: 20px; color: gray;')
        self.passwordEntry_login_frame.show()

    def loginPageButtons(self):

        ##############################
        #  Button For The About Us   #
        ##############################
        self.aboutUsButton = QPushButton(self.loginFrame)
        self.aboutUsButton.setText('SOBRE NÓS')
        self.aboutUsButton.setGeometry(850, 10, 200, 50)
        self.aboutUsButton.setStyleSheet('background: none; border-radius: 5px; color: white; font-family: gotham;')
        self.aboutUsButton.show()

        ##############################
        #    Button For The Menu     #
        ##############################
        self.menuButton = QPushButton(self.loginFrame)
        self.menuButton.setGeometry(1024, 7, 50, 50)
        self.menuButton.setStyleSheet('background: none; border-radius: 5px; background-image: url( ../images/firstPageImages/menu.png); background-repeat: none;')
        self.menuButton.show()

        ##############################
        #  Button For The Forgot Password   #
        ##############################
        self.forgotPasswordButton = QPushButton(self.loginFrame)
        self.forgotPasswordButton.setText('Esqueceu a Senha?')
        self.forgotPasswordButton.setGeometry(340, 390, 200, 50)
        self.forgotPasswordButton.setStyleSheet('background: none; border-radius: 5px; color: white; font-family: gotham; font-size: 15px;')
        self.forgotPasswordButton.show()

        ##############################
        #    Button For The Login    #
        ##############################
        self.loginButton = QPushButton(self.loginFrame)
        self.loginButton.setText('LOG IN')
        self.loginButton.setGeometry(285, 450, 300, 40)
        self.loginButton.setStyleSheet('background-color: #00f0ff; border-radius: 20px; color: black; font: bold gotham; font-size: 17px;')
        self.loginButton.clicked.connect(self.confirmation_user)
        self.loginButton.show()

        ##############################
        #  Button For The Cadastre   #
        ##############################
        self.cadastreButton = QPushButton(self.loginFrame)
        self.cadastreButton.setText('Ou Cadastre-se')
        self.cadastreButton.setGeometry(335, 530, 200, 50)
        self.cadastreButton.setStyleSheet('background: none; border-radius: 5px; color: white; font-family: gotham; font-size: 15px;')
        self.cadastreButton.clicked.connect(self.loadCadastrePage)
        self.cadastreButton.show()
    
    def loadCadastrePage (self):

        ##############################
        #   Delete The Login Frame   #
        ##############################
        self.loginFrame.deleteLater()

        self.cadastrePageFrame()
        self.cadastrePageLabels()
        self.cadastrePageButtons()

    #######################################################
    #                  third Page Things                  #
    #######################################################
    def cadastrePageLabels (self):
        
        ##############################
        # Importing The Cadastre     #
        # Frame                      #
        ##############################
        self.cadastrePageFrame()

        ##############################
        #  Label For The Background  #
        ##############################
        self.backgroundLabel = QLabel(self.cadastreFrame)
        self.backgroundLabel.setGeometry(0, 0, 1080, 720)
        self.backgroundLabel.setPixmap(QtGui.QPixmap('../images/thirdPageImages/bg3.jpg'))
        self.backgroundLabel.show()

        ##############################
        #  Label For The Green Logo  #
        ##############################
        self.logoLabel = QLabel(self.cadastreFrame)
        self.logoLabel.setGeometry(20, 20, 200, 50)
        self.logoLabel.setPixmap(QtGui.QPixmap('../images/thirdPageImages/logo3.png'))
        self.logoLabel.show()

        ##############################
        # Label For The Cadastre Men-#
        # sage                       #
        ##############################
        self.cadastreMensageLabel = QLabel(self.cadastreFrame)
        self.cadastreMensageLabel.setGeometry(695, 150, 220, 50)
        self.cadastreMensageLabel.setText('Cadastrar')
        self.cadastreMensageLabel.setStyleSheet('color: white; font: bold 40px gotham;')
        self.cadastreMensageLabel.show()

    def cadastrePageButtons (self):

        ##############################
        # Button For Return Back For #
        # The Login Page             #
        ##############################
        self.ReturnToLoginButton = QPushButton(self.cadastreFrame)
        self.ReturnToLoginButton.setText('LOG  IN')
        self.ReturnToLoginButton.setGeometry(750, 10, 220, 50)
        self.ReturnToLoginButton.setStyleSheet('background: none; border-radius: 5px; color: white; font-family: gotham;')
        self.ReturnToLoginButton.clicked.connect(self.loadRetunBackButton)
        self.ReturnToLoginButton.show()

        ##############################
        #  Button For The About Us   #
        ##############################
        self.aboutUsButton = QPushButton(self.cadastreFrame)
        self.aboutUsButton.setText('SOBRE NÓS')
        self.aboutUsButton.setGeometry(850, 10, 200, 50)
        self.aboutUsButton.setStyleSheet('background: none; border-radius: 5px; color: white; font-family: gotham;')
        self.aboutUsButton.show()

        ##############################
        #    Button For The Menu     #
        ##############################
        self.menuButton = QPushButton(self.cadastreFrame)
        self.menuButton.setGeometry(1024, 7, 50, 50)
        self.menuButton.setStyleSheet('background: none; border-radius: 5px; background-image: url( ../images/firstPageImages/menu.png); background-repeat: none;')
        self.menuButton.show()

        ##############################
        # Button For Accept The Term #
        ##############################
        self.acceptTheTermsButton = QCheckBox('Eu aceito os termos de privacidade.', self.cadastreFrame)
        self.acceptTheTermsButton.setGeometry(705, 485, 260, 50)
        self.acceptTheTermsButton.setStyleSheet('color: white;')
        self.acceptTheTermsButton.show()

        ##############################
        #  Button For The Cadastre   #
        ##############################
        self.cadastreButton = QPushButton(self.cadastreFrame)
        self.cadastreButton.setText('Cadastre-se')
        self.cadastreButton.setGeometry(650, 550, 300, 40)
        self.cadastreButton.setStyleSheet('background-color: #00f0ff; border-radius: 20px; color: black; font: bold gotham; font-size: 17px;')
        self.cadastreButton.clicked.connect(self.create_user)
        self.cadastreButton.show()

        '''def cadastrePageEntrys (self): A função não está funcionando, não fasso ideia do que seja.'''

        ##############################
        #  Login Page E-Mail Entry   #
        ##############################
        self.nameEntry = QLineEdit(self.cadastreFrame)
        self.nameEntry.setGeometry(650, 220, 300, 40)
        self.nameEntry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nameEntry.setMaxLength(20)
        self.nameEntry.setPlaceholderText('Nome')
        self.nameEntry.setStyleSheet('background-color: rgba(0, 0, 0, 0); border: 2px solid #00f0ff; border-radius: 20px; color: gray;')
        self.nameEntry.show()

        ##############################
        # Login Page Password Entry  #
        ##############################
        self.surnameEntry = QLineEdit(self.cadastreFrame)
        self.surnameEntry.setGeometry(650, 290, 300, 40)
        self.surnameEntry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.surnameEntry.setMaxLength(20)
        self.surnameEntry.setPlaceholderText('Sobrenome')
        self.surnameEntry.setStyleSheet('background-color: rgba(0, 0, 0, 0); border: 2px solid #00f0ff; border-radius: 20px; color: gray;')
        self.surnameEntry.show()

        ##############################
        #  Login Page E-Mail Entry   #
        ##############################
        self.emailEntry = QLineEdit(self.cadastreFrame)
        self.emailEntry.setGeometry(650, 360, 300, 40)
        self.emailEntry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emailEntry.setMaxLength(100)
        self.emailEntry.setPlaceholderText('E-mail')
        self.emailEntry.setStyleSheet('background-color: rgba(0, 0, 0, 0); border: 2px solid #00f0ff; border-radius: 20px; color: gray;')
        self.emailEntry.show()

        ##############################
        # Login Page Password Entry  #
        ##############################
        self.passwordEntry = QLineEdit(self.cadastreFrame)
        self.passwordEntry.setGeometry(650, 430, 300, 40)
        self.passwordEntry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.passwordEntry.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEntry.setMaxLength(8)
        self.passwordEntry.setPlaceholderText('Senha')
        self.passwordEntry.setStyleSheet('background-color: rgba(0, 0, 0, 0); border: 2px solid #00f0ff; border-radius: 20px; color: gray;')
        self.passwordEntry.show()
    
    def loadRetunBackButton (self):

        ##############################
        #   Delete The Login Frame   #
        ##############################
        self.cadastreFrame.deleteLater()

        self.loginPageFrame()
        self.loginPageLabels()
        self.loginPageEntrys()
        self.loginPageButtons()

    def loadMainWindow (self):

        ##############################
        # Main Window Configurations #
        ##############################
        self.setWindowTitle('Oficina do Corpo em Movimento')
        self.setWindowIcon(QIcon('../images/firstPageImages/Icon.png'))
        self.setGeometry(250, 90, 1080, 720)
        self.setMaximumSize(1080, 720)
        self.setMinimumSize(600, 400)
        self.show()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
