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
                    background-image: url(../images/menuFrames/whitelogo2.png);
                    background-color: rgba(0, 0, 0, 0);
                    background-repeat: none;
                }
            '''
        )
        self.logoImage.setGeometry(0, 0, 268, 194)
        self.logoImage.show()
        
        self.buttonBegin = QPushButton("Inicio", self.menuBarFrame)
        self.buttonBegin.setGeometry(40, 200, 200, 50)
        self.buttonBegin.setStyleSheet(
            '''
                QPushButton{
                    font-size: 25px;
                    border: none;
                    border-radius: 10px;
                    color: whitesmoke;
                    background-image: url(../images/menuFrames/Inicio.png);
                    background-position: left;
                    background-repeat: none;
                }

                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 40);
                }
            '''
        )
        self.buttonBegin.clicked.connect(lambda: (self.delete(), self.mainFrame_one()))
        self.buttonBegin.show()
        
        self.buttonHelth = QPushButton("Saude", self.menuBarFrame)
        self.buttonHelth.setGeometry(40, 270, 200, 50)
        self.buttonHelth.setStyleSheet(
            '''
                QPushButton{
                    font-size: 25px;
                    border: none;
                    border-radius: 10px;
                    color: whitesmoke;
                    background-image: url(../images/menuFrames/Saude.png);
                    background-position: left;
                    background-repeat: none;
                }

                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 40);
                }
            '''
        )
        self.buttonHelth.clicked.connect(lambda: (self.delete(), self.mainFrame_two()))
        self.buttonHelth.show()

        self.buttonClasses = QPushButton("Aulas", self.menuBarFrame)
        self.buttonClasses.setGeometry(40, 330, 200, 50)
        self.buttonClasses.setStyleSheet(
            '''
                QPushButton{
                    font-size: 25px;
                    border: none;
                    border-radius: 10px;
                    color: whitesmoke;
                    background-image: url(../images/menuFrames/aulas.png);
                    background-position: left;
                    background-repeat: none;
                }

                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 40);
                }
            '''
        )
        self.buttonClasses.clicked.connect(lambda: (self.delete(), self.mainFrame_tree()))
        self.buttonClasses.show()

        self.buttonExercices = QPushButton("Exercícios", self.menuBarFrame)
        self.buttonExercices.setGeometry(35, 390, 200, 50)
        self.buttonExercices.setStyleSheet(
            '''
                QPushButton{
                    font-size: 25px;
                    border: none;
                    border-radius: 10px;
                    color: whitesmoke;
                    background-image: url(../images/menuFrames/exercicios.png);
                    background-position: left;
                    background-repeat: none;
                }

                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 40);
                }
            '''
        )
        self.buttonExercices.clicked.connect(lambda: (self.delete(), self.mainFrame_four()))
        self.buttonExercices.show()

        self.buttonSchedule = QPushButton("Agenda", self.menuBarFrame)
        self.buttonSchedule.setGeometry(40, 450, 200, 50)
        self.buttonSchedule.setStyleSheet(
            '''
                QPushButton{
                    font-size: 25px;
                    border: none;
                    border-radius: 10px;
                    color: whitesmoke;
                    background-image: url(../images/menuFrames/agenda.png);
                    background-position: left;
                    background-repeat: none;
                }

                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 40);
                }
            '''
        )
        self.buttonSchedule.clicked.connect(lambda: (self.delete(), self.mainFrame_five()))
        self.buttonSchedule.show()

        self.buttonProfile = QPushButton("Perfil", self.menuBarFrame)
        self.buttonProfile.setGeometry(40, 510, 200, 50)
        self.buttonProfile.setStyleSheet(
            '''
                QPushButton{
                    font-size: 25px;
                    border: none;
                    border-radius: 10px;
                    color: whitesmoke;
                    background-image: url(../images/menuFrames/perfil.png);
                    background-position: left;
                    background-repeat: none;
                }

                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 40);
                }
            '''
        )
        self.buttonProfile.clicked.connect(lambda: (self.delete(), self.mainFrame_six()))
        self.buttonProfile.show()

    def mainFrame_one(self):
        self.beginFrame = QFrame(self.menuBarFrame)
        self.beginFrame.setGeometry(250, 10, 940, 700)
        self.beginFrame.setStyleSheet(
            '''
                QFrame{
                    border-radius: 20px;
                    background-color: #f7f7f7;
                }
            '''
        )
        self.beginFrame.show()

        self.wellcome = QLabel("Início", self.beginFrame)
        self.wellcome.setGeometry(50, 30, 635, 75)
        self.wellcome.setStyleSheet(
            '''
                QLabel{
                    font-size: 40px;
                    background: none;
                }
            '''
        )
        self.wellcome.show()

    def mainFrame_two(self):
        self.helthframe = QFrame(self.menuBarFrame)
        self.helthframe.setGeometry(250, 10, 940, 700)
        self.helthframe.setStyleSheet(
            '''
                QFrame{
                    border-radius: 20px;
                    background-color: #f7f7f7;
                }
            '''
        )
        self.helthframe.show()

        self.helthLabel = QLabel("Saúde", self.helthframe)
        self.helthLabel.setGeometry(50, 30, 200, 60)
        self.helthLabel.setStyleSheet(
            '''
                QLabel{
                    font-size: 40px;
                    background: none;
                }
            '''
        )
        self.helthLabel.show()

        self.accompainmentLabel = QLabel("Acompanhamento", self.helthframe)
        self.accompainmentLabel.setGeometry(50, 100, 205, 60)
        self.accompainmentLabel.setStyleSheet(
            '''
                QLabel{
                    font: bold 20px gothan;
                    background: none;
                }
            '''
        )
        self.accompainmentLabel.show()

        self.graphicLabel = QLabel(self.helthframe)
        self.graphicLabel.setGeometry(50, 170, 480, 200)
        self.graphicLabel.setStyleSheet(
            '''
                QLabel{
                    background-image: url(../images/menuFrames/Graph.png);
                    border-radius: 10px;
                    border: none;
                }
            '''
        )
        self.graphicLabel.show()

        self.imcLabel = QLabel("Calcular IMC", self.helthframe)
        self.imcLabel.setGeometry(580, 100, 205, 60)
        self.imcLabel.setStyleSheet(
            '''
                QLabel{
                    font: bold 20px gothan;
                    background: none;
                }
            '''
        )
        self.imcLabel.show()

        self.helthWheigtEntry = QLineEdit(self.helthframe)
        self.helthWheigtEntry.setGeometry(580, 170, 250, 35)
        self.helthWheigtEntry.setPlaceholderText('Peso')
        self.helthWheigtEntry.setStyleSheet(
            '''
                QLineEdit{
                    background-color: rgba(0, 0, 0, 0);
                    border-radius: 10px;
                    border: 2px solid #12555c;
                }
            '''

        )
        self.helthWheigtEntry.show()

        self.helthHeightEntry = QLineEdit(self.helthframe)
        self.helthHeightEntry.setGeometry(580, 215, 250, 35)
        self.helthHeightEntry.setPlaceholderText('Altura')
        self.helthHeightEntry.setStyleSheet(
            '''
                QLineEdit{
                    background-color: rgba(0, 0, 0, 0);
                    border-radius: 10px;
                    border: 2px solid #12555c;
                }
            '''

        )
        self.helthHeightEntry.show()

        self.helthCalculateButton = QPushButton("Calcular", self.helthframe)
        self.helthCalculateButton.setGeometry(580, 260, 250, 35)
        self.helthCalculateButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #12555c;
                    border-radius: 10px;
                    color: whitesmoke;
                }
            '''

        )
        self.helthCalculateButton.show()

        self.imcLabel = QLabel("IMC", self.helthframe)
        self.imcLabel.setGeometry(580, 295, 70, 60)
        self.imcLabel.setStyleSheet(
            '''
                QLabel{
                    font: bold 20px gothan;
                    background: none;
                }
            '''
        )
        self.imcLabel.show()

        self.helthImcEntry = QLineEdit(self.helthframe)
        self.helthImcEntry.setGeometry(650, 305, 180, 35)
        self.helthImcEntry.setStyleSheet(
            '''
                QLineEdit{
                    background-color: rgba(0, 0, 0, 0);
                    border-radius: 10px;
                    border: 2px solid #12555c;
                }
            '''

        )
        self.helthImcEntry.show()

    def mainFrame_tree(self):
        self.classesframe = QFrame(self.menuBarFrame)
        self.classesframe.setGeometry(250, 10, 940, 700)
        self.classesframe.setStyleSheet(
            '''
                QFrame{
                    border-radius: 20px;
                    background-color: #f7f7f7;
                }
            '''
        )
        self.classesframe.show()

        self.classesLabel = QLabel("Aulas", self.classesframe)
        self.classesLabel.setGeometry(50, 30, 200, 60)
        self.classesLabel.setStyleSheet(
            '''
                QLabel{
                    font-size: 40px;
                    background: none;
                }
            '''
        )
        self.classesLabel.show()

        x = 80
        y = 150

        for i in range(7):
            if i == 4:
                x = 80
                y = 430

            self.rectangleLabel = QLabel(self.classesframe)
            self.rectangleLabel.setGeometry(x, y, 180, 200)
            self.rectangleLabel.setStyleSheet(
                '''
                    QLabel{
                        background-image: url(../images/menuFrames/rectangle.png);
                        border-radius: 10px;
                        border: none;
                    }
                '''
            )
            self.rectangleLabel.show()

            x += 300

    def mainFrame_four(self):
        self.exercicesframe = QFrame(self.menuBarFrame)
        self.exercicesframe.setGeometry(250, 10, 940, 700)
        self.exercicesframe.setStyleSheet(
            '''
                QFrame{
                    border-radius: 20px;
                    background-color: #f7f7f7;
                }
            '''
        )
        self.exercicesframe.show()

        self.exercicesLabel = QLabel("Exercícios", self.exercicesframe)
        self.exercicesLabel.setGeometry(50, 30, 200, 60)
        self.exercicesLabel.setStyleSheet(
            '''
                QLabel{
                    font-size: 40px;
                    background: none;
                }
            '''
        )
        self.exercicesLabel.show()

    def mainFrame_five(self):
        self.scheduleframe = QFrame(self.menuBarFrame)
        self.scheduleframe.setGeometry(250, 10, 940, 700)
        self.scheduleframe.setStyleSheet(
            '''
                QFrame{
                    border-radius: 20px;
                    background-color: #f7f7f7;
                }
            '''
        )
        self.scheduleframe.show()

        self.scheduleLabel = QLabel("Agenda", self.scheduleframe)
        self.scheduleLabel.setGeometry(50, 30, 200, 60)
        self.scheduleLabel.setStyleSheet(
            '''
                QLabel{
                    font-size: 40px;
                    background: none;
                }
            '''
        )
        self.scheduleLabel.show()

        self.scheduleMapLabel = QLabel(self.scheduleframe)
        self.scheduleMapLabel.setGeometry(50, 130, 440, 500)
        self.scheduleMapLabel.setStyleSheet(
            '''
                QLabel{
                    background-image: url(../images/menuFrames/schedule.png);
                    border-radius: 10px;
                    border: none;
                }
            '''
        )
        self.scheduleMapLabel.show()

    def mainFrame_six(self):
        self.profileframe = QFrame(self.menuBarFrame)
        self.profileframe.setGeometry(250, 10, 940, 700)
        self.profileframe.setStyleSheet(
            '''
                QFrame{
                    border-radius: 20px;
                    background-color: #f7f7f7;
                }
            '''
        )
        self.profileframe.show()

        self.profileLabel = QLabel("Perfil", self.profileframe)
        self.profileLabel.setGeometry(50, 30, 200, 60)
        self.profileLabel.setStyleSheet(
            '''
                QLabel{
                    font-size: 40px;
                    background: none;
                }
            '''
        )
        self.profileLabel.show()

    def delete(self):
        self.beginFrame.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainFrame()
    window.show()
    sys.exit(app.exec())
