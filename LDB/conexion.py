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

    def insertar_producto(self, producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                values = "nombrecorto, nombrelargo, descripcioncorta, descripcionlarga, precio, promocion, cantidad, url"
                cursor.execute("INSERT INTO producto ('{0}') VALUES ('{1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}')".format(
                    values
                    , producto.get('nombrec')
                    , producto.get('nombrel')
                    , producto.get('descc')
                    , producto.get('descl')
                    , producto.get('precio')
                    , producto.get('promocion')
                    , producto.get('cantidad')
                    , producto.get('url')
                ))
                self.conexion.commit()
                return 'Producto "{0} registrado"'.format(producto.get('nombrec'))
            except Error as ex:
                print('Error al intentar la conexion: {0}'.format(ex))                