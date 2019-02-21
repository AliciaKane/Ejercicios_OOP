class Cuenta:
    def __init__(self, dinero):
        self.dinero = dinero

    def get_ingreso(self, meter):
        self.meter = meter
        return self.dinero + self.meter

    def get_reintegro(self, sacar):
        self.sacar = sacar
        return self.dinero - self.sacar

    def get_transferencia(self, transferencia):
        self.transferencia = transferencia #Hay que escribir el argumento!
        return self.transferencia #Tambien podria porner self.sacar,
                             #porque es el dinero que se mueve.


pago = Cuenta(2000)
print(pago.get_ingreso(200), pago.get_reintegro(50), pago.get_transferencia(75))
#QUE NO SE TE OLVIDEN LOS PAREBNTESIS DUMM!!
