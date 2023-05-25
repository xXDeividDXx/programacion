class Animal:
    def __init__(self, id:int, nombre:str, especie:str):
        self.id=id
        self.nombre=nombre
        self.especie=especie

    def se_mueve(self):
        print(f"{self.nombre} se mueve...")    