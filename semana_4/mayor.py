def encontrar_mayor(numero_uno, numero_dos, numero_tres):
    mayor = numero_uno
    if numero_dos > mayor:
        mayor = numero_dos
    if numero_tres > mayor:
        mayor = numero_tres
    return mayor

def main():
    numero_uno = float(input("Ingresa el primer número: "))
    numero_dos = float(input("Ingresa el segundo número: "))
    numero_tres = float(input("Ingresa el tercer número: "))

    mayor = encontrar_mayor(numero_uno, numero_dos, numero_tres)

    print(f"El mayor de los tres números es: {mayor:.0f}")

if __name__ == "__main__":
    main()
