# Integracion de los otros dos scripts en el archivo app.py:

from flask import Flask, render_template, request
from scrapping_abc import busqueda_abc
from scrapping_cocinatis import busqueda_cocinatis

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recetas_abc = []
    recetas_cocinatis = []
    if request.method == "POST":
        ingrediente = request.form.get("ingrediente")
        if ingrediente:
            recetas_abc = busqueda_abc(ingrediente)
            recetas_cocinatis = busqueda_cocinatis(ingrediente)
    return render_template("index.html", recetas_abc=recetas_abc, recetas_cocinatis=recetas_cocinatis)

if __name__ == "__main__":
    app.run(debug=True)
