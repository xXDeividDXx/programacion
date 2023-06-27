from Habitacion import Habitacion
from Reserva import Reserva
from Cliente import Cliente

def main():
    mi_habitacion = Habitacion(10,4)

    Cliente.nombre = input("Hola, Ingrese su nombre: ")
    Cliente.rut = input("Ingrese su RUT: ")
    Reserva.fecha_entrada = input("Ingrese la fecha de entrada (dd/mm/aaaa): ")
    Reserva.fecha_salida = input("Ingrese la fecha de salida (dd/mm/aaaa): ")

    print("Hay " + str(Habitacion.cantidad_habitaciones) + " habitaciones disponibles")
    print("con capacidad para " +str(Habitacion.capacidad)+(" en cada una."))
    Reserva.num_habitacion = input("Ingrese cuantas habitaciones desea reserva: ")
    Reserva.num_personas = input("Ingrese cuantas personas van a alojar: ")
    