from student import Student

def add_students(students):
    """
    Add students to the list.

    Args:
        students (list): List of Student objects.
    """

    # Ask user how many students they want to add
    n = int(input("Cuantos estudiantes desea ingresar? "))
    # Loop n times to collect data for each student (using _ as a throwaway variable since we don't need the loop counter)
    for _ in range(n):
        # Display a prompt showing which student number is being entered (calculated dynamically based on current list size)
        print(f"\nIngrese los datos del estudiante {len(students) + 1}:")

        # Get basic student information
        nombre = input("Nombre completo: ")
        seccion = input("Seccion (ej. 11B) ")

        # Inicializar variables para las notas
        notas = {}
        # Define the subjects for which grades will be collected
        subjets = ["español", "ingles", "sociales", "ciencias"]
        for subjet in subjets: # Loop through each subject
            while True:
                try:
                    # Get and validate the grade for each subject
                    note = float(input(f"Nota de {subjet} (0-100):"))
                    if 0 <= note <= 100:
                        notas[subjet] = note # Add grade to student record
                        break
                    else: 
                        print("La nota debe estar entre 0 y 100. Intente nuevamente.")
                except ValueError:
                    print("Ingrese una nota valida (un numero). Intente nuevamente.")
        
        # Create a Student object and add it to the list
        student = Student(nombre, seccion, notas["español"], notas["ingles"], notas["sociales"], notas["ciencias"])
        students.append(student)
    
    # Confirm successful addition of students
    print(f"\nSe han ingresado {n} estudiantes correctamente.")

def show_students(students):
    """
    Display the list of students.

    Args:
        students (list): List of Student objects.
    """
    # Check if there are any students to display
    if not students:
        print("No hay estudiantes registrados.")
        return

    print("\n--- LISTA DE ESTUDIANTES ---")
    for i, student in enumerate(students, 1):
        # Display information for each student
        print(f"\nEstudiante {i}:")  # Display student number
        print(f"Nombre: {student.nombre}")
        print(f"Seccion: {student.seccion}")
        print(f"Nota de Español: {student.español}")
        print(f"Nota de Ingles: {student.ingles}")
        print(f"Nota de Sociales: {student.sociales}")
        print(f"Nota de Ciencias: {student.ciencias}")
        # Calculate and display the student's overall average
        promedio = student.calcular_promedio()
        print(f"Promedio General: {promedio:.2f}")  # Display average with 2 decimal places

def top3_students(students):
    """
    Display the top 3 students based on their overall average grade.

    Args:
        students (list): List of Student objects.
    """
    # Check if there are any students to rank
    if not students:
        print("No hay estudiantes registrados.")
        return

    # Create a dictionary to store unique students by name and section
    unique_students = {}
    
    # Calculate average for each student and store only unique students
    for student in students:
        # Create a unique key using name and section
        key = (student.nombre, student.seccion)
        
        promedio = student.calcular_promedio()
        
        # Only keep the student if we haven't seen this name+section before,
        # or if this instance has a higher average than the one we've seen
        if key not in unique_students or promedio > unique_students[key][1]:
            unique_students[key] = (student, promedio)
    
    # Convert dictionary values back to a list
    students_with_average = list(unique_students.values())

    # Sort the list of (student, average) tuples by average grade in descending order and take only the top 3
    students_with_average = sorted(
        students_with_average,  # The list of (student, average) tuples to sort
        key=lambda x: x[1],     # Sort based on the second element of each tuple (the average grade)
        reverse=True,           # Sort in descending order (highest grades first)
    )[:3]                       # Slice the result to get only the first 3 elements (top 3 students)

    # Display the top 3 students
    print("\n--- TOP 3 ESTUDIANTES ---")
    for i, (student, average) in enumerate(students_with_average, 1):
        print(f"\nPosición {i}:")   
        print(f"Nombre: {student.nombre}")  # Removed extra comma
        print(f"Seccion: {student.seccion}")  # Removed extra comma
        print(f"Promedio General: {average:.2f}")

def overall_average(students):
    """
    Calculate and display the overall average grade for all students.

    Args:
        students (list): List of Student objects.
    """
    # Check if there are any students to calculate average
    if not students:
        print("No hay estudiantes registrados.")
        return  # Added return statement to prevent division by zero

    # Calculate the sum of all student averages
    total_average = 0
    for student in students:
        total_average += student.calcular_promedio()

    # Calculate and display the overall average for all students
    average = total_average / len(students)
    print(f"\nPromedio General de todos los estudiantes: {average:.2f}")