#-------------------------------------------------------------------#
#Ejercicio 3
#-------------------------------------------------------------------#
print(f'#-------------------------------------------------------------------#')
print(f'#--------------------Eliminar Keys de diccionario-------------------#')
print(f'#-------------------------------------------------------------------#\n')

datos_a_borrar = ['corregimiento', 'baños']
las_nubes_hostal = {
    'pais': 'Panama',
    'provincia': 'Chiriqui',
    'corregimiento': 'Cerro Punta',
    'pueblo': 'Las Nubes',
    'nombre_hotel': 'Las Nubes Hostal',
    'baños': 3
}

# Creamos nuevo diccionario usando dict comprehension
nueva_info_hostal = {
    #creo un nuevo diccionario si modificar el anterior
    key: value for key, value in las_nubes_hostal.items() if key not in datos_a_borrar
    #solo se incluye el par clave-valor si la clave NO esta en datos_a_borrar
    #si la clave esta en datos_a_borrar ese par se omite
}


print(nueva_info_hostal)