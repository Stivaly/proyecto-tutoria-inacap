
"""
En este archivo se encuentran las variables de conexión a la base de datos.

Se debe solicitar al Administrador de la base de datos los datos de conexión, el puente de conexión
y el nombre de los campos de notas y asignaturas clasificados por semestre actual únicamente.

Entendiendo que desconocemos esta información crearemos un códgio de fácil mantención
que permita al equipo técnico de INACAP modificar los datos de conexión sin necesidad de
modificar el código fuente.

"""

# Variables de conexión a la base de datos. Estas variables deben ser modificadas por el equipo técnico de INACAP.

import psycopg2
import sqlite3
import mysql.connector

class DatabaseConnector:
    """
    Clase que permite la conexión a la base de datos.
    Campos a modificar:
    sqlite_database = "mydatabase.db" # Nombre de la base de datos SQLite 
    
    """
    def __init__(self):
        self.mysql_host = "localhost"
        self.mysql_user = "root"
        self.mysql_password = "password"
        self.mysql_database = "mydatabase"

        self.pg_host = "localhost"
        self.pg_user = "postgres"
        self.pg_password = "password"
        self.pg_database = "mydatabase"

        self.sqlite_database = "demotutorias.db"

    def connect_mysql(self):
        mysql_conn = mysql.connector.connect(
            host=self.mysql_host,
            user=self.mysql_user,
            password=self.mysql_password,
            database=self.mysql_database
        )
        return mysql_conn

    def connect_postgresql(self):
        pg_conn = psycopg2.connect(
            host=self.pg_host,
            user=self.pg_user,
            password=self.pg_password,
            database=self.pg_database
        )
        return pg_conn

    def connect_sqlite(self):
        sqlite_conn = sqlite3.connect(self.sqlite_database)
        return sqlite_conn

    def fetch_data(self, conn):
        cursor = conn.cursor()
        cursor.execute("SELECT nota1, nota2, nota3, nota4, tutor_nombre, tutor_correo, alumno_nombre, alumno_rut, semestre, asignatura_nombre FROM notas") 
        # Consultar al administrador de la base de datoss la consulta correcta para sacar estos datos y pegala en el cursor.execute
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

