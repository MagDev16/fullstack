from abc import ABC, abstractmethod
import math

# =============================================
# CLASE ABSTRACTA: Shape (Figura Geométrica)
# =============================================

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        """Adstract method to get the perimeter"""
        pass

    @abstractmethod
    def calculate_area(self):
        """Adstract method to get the area"""
        pass

# =============================================
# SUBCLASE: Circle (Círculo)
# =============================================
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius # radius of the circle

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius # perimeter = 2 * pi * radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2 # area = pi * radius^2

# =============================================
# SUBCLASE: Square (Cuadrado)
# =============================================
class Square(Shape):
    def __init__(self, side):
        self.side = side  # side of the square
    
    def calculate_perimeter(self):
        return 4 * self.side  # perimeter = 4 * side
    
    def calculate_area(self):
        return self.side ** 2  # area = side^2

# =============================================
# SUBCLASE: Rectangle (Rectángulo)
# =============================================
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  # length of the rectangle
        self.width = width    # width of the rectangle
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)  # perimeter = 2(length + width)
    
    def calculate_area(self):
        return self.length * self.width  # area = length * width

# =============================================
# DEMOSTRACIÓN
# ============================================= 
if __name__ == "__main__":
    #create figures
    circle = Circle(radius=5)
    square = Square(side=4)
    rectangle = Rectangle(length=3, width=6)

    print("\n🔍 Resultados:\n")
    #show results
    print(f"🔵 Círculo (radio = 5):")
    print(f" - Perímetro: {circle.calculate_perimeter():.2f}")
    print(f" - Área: {circle.calculate_area():.2f}\n")

    print(f"🟧 Cuadrado (lado = 4):")
    print(f" - Perímetro: {square.calculate_perimeter():.2f}")
    print(f" - Área: {square.calculate_area():.2f}\n")

    print(f"🟥🟥 Rectángulo (largo = 3, ancho = 6):")
    print(f" - Perímetro: {rectangle.calculate_perimeter():.2f}")
    print(f" - Área: {rectangle.calculate_area():.2f}\n")
    