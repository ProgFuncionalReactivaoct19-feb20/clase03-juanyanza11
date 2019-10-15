"""
	Dadas las siguiente ciudades, filtrar aquellas que tienen un número par como longitud en sus caracteres.

	Loja, Pichincha, Guayaquil, Zamora, Ibarra, Manabi, Machala,  Portoviejo, Macas
"""
lista = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra", "Manabi", "Machala",  "Portoviejo", "Macas"]

def longitud(x):
	num = len(x)
	
	if num % 2 == 0:
		return True
	else:
		return False

resultado = filter(longitud, lista)

print(list(resultado))