#-- Person class --#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#-- Bus class --#
class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = [] #-- list to store passengers --#
    #-- Add passangers --#
    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} se subio al bus.Pasajeros: {len(self.passengers)}/{self.max_passengers}")
        else:
            print(f"El bus esta lleno! {person.name} no se puede subir.")
    #-- Remove passangers --#
    def remove_passenger(self, person):
        if person in self.passengers:
            removed_person = self.passengers.pop(self.passengers.index(person))
            print(f"{removed_person.name} se bajó del bus. Pasajeros restantes: {len(self.passengers)}/{self.max_passengers}")
        else:
            print(f"{person.name} no se encuentra en el bus.")

#-- Usage --#
if __name__ == "__main__":
    school_bus = Bus(max_passengers=3)
    #--Passengers--#
    person1 = Person("Garcia", 37)
    person2 = Person("Arias", 60)
    person3 = Person("Sga", 30)
    person4 = Person("Gengar", 65)
    #--Add Passengers--#
    print("\n---Pasajeros Subiendo---")
    school_bus.add_passenger(person1)
    school_bus.add_passenger(person2)
    school_bus.add_passenger(person3)
    school_bus.add_passenger(person4)
    #-- Remove Passangers --#
    print("\n---Pasajeros Bajando---")
    school_bus.remove_passenger(person4)
    school_bus.remove_passenger(person3)
    school_bus.remove_passenger(person2)
    school_bus.remove_passenger(person1)
    
