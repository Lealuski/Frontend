from flask import Flask, render_template, request, url_for, redirect, flash
from LDB.conexion import DAO

dao = DAO()
app = Flask(__name__)
app.secret_key = 'mysecretkey'

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
    getprods = dao.listar_productos()
    print(getprods)
    return render_template('catalogo.html', products=getprods)

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
        mes = dao.insertar_producto(prod)
        print(mes)
        flash(mes)
        return redirect(url_for('crud'))

if __name__ == '__main__':
    app.run(port= 3000, debug=True)
