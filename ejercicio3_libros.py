class Libro:
    def __init__(self, book):
        self.book = book

    def get_book(self):
        return self.book

    def get_back_book(self):
        return self.book

    def get_info_book(self):
        return self.book


l1 = Libro("Harry Potter")
l2 = Libro("Los Juegos del Hambre")
l3 = Libro("Elegida por la Luna")


print ("El libro", l1.get_book(), "ha sido tomado prestado")
print ("El libro", l2.get_back_book(), "ha sido devuelto")
print ("El libro", l3.get_info_book(), "trata de...")
