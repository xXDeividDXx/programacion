
# Integrantes del grupo:
#   - David Inostroza
#   - Sergei Igor
#   - Mauricio Huenchuan

from os import system

from instrumento import instrumento
from cuerda import cuerda
from viento import viento
from percusion import percusion

if __name__ == "__main__":
    
    system("cls")

    instrumento = instrumento("\nInstrumentos\n")
    print(instrumento.getNombre())


    cuerda = cuerda("Guitarra", "La")
    print(cuerda.getNombre())
    cuerda.tocar()


    viento = viento("Flauta", "Do")
    print(viento.getNombre())
    viento.tocar()

    percusion = percusion("Xilofono", "Mi")
    print(percusion.getNombre())
    percusion.tocar()


print("\nQue tenga un buen dia.\n")