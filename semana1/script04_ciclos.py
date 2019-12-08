def ciclos(letras_tarea):
	count = 0;

	for letra in letras_tarea:

		if count%2 == 0:
			print(letra)

		count = count + 1

ciclos('supercalifragilisticoespiralidoso')
