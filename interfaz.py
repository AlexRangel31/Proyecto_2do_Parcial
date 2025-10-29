import tkinter as tk
from tkinter import messagebox
from contacto import Amigo, Familiar, Trabajo
from contacto_dao_sqlserver import ContactoDAO

dao = ContactoDAO()

def agregar_contacto():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    tipo = tipo_var.get()
    extra = entry_extra.get()

    if not nombre or not telefono or not extra:
        messagebox.showwarning("Campos incompletos", "Por favor llena todos los campos.")
        return

    if tipo == "amigo":
        contacto = Amigo(nombre, telefono, extra)
    elif tipo == "familiar":
        contacto = Familiar(nombre, telefono, extra)
    elif tipo == "trabajo":
        contacto = Trabajo(nombre, telefono, extra)

    dao.agregar_contacto(contacto)
    listar_contactos()
    messagebox.showinfo("Éxito", f"Contacto '{nombre}' agregado.")

def listar_contactos():
    lista.delete(0, tk.END)
    for contacto in dao.listar_contactos():
        lista.insert(tk.END, contacto.mostrar_info())

def eliminar_contacto():
    nombre = entry_nombre.get()
    if not nombre:
        messagebox.showwarning("Nombre requerido", "Ingresa el nombre a eliminar.")
        return
    dao.eliminar_contacto(nombre)
    listar_contactos()
    messagebox.showinfo("Eliminado", f"Contacto '{nombre}' eliminado.")

# Interfaz
ventana = tk.Tk()
ventana.title("Agenda de Contactos")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Teléfono:").grid(row=1, column=0)
entry_telefono = tk.Entry(ventana)
entry_telefono.grid(row=1, column=1)

tk.Label(ventana, text="Tipo:").grid(row=2, column=0)
tipo_var = tk.StringVar(value="amigo")
tk.OptionMenu(ventana, tipo_var, "amigo", "familiar", "trabajo").grid(row=2, column=1)

tk.Label(ventana, text="Extra:").grid(row=3, column=0)
entry_extra = tk.Entry(ventana)
entry_extra.grid(row=3, column=1)

tk.Button(ventana, text="Agregar", command=agregar_contacto).grid(row=4, column=0)
tk.Button(ventana, text="Eliminar", command=eliminar_contacto).grid(row=4, column=1)

lista = tk.Listbox(ventana, width=50)
lista.grid(row=5, column=0, columnspan=2)

listar_contactos()
ventana.mainloop()