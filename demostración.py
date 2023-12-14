"""
En este apartado realizaremos una demostración del uso del programa de tutorías de INACAP desde una
persepectva orientada a los encargados tecnicos de la institución así como explicaciones breves que ayuden
a comprender el código fuente y el uso de las herramientas utilizadas.
"""

from inecuacion import Inecuacion


def menu():
    """
    Bienvenida al programa de tutorías de INACAP.
    """
    print("Bienvenido al programa de tutorías de INACAP.")
    print("Este programa tiene como objetivo notificar a los tutores de los alumnos que se encuentran en riesgo de reprobar un ramo.")
    print("Para ello se debe configurar el programa con las credenciales del servidor SMTP y los datos de conexión a la base de datos.")
    print("Se recomienda que el programa se ejecute cada 24horas para evitar la saturación de los servidores.")
    print("Para configurar el programa se debe ejecutar el archivo main.py")
    print("Para iniciar el programa se debe ejecutar el archivo main.py")
    print("""
    ingresa 1 para iniciar el programa""")

def main():
    """
    Función principal del programa.
    """
    menu()
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        script = Inecuacion()
    else:
        print("Opción incorrecta, por favor intente nuevamente.")
        main()