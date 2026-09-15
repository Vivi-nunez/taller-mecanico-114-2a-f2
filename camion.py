# Importa la clase base Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Define la clase Camion que hereda de la clase base Vehiculo
class Camion(Vehiculo):
    # Método para retornar la tarifa por hora específica para un camión
    def tarifa_hora(self) -> int:
        return 40000