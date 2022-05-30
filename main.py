from flask import Flask, render_template
app = Flask(__name__)
PORT = 5000
DEBUG = False


@app.route('/')
@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/vis')
def vis_page():
    items = [
        {'id': 1, 'name': 'Clientes Banco UK', 'page': 'clientesbanco_page', 'desc': 'Storyline Segmentacion Clientes Banco Regiones UK.'},
        {'id': 2, 'name': 'Mapa Salario Promedio NY', 'page': 'salariopromedio_page', 'desc': 'Graficos Emergentes mientras se explora mapa de salarios promedios anuales por industria.'},
        {'id': 3, 'name': 'Ventas Vehiculos Global', 'page': 'vehiculosventa_page', 'desc': 'Ventas de Vehiculos Global por Regiones y Año'},
        {'id': 4, 'name': 'Graficos Ventas Doble Eje', 'page': 'dobleeje_page', 'desc': 'Ventas Mensuales por Rubro: Objetivos vs Real'},
        {'id': 5, 'name': 'Expansion Startup Lavanderia', 'page': 'startupexpansion_page', 'desc': 'Expansion de una Lavanderia. Clustering: Agrupamiento de Obs por Variables (Ingreso Medio, Gasto Marketing y Poblacion)'}
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

