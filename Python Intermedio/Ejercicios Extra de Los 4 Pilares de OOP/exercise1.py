class Employee:
    #class constructor
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value
        
    @property
    def salary(self) -> float:
        return self._salary
    
    @salary.setter
    def salary(self, value: float):
        if value < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._salary = value
    
    def promote(self, percentage: float):
        if percentage < 0:
            raise ValueError("El porcentaje de promocion no puede ser negativo.")
        self.salary += self.salary * percentage
        
# --- Caso de Uso --- #
if __name__ == "__main__":
    employee = Employee("Manuel", 420000)
    
    employee.promote(0.1) #Aumento del 10%
    
    print(employee.name)
    print(employee.salary) # Salario actualizado después de la promoción