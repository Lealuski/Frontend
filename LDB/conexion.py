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
                values = "producto_nombrecorto, producto_nombrelargo, producto_descripcioncorto, producto_descripcionlarga, producto_precio, producto_promocion, producto_cantidad, producto_ulrimagen"
                cursor.execute("INSERT INTO producto ({0}) VALUES ('{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')".format(
                    values
                    , producto.get('nombrec') if producto.get('nombrec') is not None else ""
                    , producto.get('nombrel') if producto.get('nombrel') is not None else ""
                    , producto.get('descc') if producto.get('descc') is not None else ""
                    , producto.get('descl') if producto.get('descl') is not None else ""
                    , producto.get('precio') if producto.get('precio') is not None else ""
                    , producto.get('promocion') if producto.get('promocion') is not None else ""
                    , producto.get('cantidad') if producto.get('cantidad') is not None else ""
                    , producto.get('url') if producto.get('url') is not None else ""
                ))
                self.conexion.commit()
                return 'Producto "{0} registrado"'.format(producto.get('nombrec'))
            except Error as ex:
                print('Error al intentar la conexion: {0}'.format(ex))                