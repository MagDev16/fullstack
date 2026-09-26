# Import functions from the actions module that handle student data operations
from actions import (
    add_students,
    show_students,
    top3_students,
    overall_average
)

# Import functions from the data module for CSV file operations
from data import export_csv, import_csv

def show_main_menu(students):
    """
    Display the main menu and handle user input for student data operations.

    Args:
        students (list): List of student dictionaries.
    """
    # Main program loop that continues until user chooses to exit
    while True:
        # Display menu options to the user
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ingresar información de estudiantes")
        print("2. Ver información de todos los estudiantes")
        print("3. Ver top 3 estudiantes con mejor promedio")
        print("4. Ver nota promedio general")
        print("5. Exportar datos a CSV")
        print("6. Importar datos desde CSV")
        print("7. Salir")

        # Get user input for menu selection
        option = input("Selecciones una opción (1-7): ")

        # Process the user's selection
        if option  == "1":
            add_students(students)  # Add new students to the list
        elif option == "2":
            show_students(students)  # Display all student information
        elif option == "3":
            top3_students(students)  # Show top 3 students by average grade
        elif option == "4":
            overall_average(students)  # Calculate and display overall average grade
        elif option == "5":
            export_csv(students)  # Save student data to CSV file
        elif option == "6":
            students.extend(import_csv(students))  # Load student data from CSV file
        elif option == "7":
            print("Saliendo del programa...")  # Exit the program
            break
        else:
            # Handle invalid input
            print("Opción inválida. Por favor, seleccione una opción válida (1-7).")