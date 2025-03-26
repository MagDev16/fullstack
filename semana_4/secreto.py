import random

def adivinar_numero_secreto():
    numero_secreto = random.randint(1, 10)
    adivinanza = None

    while adivinanza != numero_secreto:
        adivinanza = int(input("Adivina el número secreto (entre 1 y 10): "))
        if adivinanza < numero_secreto:
            print("Muy bajo. Intenta nuevamente.")
        elif adivinanza > numero_secreto:
            print("Muy alto. Intenta nuevamente.")
        else:
            print("¡Felicidades! Adivinaste el número secreto.")

if __name__ == "__main__":
    adivinar_numero_secreto()