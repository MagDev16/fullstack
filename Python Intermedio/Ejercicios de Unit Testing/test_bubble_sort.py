# ==============================================================================
# ARCHIVO DE UNIT TESTS
# ==============================================================================
from bubble_sort import bubble_sort
import unittest

class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort_small_list(self):
        # 1. Funciona con una lista pequeña
        # Arrange
        numbers = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]

        # Act
        result = bubble_sort(numbers)

        # Assert
        self.assertEqual(result, expected)

    def test_bubble_sort_large_list(self):
        # 2. Funciona con una lista grande (más de 100 elementos)
        # Arrange: Generamos una lista desordenada de 150 elementos
        large_list = list(range(150, 0, -1))
        expected_sorted = list(range(1, 151))

        # Act
        result = bubble_sort(large_list)

        # Assert
        self.assertEqual(result, expected_sorted)

    def test_bubble_sort_empty_list(self):
        # 3. Funciona con una lista vacía
        # Arrange
        empty_list = []

        # Act
        result = bubble_sort(empty_list)

        # Assert
        self.assertEqual(result, [])

    def test_bubble_sort_invalid_parameter(self):
        # 4. No funciona con parámetros que no sean una lista (lanza TypeError)
        # Arrange
        invalid_param = "esto_es_un_string"

        # Act & Assert
        with self.assertRaises(TypeError):
            bubble_sort(invalid_param)


if __name__ == "__main__":
    unittest.main()