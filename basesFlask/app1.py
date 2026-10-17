from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    titulo = "Pagina de inicio"
    listado = ['Pythom', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template("index.html", titulo=titulo, listado=listado)

#@app.route("/")#decorador o ruta
#def index ():
 #   return "<h1> Hola Mundo </h1>"

@app.route("/operasbas", methods=["GET", "POST"])
def operasbas():
    n1 = 0
    n2 = 0
    res = 0
    operacion = ''
    if request.method == 'POST':
       
        n1 = request.form.get('n1') or 0
        n2 = request.form.get('n2') or 0
        operacion = request.form.get('operacion')
        
        if operacion == 'sumar':
            res = float(n1) + float(n2)
        elif operacion == 'restar':
            res = float(n1) - float(n2)
        elif operacion == 'multiplicar':
            res = float(n1) * float(n2)

    return render_template('operasbas.html', n1=n1, n2=n2, res=res)

@app.route("/distancia")
def distancia():
    return render_template('distancia.html')

@app.route("/hola")
def hola():
    return "<h1> Hola PWA - IEVN1003</h1>"

#COMO PASAR PARAMETROS POR URL
@app.route("/user/<string:nom>")
def user(nom):
    return "<h1>Hola User: {} </h1>".format(nom)

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1, n2):
    return "la suma es: {}".format(n1 + n2)

if __name__ == "__main__":
    app.run(debug=True)