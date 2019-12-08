def condicionales(num1, num2):
    if num1 < num2:
        return num1 + num2
    else:
        return num1 * num2

def tarea(alto, ancho):
	if alto == ancho:
		return "Es un cuadrado"
	else:
		print("Es un rectángulo")

print(condicionales(1,2))
print(condicionales(2,1))

print(condicionales(8,4))
print(condicionales(4,8))

print(tarea(10,10))
tarea(10,15)
