

from instrumento import instrumento

class percusion(instrumento):
    def __init__(self, nombre, nota):
        super().__init__(nombre)
        self.nota = nota

    def tocar(self):
        print(f"Tocando el {self.nombre} en la nota {self.nota}\n")