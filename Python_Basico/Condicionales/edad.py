def clasificar_edad(edad):
    if edad < 2:
        return "bebé"
    elif 2 <= edad <= 12:
        return "niño"
    elif 13 <= edad <= 19:
        return "preadolescente"  if edad < 15 else "adolescente"
    elif 20 <= edad <= 35:
        return "adulto joven"
    elif 36 <= edad <= 60:
        return "adulto"
    else:
        return "adulto mayor"

def main():
    nombre = input("Por favor, ingrese su nombre: ")
    apellido = input("Por favor, ingrese su apellido: ")
    edad = int(input("Por favor, ingrese su edad: "))

    clasificacion = clasificar_edad(edad)

    print(f"{nombre} {apellido}, tienes {edad} años y eres un {clasificacion}.")

if __name__ == "__main__":
    main()
