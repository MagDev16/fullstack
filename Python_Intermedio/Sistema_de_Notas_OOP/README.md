# Sistema de Gestión de Notas de Estudiantes

## Descripción
Este proyecto es un sistema de gestión de notas de estudiantes que permite registrar, visualizar y analizar el rendimiento académico de los estudiantes en diferentes materias.

## Características
- Registro de estudiantes con sus datos personales y calificaciones
- Visualización de la información de todos los estudiantes
- Identificación de los 3 mejores estudiantes según su promedio
- Cálculo del promedio general de todos los estudiantes
- Exportación e importación de datos en formato CSV

## Estructura del Proyecto
- `main.py`: Punto de entrada de la aplicación
- `menu.py`: Implementación del menú principal y manejo de opciones
- `actions.py`: Funciones para realizar operaciones con los datos de estudiantes
- `data.py`: Funciones para importar y exportar datos desde/hacia archivos CSV
- `student.py`: Definición de la clase Student para representar a los estudiantes

## Implementación Orientada a Objetos
El sistema utiliza la clase `Student` para representar a cada estudiante, en lugar de usar diccionarios. Esto proporciona una estructura más organizada y facilita la implementación de métodos específicos para cada estudiante, como el cálculo de su promedio.