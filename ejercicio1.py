"""
	Dado un conjunto de palabras filtrar todas aquellas 
	que sean palindromas
"""
palabras = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]

resultado = filter(lambda x: x == "".join(reversed(x)), palabras)

print(list(resultado))