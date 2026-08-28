from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    numeros = []
    for numero in range(10):
        numeros.append(numero)
    return render_template("index.html", numeros = numeros)

if __name__ == "__main__":
    app.run(debug = True)