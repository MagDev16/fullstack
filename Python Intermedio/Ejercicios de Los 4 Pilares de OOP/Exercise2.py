from abc import ABC, abstractmethod
import math

# Abstract class Shape with abstract methods area and perimeter
class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        """Calcula y retoma el area de la figura"""
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """Calcula y retoma el perimetro de la figura"""
        pass
    
#Circle class that inherits from Shape
class Circle(Shape):
    
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.radius = radius
        
    def calculate_area(self) -> float:
        """Calcula y retoma el area del circulo"""
        return math.pi * (self.radius ** 2)
    
    def calculate_perimeter(self) -> float:
        """Calcula y retoma el perimetro del circulo"""
        return 2 * math.pi * self.radius

#square class that inherits from Shape
class Square(Shape):
    
    def __init__(self, side_length: float):
        if side_length <= 0:
            raise ValueError("La longitud del lado debe ser un número positivo.")
        self.side_length = side_length
        
    def calculate_area(self) -> float:
        """Calcula y retoma el area del cuadrado"""
        return self.side_length ** 2
    
    def calculate_perimeter(self) -> float:
        """Calcula y retoma el perimetro del cuadrado"""
        return 4 * self.side_length
    
#Rectangle class that inherits from Shape
class Rectangle(Shape):
    
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("El ancho y la altura deben ser números positivos.")
        self.width = width
        self.height = height
        
    def calculate_area(self) -> float:
        """Calcula y retoma el area del rectangulo"""
        return self.width * self.height
    
    def calculate_perimeter(self) -> float:
        """Calcula y retoma el perimetro del rectangulo"""
        return 2 * (self.width + self.height)
    
#ejemplo de uso
if __name__ == "__main__":
    circle = Circle(5)
    print(f"Circle Area: {circle.calculate_area()}")
    print(f"Circle Perimeter: {circle.calculate_perimeter()}")

    square = Square(4)
    print(f"Square Area: {square.calculate_area()}")
    print(f"Square Perimeter: {square.calculate_perimeter()}")

    rectangle = Rectangle(3, 6)
    print(f"Rectangle Area: {rectangle.calculate_area()}")
    print(f"Rectangle Perimeter: {rectangle.calculate_perimeter()}")