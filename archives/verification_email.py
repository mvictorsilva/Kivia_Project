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
