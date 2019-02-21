class Empleado:
    def __init__ (self, nombre, familia_numerosa, pago, porcentaje = None):
        self.nombre = nombre
        self.familia_numerosa = familia_numerosa
        self.pago = pago
        self.porcentaje = porcentaje


    def get_nombre(self):
        return self.nombre

    def get_large_family(self):
        return self.familia_numerosa

    def get_pago(self):
        return self.pago

    def get_porcentaje(self):
        return self.porcentaje

    def bonificacion_total(self):
        return self.pago + (self.pago * self.porcentaje)


e1 = Empleado("Juan", "Si", 2300, 0.2)
print("Nombre:", e1.get_nombre(), "¿Familia numerosa?: ",e1.get_large_family())
print("Pago Normal:", e1.get_pago(), ", pago con bonificacion: ", e1.bonificacion_total())
