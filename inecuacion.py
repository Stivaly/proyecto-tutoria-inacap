from setdatabase import *
from email import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


"""
Esta clase permite enviar correos electrónicos a través de un servidor SMTP.
Debes conocer las credenciales del remitente (correo y contraseña) y el servidor SMTP, además del puerto SMTP. Esto debes solicitarselo al administrador del servidor SMTP.
"""
class Correo:
    def __init__(self):
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


class Inecuacion(Correo):
    def __init__(self, nota1, nota2, nota3, nota4, tutor_nombre, tutor_correo, alumno_nombre, semestre, asignatura_nombre):
        super().__init__()
        self.nota1_comparar = 0
        self.nota2_comparar = 0
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.tutor_nombre = tutor_nombre
        self.tutor_correo = tutor_correo
        self.alumno_nombre = alumno_nombre
        self.semestre = semestre
        self.asignatura_nombre = asignatura_nombre
        
    def solicitud_base_datos(self):
        database = DatabaseConnector()
        database.connect_sqlite()
        database.fetch_data()
        i = 0
        for i in range(0, len(database)):
            if database[i][0] + database[i][1] < 4:
                envio_mail = Correo()
                envio_mail.enviar_correo(self.tutor_correo, "Riesgo de reprobación", "Estimado/a " + self.tutor_nombre + ", su pupilo " + self.alumno_nombre + " está en riesgo de reprobar el ramo " + self.asignatura_nombre + " del semestre " + self.semestre + ".")
                i += 1
            elif database[i][0] + database[i][2] < 4:
                envio_mail = Correo()
                envio_mail.enviar_correo(self.tutor_correo, "Riesgo de reprobación", "Estimado/a " + self.tutor_nombre + ", su pupilo " + self.alumno_nombre + " está en riesgo de reprobar el ramo " + self.asignatura_nombre + " del semestre " + self.semestre + ".")
                i += 1
            elif database[i][0] + database[i][3] < 4:
                envio_mail = Correo()
                envio_mail.enviar_correo(self.tutor_correo, "Riesgo de reprobación", "Estimado/a " + self.tutor_nombre + ", su pupilo " + self.alumno_nombre + " está en riesgo de reprobar el ramo " + self.asignatura_nombre + " del semestre " + self.semestre + ".")
                i += 1
            elif database[i][1] + database[i][2] < 4:
                envio_mail = Correo()
                envio_mail.enviar_correo(self.tutor_correo, "Riesgo de reprobación", "Estimado/a " + self.tutor_nombre + ", su pupilo " + self.alumno_nombre + " está en riesgo de reprobar el ramo " + self.asignatura_nombre + " del semestre " + self.semestre + ".")
                i += 1
            elif database[i][1] + database[i][3] < 4:
                envio_mail = Correo()
                envio_mail.enviar_correo(self.tutor_correo, "Riesgo de reprobación", "Estimado/a " + self.tutor_nombre + ", su pupilo " + self.alumno_nombre + " está en riesgo de reprobar el ramo " + self.asignatura_nombre + " del semestre " + self.semestre + ".")
                i += 1
            elif database[i][2] + database[i][3] < 4:
                envio_mail = Correo()
                envio_mail.enviar_correo(self.tutor_correo, "Riesgo de reprobación", "Estimado/a " + self.tutor_nombre + ", su pupilo " + self.alumno_nombre + " está en riesgo de reprobar el ramo " + self.asignatura_nombre + " del semestre " + self.semestre + ".")
                i += 1
            else:
                print("No hay alumnos en riesgo de reprobar el ramo")
            


