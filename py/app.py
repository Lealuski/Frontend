from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return 'Home'

@app.route('/login')
def login():
    return 'Login'

@app.route('/detalle')
def detalle():
    return 'Detalle productos'

@app.route('/catalogo')
def catalogo():
    return 'Catalogo'

@app.route('/crud')
def crud():
    return 'Crud'

if __name__ == '__main__':
    app.run(port= 3000, debug=True)
