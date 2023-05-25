class Gato:
    def __init__(self, name, sex, age, weight, color, texture):
        self.name = name
        self.sex = sex
        self.age = age
        self.weight = weight
        self.color = color
        self.texture = texture

        mi_gato = Gato(name="Ariana", sex="Hembra", age=7, weight=4.5, color="calico", texture="Suave")

        print(mi_gato.name)
