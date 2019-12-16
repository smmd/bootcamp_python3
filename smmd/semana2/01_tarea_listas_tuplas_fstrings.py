#INCOMPLETO

def pepepecas(tupla):
	pe = (tupla[0], tupla[1],)

	pecas = list(tupla) 
	pecas.pop()

	pica = pecas.copy()
	pica[1] = tupla[-1]
	pica.remove('s')
	
	papas = pecas.copy()
	papas[1] = tupla[3]
	papas[2] = tupla[0]

	trabalenguas = (
		f'{(pe[0].upper()+pe[1].upper())*2} ' 
		#'{}{}{}{}{} '.format(*pecas)
		f'{(pica[0].upper()+pica[1].upper()+pica[2].upper()+pica[3].upper())} '
		#'{}{}{}{}{} '.format(*papas)
		)

	return trabalenguas

tupla = ('p','e', 'c', 'a', 's', 'i')

#PEPE pecas PICA papas papas PICA pecas PEPE
print(pepepecas(tupla))
