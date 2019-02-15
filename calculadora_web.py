from flask import Flask
from flask import render_template
from calculadora import Calculadora
from flask import request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def inicio():
    resultado = None
    if request.method == 'POST':
        primer_numero = float(request.form['primer_numero'])
        segundo_numero = float(request.form['segundo_numero'])
        comando = request.form['comando']
        calc = Calculadora(primer_numero, segundo_numero, comando)
        resultado = calc.calcular()
    return render_template("index.html", resultado=resultado)











@app.route("/about")
def get_about():
    return "Esta es la pagina donde hablas de la calculadora y tus experiencias sexuales."
