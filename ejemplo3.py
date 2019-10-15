"""
lista = [1, 2, 10, 11, 12, 13]

resultado = []

for i in lista:
	if i % 2 == 0:
		resultado.append(i)
print(resultado)
"""
lista = [1, 2, 10, 11, 12, 13]
resultado = filter(lambda x: x % 2 == 0, lista)
print(resultado)
print(list(resultado))