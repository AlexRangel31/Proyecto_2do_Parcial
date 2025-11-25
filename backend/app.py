from flask import Flask, request, jsonify
from contacto import Amigo, Familiar, Trabajo
from contacto_dao_sqlserver import ContactoDAO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # Permite que el frontend acceda al backend
dao = ContactoDAO()

@app.get("/contactos")
def obtener_contactos():
    contactos = [c.__dict__ for c in dao.listar_contactos()]
    return jsonify(contactos)

@app.post("/contactos")
def agregar_contacto():
    data = request.json
    tipo = data["tipo"]

    if tipo == "amigo":
        contacto = Amigo(data["nombre"], data["telefono"], data["extra"])
    elif tipo == "familiar":
        contacto = Familiar(data["nombre"], data["telefono"], data["extra"])
    elif tipo == "trabajo":
        contacto = Trabajo(data["nombre"], data["telefono"], data["extra"])

    dao.agregar_contacto(contacto)
    return jsonify({"mensaje": "Contacto agregado"}), 201

@app.delete("/contactos/<nombre>")
def eliminar_contacto(nombre):
    dao.eliminar_contacto(nombre)
    return jsonify({"mensaje": "Contacto eliminado"})
    
if __name__ == "__main__":
    app.run(debug=True)
