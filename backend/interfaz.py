from flask import Flask, request, redirect, render_template_string
from contacto import Amigo, Familiar, Trabajo
from contacto_dao_sqlserver import ContactoDAO

app = Flask(__name__)
dao = ContactoDAO()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Agenda de Contactos</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        input, select { padding: 8px; margin: 4px; width: 250px; }
        button { padding: 10px 20px; margin: 5px; }
        .contact-list { margin-top: 20px; }
        .item { background: #f2f2f2; padding: 10px; margin: 5px 0; }
    </style>
</head>
<body>
    <h1>Agenda de Contactos</h1>
    <form method="POST" action="/agregar">
        <input type="text" name="nombre" placeholder="Nombre">
        <br>
        <input type="text" name="telefono" placeholder="Teléfono">
        <br>
        <select name="tipo">
            <option value="amigo">Amigo</option>
            <option value="familiar">Familiar</option>
            <option value="trabajo">Trabajo</option>
        </select>
        <br>
        <input type="text" name="extra" placeholder="Extra">
        <br>
        <button type="submit">Agregar</button>
    </form>

    <form method="POST" action="/eliminar">
        <input type="text" name="nombre" placeholder="Nombre a eliminar">
        <button type="submit" style="background:#d9534f; color:white;">Eliminar</button>
    </form>

    <div class="contact-list">
        <h2>Contactos</h2>
        {% for c in lista %}
            <div class="item">{{ c }}</div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    contactos = [c.mostrar_info() for c in dao.listar_contactos()]
    return render_template_string(HTML, lista=contactos)

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    tipo = request.form.get("tipo")
    extra = request.form.get("extra")

    if not nombre or not telefono or not extra:
        return "Faltan campos", 400

    if tipo == "amigo":
        contacto = Amigo(nombre, telefono, extra)
    elif tipo == "familiar":
        contacto = Familiar(nombre, telefono, extra)
    elif tipo == "trabajo":
        contacto = Trabajo(nombre, telefono, extra)

    dao.agregar_contacto(contacto)
    return redirect("/")

@app.route("/eliminar", methods=["POST"])
def eliminar():
    nombre = request.form.get("nombre")
    if not nombre:
        return "Nombre requerido", 400
    dao.eliminar_contacto(nombre)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
