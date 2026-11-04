import unittest
from ejercicios_funciones import (
    sumar_lista,
    invertir_string,
    contar_mayus_minus,
    ordenar_palabras_guion,
    obtener_primos,
)


class TestEjerciciosFunciones(unittest.TestCase):

    # ==========================================
    # TESTS EJERCICIO 3: Suma de una lista
    # ==========================================
    def test_sumar_lista_caso_1(self):
        # Arrange
        lista = [4, 6, 2, 29]
        esperado = 41

        # Act
        resultado = sumar_lista(lista)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_sumar_lista_caso_2(self):
        # Arrange
        lista = [10, 20, 30, 40]
        esperado = 100

        # Act
        resultado = sumar_lista(lista)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_sumar_lista_caso_3(self):
        # Arrange
        lista = [-5, 5, 10]
        esperado = 10

        # Act
        resultado = sumar_lista(lista)

        # Assert
        self.assertEqual(resultado, esperado)

    # ==========================================
    # TESTS EJERCICIO 4: Invertir un string
    # ==========================================
    def test_invertir_string_caso_1(self):
        # Arrange
        texto = "Hola mundo"
        esperado = "odnum aloH"

        # Act
        resultado = invertir_string(texto)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_invertir_string_caso_2(self):
        # Arrange
        texto = "Python"
        esperado = "nohtyP"

        # Act
        resultado = invertir_string(texto)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_invertir_string_caso_3(self):
        # Arrange
        texto = "12345"
        esperado = "54321"

        # Act
        resultado = invertir_string(texto)

        # Assert
        self.assertEqual(resultado, esperado)

    # ==========================================
    # TESTS EJERCICIO 5: Contar mayús/minús
    # ==========================================
    def test_contar_mayus_minus_caso_1(self):
        # Arrange
        texto = "I love Nación Sushi"
        esperado = "There's 3 upper cases and 13 lower cases"

        # Act
        resultado = contar_mayus_minus(texto)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_contar_mayus_minus_caso_2(self):
        # Arrange
        texto = "Hola Mundo"
        esperado = "There's 2 upper cases and 7 lower cases"

        # Act
        resultado = contar_mayus_minus(texto)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_contar_mayus_minus_caso_3(self):
        # Arrange
        texto = "PYTHON"
        esperado = "There's 6 upper cases and 0 lower cases"

        # Act
        resultado = contar_mayus_minus(texto)

        # Assert
        self.assertEqual(resultado, esperado)

    # ==========================================
    # TESTS EJERCICIO 6: Ordenar por guiones
    # ==========================================
    def test_ordenar_palabras_guion_caso_1(self):
        # Arrange
        texto = "python-variable-funcion-computadora-monitor"
        esperado = "computadora-funcion-monitor-python-variable"

        # Act
        resultado = ordenar_palabras_guion(texto)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_ordenar_palabras_guion_caso_2(self):
        # Arrange
        texto = "c-a-b"
        esperado = "a-b-c"

        # Act
        resultado = ordenar_palabras_guion(texto)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_ordenar_palabras_guion_caso_3(self):
        # Arrange
        texto = "zanahoria-manzana-banano"
        esperado = "banano-manzana-zanahoria"

        # Act
        resultado = ordenar_palabras_guion(texto)

        # Assert
        self.assertEqual(resultado, esperado)

    # ==========================================
    # TESTS EJERCICIO 7: Filtrar números primos
    # ==========================================
    def test_obtener_primos_caso_1(self):
        # Arrange
        lista = [1, 4, 6, 7, 13, 9, 67]
        esperado = [7, 13, 67]

        # Act
        resultado = obtener_primos(lista)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_obtener_primos_caso_2(self):
        # Arrange
        lista = [2, 3, 5, 10, 12]
        esperado = [2, 3, 5]

        # Act
        resultado = obtener_primos(lista)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_obtener_primos_caso_3(self):
        # Arrange
        lista = [11, 14, 17, 20, 23]
        esperado = [11, 17, 23]

        # Act
        resultado = obtener_primos(lista)

        # Assert
        self.assertEqual(resultado, esperado)


if __name__ == "__main__":
    unittest.main()