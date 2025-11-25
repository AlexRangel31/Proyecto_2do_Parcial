# contacto_dao.py
class ContactoDAO:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def eliminar_contacto(self, nombre):
        self.contactos = [c for c in self.contactos if c.nombre != nombre]

    def buscar_contacto(self, nombre):
        return next((c for c in self.contactos if c.nombre == nombre), None)

    def listar_contactos(self):
        return self.contactos