from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random

code_verification = random.randrange(0, 9999)

msg = MIMEMultipart()
message = f'Seu código de verificação é {code_verification}'

password = 'steelseries'
msg['From'] = 'testiktok111@gmail.com'
msg['To'] = f'{self.email}'
msg['Subject'] = 'Código de verifição Oficina Corpo e Movimento'

msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
