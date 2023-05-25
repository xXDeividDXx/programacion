from Hotel import Hotel
from Reserva import Reserva

def main():
    # Crear una instancia de la clase Hotel
    mi_hotel = Hotel("Hotel Ejemplo", "Ciudad Ejemplo", 10)

    # Mostrar la disponibilidad del hotel
    mi_hotel.mostrar_disponibilidad()

    # Solicitar información al usuario para crear una reserva
    nombre = input("Ingrese su nombre: ")
    fecha_entrada = input("Ingrese la fecha de entrada (dd/mm/aaaa): ")
    fecha_salida = input("Ingrese la fecha de salida (dd/mm/aaaa): ")
    num_habitaciones = int(input("Ingrese el número de habitaciones que desea reservar: "))

    # Crear una instancia de la clase Reserva
    mi_reserva = Reserva(nombre, fecha_entrada, fecha_salida, num_habitaciones)

    # Intentar hacer la reserva en el hotel
    mi_hotel.hacer_reserva(mi_reserva)

    # Mostrar la disponibilidad actualizada del hotel
    mi_hotel.mostrar_disponibilidad()

if __name__ == "__main__":
    main()
