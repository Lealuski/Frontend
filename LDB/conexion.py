import mysql.connector
from mysql.connector import Error
#Para ejecutar se deben tener las tablas que están en la carpeta Scripts
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
                cursor.execute("SELECT * FROM producto")
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
                return 'Producto "{0}" registrado'.format(producto.get('nombrec'))
            except Error as ex:
                print('Error al intentar la conexion: {0}'.format(ex))

    def actualizar_producto(self, producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("UPDATE producto SET {0} = {1}, {2} = '{3}', {4} = '{5}', {6} = '{7}', {8} = '{9}', {10} = '{11}', {12} = '{13}', {14} = '{15}')".format(
                    'producto_nombrecorto'
                    , producto.get('nombrec') if producto.get('nombrec') is not None else ""
                    ,'producto_nombrelargo'
                    , producto.get('nombrel') if producto.get('nombrel') is not None else ""
                    ,'producto_descripcioncorto'
                    , producto.get('descc') if producto.get('descc') is not None else ""
                    , 'producto_descripcionlarga'
                    , producto.get('descl') if producto.get('descl') is not None else ""
                    , 'producto_precio'
                    , producto.get('precio') if producto.get('precio') is not None else ""
                    , 'producto_promocion'
                    , producto.get('promocion') if producto.get('promocion') is not None else ""
                    , 'producto_cantidad'
                    , producto.get('cantidad') if producto.get('cantidad') is not None else ""
                    , 'producto_ulrimagen'
                    , producto.get('url') if producto.get('url') is not None else ""
                ))
                self.conexion.commit()
                return 'Producto "{0} actualizado"'.format(producto.get('nombrec'))
            except Error as ex:
                print('Error al intentar la conexion: {0}'.format(ex))  