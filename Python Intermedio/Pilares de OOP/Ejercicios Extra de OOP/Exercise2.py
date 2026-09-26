class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Hace un sonido"


class Dog(Animal):
    def speak(self):
        return "Guau"


class Cat(Animal):
    def speak(self):
        return "Miau"


def main():
    dog = Dog("Firulais")
    cat = Cat("Michi")
    animal = Animal("Genérico")
    print(dog.speak())     # Guau
    print(cat.speak())     # Miau
    print(animal.speak())  # Hace un sonido


if __name__ == "__main__":
    main()
