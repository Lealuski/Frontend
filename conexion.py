import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                user='root', 
                password='', 
                host='localhost', 
                database='flamel', 
                port='3306'
            )
        except Error as ex:
            print('Error al intentar la conexion: {0}'.format(ex))

    def listar_productos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM producto ORDER BY id DESC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print('Error al intentar la conexion: {0}'.format(ex))

    def insertar_producto(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("INSERT INTO producto () VALUES ('{0}')".format())
                conexion.commit()
                return True
            except Error as ex:
                print('Error al intentar la conexion: {0}'.format(ex))                