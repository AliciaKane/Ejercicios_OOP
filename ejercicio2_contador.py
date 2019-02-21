class Contador:
    def __init__ (self, numero):
        self.numero = numero

    def get_up(self):
        return self.numero + 1

    def get_down(self):
        return self.numero - 1

c1 = Contador(2)
c2 = Contador(5)
print("El numero inicial ha aumentado a:", c1.get_up())
print("El numero inicial a disminuido a:", c2.get_down())
