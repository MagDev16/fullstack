import csv  # Import the CSV module for reading/writing CSV files
import os   # Import the OS module for file operations
from student import Student  # Import the Student class

def export_csv(students):
    """
    Export student data to a CSV file.

    Args:
        students (list): List of Student objects.
    """
    # Check if there are any students to export
    if not students:
        print("No hay estudiantes registrados para exportatar.")
        return  # Added return to prevent trying to export empty data

    # Get filename from user and add .csv extension
    file_name = input("Ingrese el nomnre del archivo CSV (sin extension): ") + ".csv"
    
    try:
        # Open the file in write mode with proper encoding for Excel
        with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            # Define the field names (column headers)
            fieldnames = [
                "nombre",
                "seccion",
                "español",
                "ingles",
                "sociales",
                "ciencias"
            ]
            
            # Create a CSV writer with semicolon delimiter (works better with Excel)
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
            
            # Write the header row with column names
            writer.writeheader()
            
            # Convert Student objects to dictionaries and write to CSV
            student_dicts = [student.to_dict() for student in students]
            writer.writerows(student_dicts)

        print(f"Datos exportados correctamente a {file_name}")
        
    except Exception as e:
        print(f"Error al exportar datos: {e}")

def import_csv(students):
    """
    Import student data from a CSV file.

    Args:
        students (list): List of Student objects.

    Returns:
        list: List of imported Student objects.
    """
    # Get filename from user and add .csv extension
    file_name = input("ingrese el nombnre del archivo CSV a importar (sin extension): ") + ".csv"

    # Check if the file exists before attempting to read it
    if not os.path.exists(file_name):
        print("El archivo especificado no existe.")
        return []

    # Create a new list to store imported students
    imported_students = []
    
    try:
        # Open the file in read mode with proper encoding
        with open(file_name, mode="r", encoding="utf-8") as file:
            # Create a CSV reader with semicolon delimiter to match the export format
            reader = csv.DictReader(file, delimiter=';')
            
            # Process each row in the CSV file
            for row in reader:
                # Convert grade strings to float numbers
                row["español"] = float(row["español"])
                row["ingles"] = float(row["ingles"])
                row["sociales"] = float(row["sociales"])
                row["ciencias"] = float(row["ciencias"])
                
                # Convert dictionary to Student object and add to the list
                student = Student.from_dict(row)
                imported_students.append(student)

        print(f"Se importaron {len(imported_students)} estudiantes desde {file_name}")
        
    except Exception as e:
        print(f"Error al importar datos: {e}")
        return []
        
    return imported_students