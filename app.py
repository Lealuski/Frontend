from flask import Flask, render_template


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

if __name__ == '__main__':
    app.run(port= 3000, debug=True)
