def calcular_estadisticas_notas(notas):
    aprobadas = [nota for nota in notas if nota > 70]
    desaprobadas = [nota for nota in notas if nota <= 70]
    
    total_notas = len(notas)
    total_aprobadas = len(aprobadas)
    total_desaprobadas = len(desaprobadas)
    
    promedio_total = sum(notas) / total_notas if total_notas else 0
    promedio_aprobadas = sum(aprobadas) / total_aprobadas if total_aprobadas else 0
    promedio_desaprobadas = sum(desaprobadas) / total_desaprobadas if total_desaprobadas else 0
    
    return total_aprobadas, total_desaprobadas, promedio_total, promedio_aprobadas, promedio_desaprobadas

def main():
    notas = []
    n = int(input("¿Cuántas notas deseas ingresar?: "))
    
    for _ in range(n):
        nota = int(input("Ingresa la nota: "))
        notas.append(nota)
    
    total_aprobadas, total_desaprobadas, promedio_total, promedio_aprobadas, promedio_desaprobadas = calcular_estadisticas_notas(notas)
    
    print(f"Cantidad de notas aprobadas: {total_aprobadas}")
    print(f"Cantidad de notas desaprobadas: {total_desaprobadas}")
    print(f"Promedio de todas las notas: {promedio_total:.0f}")
    print(f"Promedio de las notas aprobadas: {promedio_aprobadas:.0f}")
    print(f"Promedio de las notas desaprobadas: {promedio_desaprobadas:.0f}")

if __name__ == "__main__":
    main()
