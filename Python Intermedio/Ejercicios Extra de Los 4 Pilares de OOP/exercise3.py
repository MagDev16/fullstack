class Vehicle:
    def __init__(self, brand: str, year: int):
        self._brand = brand
        self._year = year
        
    def get_info(self) -> str:
        # Devuelve la info del vehiculo en formato "Marco(año)"
        return f"{self._brand} ({self._year})"
    
class Car(Vehicle):
    def __init__(self, brand: str, year: int, doors: int):
        super().__init__(brand, year)
        self.doors = doors
        
    def get_info(self) -> str:
        return f"{super().get_info()} - {self.doors} puertas"
    
class Motorcycle(Vehicle):
    def __init__(self, brand: str, year: int, vehicle_type: str):
        super().__init__(brand, year)
        self.type = vehicle_type
        
    def get_info(self) -> str:
        return f"{super().get_info()} - Tipo de moto: {self.type}"
    
class Bus(Vehicle):
    def __init__(self, brand: str, year: int, decks: int, internet_type: str):
        super().__init__(brand, year)
        self.decks = decks
        self.internet_type = internet_type
        
    def get_info(self) -> str:
        return f"{super().get_info()} - {self.decks} pisos - Internet: {self.internet_type}"

# --- Caso de Uso --- #

vehicle1 = Car("Subaru", 2015, 4)
vehicle2 = Motorcycle("Freedom", 2026, "Doble proposito")
vehicle3 = Bus("Volvo", 2020, 2, "WiFi")

print(vehicle1.get_info())
print(vehicle2.get_info())
print(vehicle3.get_info())

