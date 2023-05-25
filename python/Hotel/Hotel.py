class Hotel:
    
    def __init__(self, nombre, ubicacion, cantidad_habitaciones):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.cantidad_habitaciones = cantidad_habitaciones
        self.reservas = []
        
    def mostrar_disponibilidad(self):
        print(f"El hotel {self.nombre} tiene {self.cantidad_habitaciones - len(self.reservas)} habitaciones disponibles.")
        
    def hacer_reserva(self, reserva):
        if len(self.reservas) < self.cantidad_habitaciones:
            self.reservas.append(reserva)
            print(f"Reserva para {reserva.nombre} en {self.nombre} confirmada.")
        else:
            print(f"No hay habitaciones disponibles en {self.nombre} para las fechas solicitadas.")


