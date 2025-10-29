# contacto.py
class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}"


class Amigo(Contacto):
    def __init__(self, nombre, telefono, apodo):
        super().__init__(nombre, telefono)
        self.apodo = apodo

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Apodo: {self.apodo}"


class Familiar(Contacto):
    def __init__(self, nombre, telefono, parentesco):
        super().__init__(nombre, telefono)
        self.parentesco = parentesco

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Parentesco: {self.parentesco}"


class Trabajo(Contacto):
    def __init__(self, nombre, telefono, empresa):
        super().__init__(nombre, telefono)
        self.empresa = empresa

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Empresa: {self.empresa}"