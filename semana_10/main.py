# Import the main menu function from menu.py
from menu import show_main_menu

def main():
    try:
        # Initialize an empty list to store student records
        students = [] 
        # Display the main menu and pass the students list as a parameter
        show_main_menu(students) 
    except Exception as e:
        # Handle any unexpected errors that might occur during execution
        print("\nAn error occurred:", str(e))
        print("Please try again.")

if __name__ == "__main__":
    main()