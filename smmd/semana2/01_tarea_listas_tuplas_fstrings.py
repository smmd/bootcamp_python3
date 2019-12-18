def pepepecasOpcionUno(tupla):
    palabras = ((0, 1, 0, 1), (0, 1, 2, 3, 4), (0, 5, 2, 3), (0, 3, 0, 3, 4))

    trabalenguas = []

    for letras in palabras:
        palabra = ""
        for letra in letras:
            palabra = palabra + tupla[letra]
        trabalenguas.append(palabra)
    trabalenguas[::2] = [palabra.upper() for palabra in trabalenguas[::2]]

    return " ".join(trabalenguas + trabalenguas[::-1])

def pepepecaOpcionDos(tupla):
    palabras = (
		(0, 1, 0, 1),
		(0, 1, 2, 3, 4),
		(0, 5, 2, 3),
		(0, 3, 0, 3, 4)
    )

    trabalenguas = ["".join([tupla[letra] for letra in palabra]) for palabra in palabras]
    trabalenguas[::2] = [palabra.upper() for palabra in trabalenguas[::2]]

    return " ".join(trabalenguas + trabalenguas[::-1])

tupla = ('p','e', 'c', 'a', 's', 'i')
#PEPE pecas PICA papas papas PICA pecas PEPE
print(pepepecasOpcionUno(tupla))
print(pepepecaOpcionDos(tupla))
