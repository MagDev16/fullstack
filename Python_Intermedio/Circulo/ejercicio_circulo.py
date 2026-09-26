import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

#--ask user for radiu--#
while True:
    try:
        user_radius = float(input("Ingrese el radio del circulo: "))
        if user_radius <= 0:
            print("EL radio debe de ser positivo.")
        else:
            break
    except ValueError:
        print("Ingrese un valor numerico valido.")

#--Build the circle and show the area --#
user_circle = Circle(user_radius)
print(f"\nEl Área del circulo con radio {user_radius}: {user_circle.get_area():.2f}")