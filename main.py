from flask import Flask, render_template
app = Flask(__name__)
PORT = 5000
DEBUG = FALSE


@app.route('/')
@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/vis')
def vis_page():
    items = [
        {'id': 1, 'name': 'Clientes Banco', 'page': 'clientesbanco_page', 'desc': 'Esse cillum qui reprehenderit fugiat duis anim duis anim cillum est.'},
        {'id': 2, 'name': 'Salario Promedio', 'page': 'salariopromedio_page', 'desc': 'Pariatur enim incididunt sint Lorem incididunt reprehenderit eu ut.'},
        {'id': 3, 'name': 'Venta Vehiculos', 'page': 'vehiculosventa_page', 'desc': 'Est ad mollit excepteur proident aute deserunt.'},
        {'id': 4, 'name': 'Doble Eje', 'page': 'dobleeje_page', 'desc': 'Cupidatat ex officia ipsum proident ad sunt nulla veniam culpa non culpa fugiat adipisicing.'},
        {'id': 5, 'name': 'Startup Expansion', 'page': 'startupexpansion_page', 'desc': 'Mollit incididunt cupidatat irure eiusmod commodo nulla nisi do culpa dolore sint enim magna commodo.'}
    ]
    return render_template('vis.html', items=items)

@app.route('/clientes-banco')
def clientesbanco_page():
    return render_template('v-clientes-banco.html')

@app.route('/salario-promedio')
def salariopromedio_page():
    return render_template('v-salario-promedio.html')

@app.route('/vehiculos-venta')
def vehiculosventa_page():
    return render_template('v-vehiculos-venta.html')

@app.route('/doble-eje')
def dobleeje_page():
    return render_template('v-doble-eje.html')

@app.route('/startup-expansion')
def startupexpansion_page():
    return render_template('v-startup-expansion.html')

