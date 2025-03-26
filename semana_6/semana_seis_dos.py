print('--------------------------------------------------------')
print('------------Experimente con el concepto de scope--------')
print('--------------------------------------------------------')
print('------------------------EJEMPLO 1-----------------------')
print('--------------------------------------------------------')

# Example 1: Access to a variable defined within a function from outside
def example_function():
    # Local variable within the function
    local_var = "Esta es una variable local"
    print("Dentro de la función:", local_var)

# We call the function
example_function()

# We try to access the local variable outside the function
try:
    print("Fuera de la función:", local_var)
except NameError as e:
    print("Error:", e)  # This will show an error because the variable does not exist outside the function

print("\n" + "-"*50 + "\n")


print('--------------------------------------------------------')
print('------------------------EJEMPLO 2-----------------------')
print('--------------------------------------------------------')

# Example 2: Access and modification of a global variable from a function
# We define a global variable
global_var = "Valor inicial global"

def modify_global():
    # If we try to modify the global variable without declaring it, Python creates a new local variable
    # global_var = "Nuevo valor"  # This would create a local variable, would not modify the global
    
    # To modify the global variable, we use the keyword 'global'
    global global_var
    global_var = "Nuevo valor global"
    print("Dentro de la función después de modificar:", global_var)

print("Antes de llamar a la función:", global_var)
modify_global()
print("Después de llamar a la función:", global_var)

print("\n" + "-"*60 + "\n")

# Additional example: Behavior without the word 'global'
other_global_var = "Otro valor global"

def without_declare_global():
    # This creates a local variable with the same name
    other_global_var = "Valor local, no global"
    print("Dentro de la función con variable local:", other_global_var)

print("Antes de llamar a la segunda función:", other_global_var)
without_declare_global()
print("Después de llamar a la segunda función:", other_global_var)  # The global value does not change