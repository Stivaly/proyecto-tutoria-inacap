from setdatabase import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


"""
Esta clase permite enviar correos electrónicos a través de un servidor SMTP.
Debes conocer las credenciales del remitente (correo y contraseña) y el servidor SMTP, además del puerto SMTP. Esto debes solicitarselo al administrador del servidor SMTP.
"""
class Correo:
    def __init__(self):
        self.remitente = 'notreply@ejemplo.com' # Se recomienda que el remitente sea un correo noreply genérico
        self.contraseña = '' # Se debe solicitar el acceso por seguridad a el administrador del servidor SMTP para su configuración
        self.servidor_smtp = 'smtp-mail.outlook.com' # Cambiar si se usa otro servidor SMTP
        self.puerto_smtp = 587 # Cambiar si se usa otro puerto SMTP

    def enviar_correo(self, destinatario, asunto, mensaje):
        print("Intentando enviar correo...")
        mensaje_correo = MIMEMultipart()
        mensaje_correo['From'] = self.remitente
        mensaje_correo['To'] = destinatario
        mensaje_correo['Subject'] = asunto
        mensaje_correo.attach(MIMEText(mensaje, 'plain'))

        try:
            with smtplib.SMTP(host=self.servidor_smtp, port=self.puerto_smtp) as server:
                server.starttls()
                server.login(self.remitente, self.contraseña)
                server.send_message(mensaje_correo)
                print("Correo enviado exitosamente.")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")


class Inecuacion(Correo):
    def __init__(self):
        super().__init__()
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0
        self.nota4 = 0
        self.tutor_nombre = "tutor_nombre"
        self.tuto_correo = "tutor_correo"
        self.alumno_nombre = "alumno_nombre"
        self.semestre = "semestre"
        self.asignatura_nombre = "asignatura_nombre"
        self.carrera = "carrera"
        self._solicitud_base_datos()
        
    def _solicitud_base_datos(self):
        database = DatabaseConnector()
        connect = database.connect_sqlite()
        result = database.fetch_data(connect)
        print("prueba")
        for row in result:
            print(result)
            nota1, nota2, nota3, nota4, tutor_nombre, tuto_correo, alumno_nombre, semestre, asignatura_nombre, carrera = row
            print(row)
            self.nota1 = nota1
            self.nota2 = nota2
            self.nota3 = nota3
            self.nota4 = nota4
            self.tutor_nombre = tutor_nombre
            self.tuto_correo = tuto_correo
            self.alumno_nombre = alumno_nombre
            self.semestre = semestre
            self.asignatura_nombre = asignatura_nombre
            self.carrera = carrera
            if self.nota1 < 4.0 and self.nota2 < 4.0:
                envio_mail = Correo()
                envio_mail.enviar_correo(self.tuto_correo, "Riesgo de reprobación", f"Estimado/a {self.tutor_nombre} su pupilo {self.alumno_nombre} está en riesgo de reprobar el ramo {self.asignatura_nombre} de la carrera {self.carrera} del semestre {self.semestre}.")
                print("Correo enviado correctamente")
            elif self.nota1 < 4.0 and self.nota2 < 4.0:
                envio_mail = Correo()
                envio_mail.enviar_correo(self.tuto_correo, "Riesgo de reprobación", f"Estimado/a {self.tutor_nombre} su pupilo {self.alumno_nombre} está en riesgo de reprobar el ramo {self.asignatura_nombre} de la carrera {self.carrera} del semestre {self.semestre}.")
                print("Correo enviado correctamente")
            elif self.nota1 < 4.0 and self.nota2 < 4.0:
                envio_mail = Correo()
                envio_mail.enviar_correo(self.tuto_correo, "Riesgo de reprobación", f"Estimado/a {self.tutor_nombre} su pupilo {self.alumno_nombre} está en riesgo de reprobar el ramo {self.asignatura_nombre} de la carrera {self.carrera} del semestre {self.semestre}.")
                print("Correo enviado correctamente")
            elif self.nota1 < 4.0 and self.nota2 < 4.0:
                envio_mail = Correo()
                envio_mail.enviar_correo(self.tuto_correo, "Riesgo de reprobación", f"Estimado/a {self.tutor_nombre} su pupilo {self.alumno_nombre} está en riesgo de reprobar el ramo {self.asignatura_nombre} de la carrera {self.carrera} del semestre {self.semestre}.")
                print("Correo enviado correctamente")
            elif self.nota1 < 4.0 and self.nota2 < 4.0:
                envio_mail = Correo()
                envio_mail.enviar_correo(self.tuto_correo, "Riesgo de reprobación", f"Estimado/a {self.tutor_nombre} su pupilo {self.alumno_nombre} está en riesgo de reprobar el ramo {self.asignatura_nombre} de la carrera {self.carrera} del semestre {self.semestre}.")
                print("Correo enviado correctamente")
            elif self.nota1 < 4.0 and self.nota2 < 4.0:
                envio_mail = Correo()
                envio_mail.enviar_correo(self.tuto_correo, "Riesgo de reprobación", f"Estimado/a {self.tutor_nombre} su pupilo {self.alumno_nombre} está en riesgo de reprobar el ramo {self.asignatura_nombre} de la carrera {self.carrera} del semestre {self.semestre}.")
                print("Correo enviado correctamente")
            else:
                print("No hay alumnos en riesgo de reprobar el ramo")
            connect.close()
            
        return print("El Script ha finalizado correctamente.")