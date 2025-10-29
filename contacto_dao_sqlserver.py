import pyodbc
from contacto import Amigo, Familiar, Trabajo

class ContactoDAO:
    def __init__(self):
        self.conn = pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=PC-ALEX;"
            "DATABASE=agenda;"
            "UID=sa;"
            "PWD=123456"
        )
        self.cursor = self.conn.cursor()

    def agregar_contacto(self, contacto):
        print("Agregando:", contacto.mostrar_info())
        tipo = contacto.__class__.__name__.lower()
        extra = getattr(contacto, 'apodo', None) or getattr(contacto, 'parentesco', None) or getattr(contacto, 'empresa', None)
        sql = "INSERT INTO contacto (nombre, telefono, tipo, extra) VALUES (?, ?, ?, ?)"
        try:
            self.cursor.execute(sql, (contacto.nombre, contacto.telefono, tipo, extra))
            self.conn.commit()
            print("✅ Commit ejecutado")
        except Exception as e:
            print("❌ Error al agregar contacto:", e)

    def eliminar_contacto(self, nombre):
        sql = "DELETE FROM contacto WHERE nombre = ?"
        self.cursor.execute(sql, (nombre,))
        self.conn.commit()

    def buscar_contacto(self, nombre):
        sql = "SELECT nombre, telefono, tipo, extra FROM contacto WHERE nombre = ?"
        self.cursor.execute(sql, (nombre,))
        row = self.cursor.fetchone()
        return self._crear_contacto(row) if row else None

    def listar_contactos(self):
        self.cursor.execute("SELECT nombre, telefono, tipo, extra FROM contacto")
        return [self._crear_contacto(row) for row in self.cursor.fetchall()]

    def _crear_contacto(self, row):
        nombre, telefono, tipo, extra = row
        if tipo == 'amigo':
            return Amigo(nombre, telefono, extra)
        elif tipo == 'familiar':
            return Familiar(nombre, telefono, extra)
        elif tipo == 'trabajo':
            return Trabajo(nombre, telefono, extra)

# Inicialización para pruebas
dao = ContactoDAO()
print("✅ Conexión establecida con SQL Server")