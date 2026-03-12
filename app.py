from flask import Flask, render_template, request
from pulp import *
app = Flask(__name__)

@app.route('/')
def home():
    return f'Welcome'

@app.route('/optimizacion', methods=['GET', 'POST'])
def modelo():
    if request.method == 'POST':
        madera=float(request.form.get("madera"))
        aluminio=float(request.form.get("aluminio"))

        ventanas=LpProblem("modelo_de_optimizacion", LpMaximize)
        x1= LpVariable("ventana_madera",0)
        x2= LpVariable("ventana_aluminio",0)

        ventanas += madera*x1 + aluminio*x2 #fo
        ventanas +=x1<=6 #r1
        ventanas +=x2<=4 #r2
        ventanas +=6*x1+8*x2<=48 #r3

        ventanas.solve()  #instruccion para resolver el modelo
        res1= x1.varValue
        res2= x2.varValue
        fo = ventanas.objective.value()

        return render_template("optimizacion.html", res1=res1, res2=res2, fo=fo)

    return render_template("optimizacion.html")
if __name__ == '__main__':
    app.run(debug=True)
