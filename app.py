#librerias descargadas
from flask import Flask, render_template, request, redirect, session, url_for


app = Flask(__name__)
app.secret_key="develoteca"

#Ruta para el inicio de sesión
@app.route("/") 
def temp():
    return render_template("index.html")


@app.route("/", methods=["POST"])  
def admin_login_post():
    _usuario=request.form["txtUsuario"]
    _password=request.form["txtPassword"]

    if _usuario == "admin" and _password == "12345":

        session["login"]=True
        session["usuario"]="Administrador"
        return redirect("/principal/")
    
    return render_template("index.html")

#Ruta para la pagina principal
@app.route("/principal/")
def admin():
    return render_template("admin/principal.html")

#Ruta para la pagina de armado de verduras
@app.route("/verduras/")  
def verduras():
    return render_template("despensas/verduras.html")

#Ruta para la pagina de armado de abarrotes
@app.route("/abarrotes/")  
def abarrotes():
    return render_template("despensas/abarrotes.html")



if __name__ == "__main__" :
    app.run(debug=True)



