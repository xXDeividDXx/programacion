

from instrumento import instrumento

class cuerda(instrumento):
    def __init__(self, nombre, nota):
        super().__init__(nombre)
        self.nota = nota

    def tocar(self):
        print(f"Tocando la {self.nombre} en la nota {self.nota}\n")