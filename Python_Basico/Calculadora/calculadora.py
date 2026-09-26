# Function to display the menu options
def show_menu(current_number):
    print("\n" + "="*43)                      
    print("================CALCULADORA🧮==============") 
    print("="*43 + "\n")                      
    print(f"Numero actual: {current_number}" + "\n") 
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Limpiar resultado")
    print("6. Salir")

# Function to handle user input and validate numbers
def get_number():
    while True:  # Infinite loop until valid input received
        try:
            return float(input("Ingrese un numero con el cual realizara la operacion: "))  # Get and convert input to decimal number
        except ValueError:  # Handle non-numeric inputs (letters, symbols, etc.)
            print("Error: Por favor, ingrese un numero valido.")

# Main calculator function that controls program flow
def calculator():
    current_number = 0    # Initialize starting number as zero
    
    while True:          # Main program loop
        show_menu(current_number)  # Display calculator interface
        try:
            # Get user's menu choice
            option = int(input("\nSeleccione una opcion de entre (1-6): "))
            
            # Handle exit option
            if option == 6:
                print("\nGracias por usar la caluladora🧮!")
                break   # Exit the program
            
            # Handle clear option
            if option == 5:
                current_number = 0  # Reset current number to zero
                print("\nResultado despejado!")
                continue  # Go back to menu
                
            # Validate menu selection
            if option not in [1, 2, 3, 4]:
                print("\nError: Opcion no valida.")
                continue  # Go back to menu
                
            # Get second number for operation
            new_number = get_number()
            # Save current value before operation for display
            old_value = current_number
            # Perform selected mathematical operation
            if option == 1:
                current_number += new_number  # Addition operation
                print(f"\n{old_value} + {new_number} = {current_number}")
            elif option == 2:
                current_number -= new_number  # Subtraction operation
                print(f"\n{old_value} - {new_number} = {current_number}")
            elif option == 3:
                current_number *= new_number  # Multiplication operation
                print(f"\n{old_value} × {new_number} = {current_number}")
            elif option == 4:
                try:
                    current_number /= new_number  # Division operation
                    print(f"\n{old_value} ÷ {new_number} = {current_number}")
                except ZeroDivisionError:    # Handle division by zero error
                    print("\nError: No se puede dividir por 0")
                    continue
            
            # Pause for user to see result
            input("Presione Enter para continuar...")    
                    
        except ValueError:  # Handle invalid menu selections
            print("\nError: Por favor, ingrese una opcion valida.")
if __name__ == "__main__":
    calculator()