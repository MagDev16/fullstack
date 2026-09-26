#-------------------------------------------------------------------#
#Ejercicio 1
#-------------------------------------------------------------------#
print(f'#-------------------------------------------------------------------#')
print(f'#------------------- información sobre un hotel---------------------#')
print(f'#-------------------------------------------------------------------#\n')

las_nubes_hostal = {
    'pais': 'Panama',
    'provincia': 'Chiriqui',
    'corregimiento': 'Cerro Punta',
    'pueblo': 'Las Nubes',
    'nombre_hotel': 'Las Nubes Hostal',
    'baños': 3,
    'habitaciones': [
        {
            'nombre': 'Cerro Punta',
            'numero': 1,
            'baño' : 'completo',
            'precio_por_noche': '$45pp'
        },
        {
            'nombre': 'Volcan Baru',
            'numero': 2,
            'baño' : 'completo',
            'precio_por_noche': '$39pp'
        },
        {
            'nombre': 'La Amistad',
            'numero': 3,
            'baño' : 'compartido',
            'precio_por_noche': '$12pp'
        },
    ],
}
print("----Informacion del Hostal-----") 
for caracteristica, respuesta in las_nubes_hostal.items():
    print(f'{caracteristica} : {respuesta}')
    #print(las_nubes_hostal['nombre_hotel'])

print("----Informacion de cada habitacion-----")    
for habitacion in las_nubes_hostal['habitaciones']:
    print(f"Habitacion: {habitacion['numero']}")
    print(f"Nombre: {habitacion['nombre']}")
    print(f"Precio por noche: {habitacion['precio_por_noche']}")
    print(f"Baño: {habitacion['baño']}")
    print("-" * 20)