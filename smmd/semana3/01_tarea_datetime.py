from datetime import datetime, timedelta

def de_timestamp_a_semanas(inicio, final):
	dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

	start = datetime.fromtimestamp(inicio)
	start_day = dias_semana[start.weekday()]
	end = datetime.fromtimestamp(final)
	end_day = dias_semana[end.weekday()]

	diff = int((end-start).days / 7)

	return f'Entre el {start_day} {start.strftime("%-d de %b de %Y")} y {end_day} {end.strftime("%-d de %b de %Y")} hay {diff} semanas'

print(de_timestamp_a_semanas(1576454400, 1578268800))
print(de_timestamp_a_semanas(1545091200, 1577750400))
