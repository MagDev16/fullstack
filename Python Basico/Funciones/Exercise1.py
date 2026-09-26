print('--------------------------------------------------------')
print('--Cree dos funciones que impriman dos cosas distintas---')
print('--------------------------------------------------------')

def first_function():
    print("Esta es la primera función")
    print("Ahora vamos a llamar a la segunda función:")
    second_function()

def second_function():
    print("¡Hola! Esta es la segunda función")
    print("Fui llamada desde la primera función")

# We call the first function, which in turn will call the second
first_function()