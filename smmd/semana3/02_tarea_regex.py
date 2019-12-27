import re

def es_rfc_valido(rfc):
	if (re.search(r'[A-Z]{4}\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])[A-Z0-9]{3}$', rfc)):
		return f'El RFC {rfc} es valido'
	else:
		return 'No se armo'


print(es_rfc_valido('MELM8305281H0'))
print(es_rfc_valido('MELM8328051H0'))
print(es_rfc_valido('M3LM8305281H0'))
print(es_rfc_valido('MELM8305281H0LA'))
