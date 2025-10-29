# main.py
from contacto import Amigo, Familiar, Trabajo
from contacto_dao_sqlserver import ContactoDAO
import pyodbc
dao = ContactoDAO()
print("Conexion establecida con SQL Server")

dao.agregar_contacto(Amigo("Luis", "555-1234", "Lu"))
dao.agregar_contacto(Familiar("Ana", "555-5678", "Hermana"))
dao.agregar_contacto(Trabajo("Carlos", "555-9012", "TechCorp"))

for contacto in dao.listar_contactos():
    print(contacto.mostrar_info())
    
print("\n Buscando a Ana:")
contacto = dao.buscar_contacto("Ana")
if contacto:
    print(contacto.mostrar_info())
else:
    print("No se encontró el contacto.")
    
print("\n Eliminando a Luis...")
dao.eliminar_contacto("Luis")

print("Lista actualizada:")
for contacto in dao.listar_contactos():
    print(contacto.mostrar_info())
    
    

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=PC-ALEX;"
    "DATABASE=agenda;"
    "UID=sa;"
    "PWD=123456"
)
cursor = conn.cursor()

try:
    cursor.execute(
        "INSERT INTO contacto (nombre, telefono, tipo, extra) VALUES (?, ?, ?, ?)",
        ("PruebaManual", "999-9999", "amigo", "Test")
    )
    conn.commit()
    print("✅ Inserción manual exitosa")
except Exception as e:
    print("❌ Error en inserción manual:", e)

conn.close()