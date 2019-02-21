import unittest
class Complejo(object):
    def __init__(self, real = None, imagen = None):
        self.real = real
        self.imagen = imagen

    def sumar (self, otro):
        result = Complejo (self.real + otro.real, self.imagen + otro.imagen)
        return result

    def resta (self, otro):
        result = Complejo (self.real - otro.real, self.imagen - otro.imagen)
        return result

    def multiplicar (self, otro):
        result = Complejo ((self.real*otro.real) - (self.imagen*otro.imagen), (self.real*otro.imagen) + (otro.real + self.imagen))
        return result
    def dividir(self, otro):
        result = Complejo(((self.real*otro.real)+(self.imagen*otro.imagen))+((self.imagen*otro.real)-(self.real*otro.imagen))/((otro.real)**2 + (otro.imagen)**2))
                            #a      *    c     +      b      *      d     +      
        return result

    def igual(self, otro):
        return self.real == otro.real and self.imagen == self.imagen

class TestComplejo(unittest.TestCase):
    def test_sumar(self):
        c1 = Complejo(1,2)
        c2 = Complejo(3,4)

        suma = c1.sumar(c2)

        self.assertEqual(suma.real, 4)
        self.assertEqual(suma.imagen, 6)

    def test_restar(self):
        c1 = Complejo(6,1)
        c2 = Complejo(8,4)

        restar = c1.resta(c2)

        self.assertEqual(restar.real, -2)
        self.assertEqual(restar.imagen, -3)

    def test_multiplicar(self):
        c1 = Complejo(3,5)
        c2 = Complejo(1,2)

        multiplicar = c1.multiplicar(c2)

        self.assertEqual(multiplicar.real, -7)
        self.assertEqual(multiplicar.imagen, 12)

    def test_dividir(self):
        c1 = Complejo(3.0,5.0)
        c2 = Complejo(1.0,2.0)

        dividir = c1.dividir(c2)

        self.assertEqual(dividir.real, 13/5)
        self.assertEqual(dividir.imagen, -1/5)

if __name__ == "__main__":
    unittest.main()
