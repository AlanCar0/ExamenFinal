import random
import csv

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = []
#asignar sueldos
def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    print("Sueldos asignados exitosamente.")
#Clasificación de menor a mayor
def clasificar_sueldos():
    menores_800k = [(trabajadores[i], sueldos[i]) for i in range(len(sueldos)) if sueldos[i] < 800000]
    entre_800k_y_2M = [(trabajadores[i], sueldos[i]) for i in range(len(sueldos)) if 800000 <= sueldos[i] <= 2000000]
    mayores_2M = [(trabajadores[i], sueldos[i]) for i in range(len(sueldos)) if sueldos[i] > 2000000]
    #menores
    print("Sueldos menores a $800.000 TOTAL: {}".format(len(menores_800k)))
    for nombre, sueldo in menores_800k:
        print(f"{nombre} \t ${sueldo}")
    #intermedios
    print("\nSueldos entre $800.000 y $2.000.000 TOTAL: {}".format(len(entre_800k_y_2M)))
    for nombre, sueldo in entre_800k_y_2M:
        print(f"{nombre} \t ${sueldo}")
    #gente millonaria
    print("\nSueldos superiores a $2.000.000 TOTAL: {}".format(len(mayores_2M)))
    for nombre, sueldo in mayores_2M:
        print(f"{nombre} \t ${sueldo}")
    #sumamos todo y...
    print("\nTOTAL SUELDOS: ${}".format(sum(sueldos)))
#promedio y mas alto y mas bajo
def ver_estadísticas():
    sld_max = max(sueldos)
    sld_min = min(sueldos)
    promedio_slds = sum(sueldos) / len(sueldos)
    #ahora printearlo
    print("Sueldo mas alto: ${}".format(sld_max))
    print("\nSueldo mas bajo: ${}".format(sld_min))
    print("\nPromedio de sueldos: ${:.2f}".format(promedio_slds))
#csv data
def reporte_sueldos_csv():
    #como odio hacer csv pipippi
    with open('Reporte_salarios.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for i in range(len(trabajadores)):
            sueldo_bruto = sueldos[i]
            menos_salud = sueldo_bruto * 0.07
            menos_afp = sueldo_bruto * 0.12
            liquido = sueldo_bruto - menos_salud - menos_afp
            writer.writerow({
                'Nombre empleado': trabajadores[i], 
                'Sueldo Base': sueldo_bruto, 
                'Descuento Salud': menos_salud, 
                'Descuento AFP': menos_afp, 
                'Sueldo Líquido': liquido
            })
    
    print("Reporte de sueldos guardado en 'Reporte_salarios.csv'.")
#un menu wapo
while True:
    print("\nQue desea hacer:")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Guardar reporte de sueldos en CSV")
    print("5. Salir del programa")
    opcion = input("Seleccione una opción (ingrese el numero de la opción):")    
    if opcion == '1':
        asignar_sueldos()
    elif opcion == '2':
        clasificar_sueldos()
    elif opcion == '3':
        ver_estadísticas()
    elif opcion == '4':
        reporte_sueldos_csv()
    elif opcion == '5':
        print("hasta la proxima...")
        print("saliendo Del programa\nDesarrolado por Alan Caro\nRut: 21.491.770-K")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
