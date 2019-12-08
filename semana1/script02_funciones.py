def upper_cadenas(cadena):
	print(cadena.upper())

def find_cadena(cadena):
	print(cadena.find('gracias'))

def cambiando_cadenas(cadena):
	nueva_cadena = cadena.replace('o', '0')
	print(nueva_cadena)

def suma(num1, num2):
	return num1 + num2

def revertir(cadena_tarea):
	stringlength=len(cadena_tarea)
	print(cadena_tarea[stringlength::-1])

upper_cadenas('hello kat')
find_cadena('gracias por el curso')
cambiando_cadenas('Hello World!')
revertir('supercalfragilisticoespiralidoso')

suma = suma(89,90)
print(suma * 2)
