# Importa la clase base Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Define la clase Auto que hereda de la clase base Vehiculo
class Auto(Vehiculo):
    # Método para retornar la tarifa por hora específica para un auto
    def tarifa_hora(self) -> int:
        return 30000