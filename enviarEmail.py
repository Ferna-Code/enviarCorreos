import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mi_correo = 'fernaluengo@gmail.com'
mi_pass = 'contrasena gmail'
receptor = 'codeferna@gmail.com'
message = MIMEMultipart()
message['From'] = mi_correo
message['To'] = receptor
message['Subject'] = 'Email de prueba'

body = 'Este es un correo de prueba'
message.attach(MIMEText(body, 'plain'))
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(mi_correo, mi_pass)

smtp_server.sendmail(mi_correo, receptor, message.as_string())
smtp_server.quit()
print('Correo enviado')
