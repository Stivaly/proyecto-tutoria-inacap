"""
Esta clase permite enviar correos electrónicos a través de un servidor SMTP.
Debes conocer las credenciales del remitente (correo y contraseña) y el servidor SMTP, además del puerto SMTP. Esto debes solicitarselo al administrador del servidor SMTP.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Correo:
    def __init__(self, remitente, contraseña, puerto_smtp=587):
        self.remitente = 'ejemplo@gmail.com' # Se recomienda que el remitente sea un correo noreply genérico
        self.contraseña = '21AEBC48383652046150C3663A57B1CB5BF957B5ECE024DEB9CBC087478CDF80' # Se debe solicitar el acceso por seguridad a el administrador del servidor SMTP para su configuración
        self.servidor_smtp = 'smtp.gmail.com' # Cambiar si se usa otro servidor SMTP
        self.puerto_smtp = '587' # Cambiar si se usa otro puerto SMTP

    def enviar_correo(self, destinatario, asunto, mensaje):
        mensaje_correo = MIMEMultipart()
        mensaje_correo['From'] = self.remitente
        mensaje_correo['To'] = destinatario
        mensaje_correo['Subject'] = asunto
        mensaje_correo.attach(MIMEText(mensaje, 'plain'))

        with smtplib.SMTP(host=self.servidor_smtp, port=self.puerto_smtp) as server:
            server.starttls()
            server.login(self.remitente, self.contraseña)
            server.send_message(mensaje_correo)
