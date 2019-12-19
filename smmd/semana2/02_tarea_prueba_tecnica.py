
import csv, json
from datetime import datetime

def generarReporte(nombreArchivo):
	datos = {
		#Esta más padre strftime('%x') pero no me da YYYY :(
		"fecha": datetime.now().strftime('%m/%d/%Y'),
		"total_efectivo": 0,
		"total_acciones": 0,
        "personas": [],
	}

	with open(nombreArchivo) as archivo:
		lector = csv.DictReader(archivo, delimiter=',')

		lineas = 0
		for linea in lector:
			datos['total_efectivo'] += float(linea['EFECTIVO'])
			datos['total_acciones'] += float(linea['ACCIONES'])

			datos['personas'].append({
                'nombre': f'{linea["PERSONA"]}',
                'acciones': f'{linea["ACCIONES"]}',
                'efectivo': f'{linea["EFECTIVO"]}',
            })

			lineas += 1

		[persona.update(porcentaje=(float(persona['efectivo'])*100)/float(datos['total_efectivo'])) for persona in datos['personas']]

	return json.dumps(datos, indent=2)

print(generarReporte('02_tarea.csv'))
