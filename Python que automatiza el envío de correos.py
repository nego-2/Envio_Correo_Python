import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Dirección de tu correo y contraseña de aplicación (si tienes activada la autenticación en dos pasos)
mi_correo = 'pruebasql@outlook.es'  # Tu correo de Outlook
mi_pass = 'tu_contraseña_de_aplicacion'  # Aquí va la contraseña de aplicación generada
receptor = 'nego@gmail.com'  # Dirección del receptor
message = MIMEMultipart()

# Definir los campos del mensaje
message['From'] = mi_correo
message['To'] = receptor
message['Subject'] = 'Email de prueba'

# Cuerpo del mensaje
body = 'Este es un correo de prueba'
message.attach(MIMEText(body, 'plain'))

# Configurar el servidor SMTP para Outlook
smtp_server = smtplib.SMTP('smtp.office365.com', 587)
smtp_server.starttls()  # Inicia la conexión segura

# Iniciar sesión con el correo y la contraseña de aplicación
smtp_server.login(mi_correo, mi_pass)

# Enviar el correo
smtp_server.sendmail(mi_correo, receptor, message.as_string())

# Cerrar la conexión con el servidor SMTP
smtp_server.quit()

# Mensaje de confirmación
print('Correo enviado')
