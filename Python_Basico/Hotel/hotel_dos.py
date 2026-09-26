#-------------------------------------------------------------------#
#Ejercicio 2
#-------------------------------------------------------------------#
print(f'#-------------------------------------------------------------------#')
print(f'#-----------------------Devolver dos listas-------------------------#')
print(f'#-------------------------------------------------------------------#\n')

primera_lista = ['nombre', 'numero', 'baño']
segunda_lista = ['Baru', 'Uno', 'Completo']

diccionario = dict(zip(primera_lista, segunda_lista))
# Une las dos listas elemento por elemento
# dict() convierte los pares en un diccionario

print(diccionario)