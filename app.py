from flask import Flask, render_template, request
from LDB.conexion import DAO

dao = DAO()
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/detalle')
def detalle():
    return render_template('detalle.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@app.route('/crud')
def crud():
    return render_template('crud.html')

@app.route('/insert_prod', methods=['POST'])
def insert_prod():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nombrel = request.form['nombrel']
        descripcionc = request.form['descripcionc']
        descripcionl = request.form['descripcionl']
        precio = request.form['precio']
        promocion = request.form['promocion']
        cantidad = request.form['cantidad']
        url = request.form['url']
        prod = {
            "nombrec" : nombre
            , "nomnbrel" : nombrel
            , "descc" : descripcionc
            , "descl" : descripcionl
            , "precio" : precio
            , "promocion" : promocion
            , "cantidad" : cantidad
            , "url" : url
        }
        print(dao.insertar_producto(prod))
        return 'Registrado'

if __name__ == '__main__':
    app.run(port= 3000, debug=True)
