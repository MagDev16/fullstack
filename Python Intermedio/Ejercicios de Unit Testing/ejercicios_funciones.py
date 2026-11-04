# 3. Suma de todos los números de una lista
def sumar_lista(lista):
    return sum(lista)


# 4. Dar la vuelta a un string
def invertir_string(texto):
    return texto[::-1]


# 5. Contar mayúsculas y minúsculas en un string
def contar_mayus_minus(texto):
    mayusculas = sum(1 for c in texto if c.isupper())
    minusculas = sum(1 for c in texto if c.islower())
    return f"There's {mayusculas} upper cases and {minusculas} lower cases"


# 6. Ordenar palabras separadas por guion alfabéticamente
def ordenar_palabras_guion(texto):
    palabras = texto.split("-")
    palabras_ordenadas = sorted(palabras)
    return "-".join(palabras_ordenadas)


# 7. Filtrar números primos de una lista
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def obtener_primos(lista):
    return [num for num in lista if es_primo(num)]