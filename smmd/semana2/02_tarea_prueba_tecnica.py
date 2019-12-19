#WIP
import csv, json
from datetime import datetime

def generarReporte():
	datos = {
		"fecha": datetime.now().strftime('%m/%d/%y'),
		"total_efectivo": 0,
		"total_acciones": 0,
        "personas": [],
	}

	with open('02_tarea.csv') as archivo:
		lector = csv.DictReader(archivo, delimiter=',')

		lineas = 0
		for linea in lector:
			if lineas == 0:
				lineas += 1
			else:
				datos['total_efectivo'] += float(linea['EFECTIVO'])
				datos['total_acciones'] += float(linea['ACCIONES'])
				datos['personas'].append({
                    'nombre': f'{linea["PERSONA"]}',
                    'acciones': f'{linea["ACCIONES"]}',
                    'efectivo': f'{linea["EFECTIVO"]}',
                    'porcentaje': 'aiññ no quiero hacer otro for'
                })
			lineas += 1

	return json.dumps(datos, indent=2)

print(generarReporte())
