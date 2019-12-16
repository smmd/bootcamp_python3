#WIP
import csv, json

datos = {}
with open('02_tarea.csv') as archivo:
	lector = csv.reader(archivo, delimiter=',')

	lineas = 0

	for linea in lector:
		if lineas == 0:
			continue
			lineas += 1
		else:
			accion = int(linea[1])
			datos["total_acciones"] += accion

print(datos) 
