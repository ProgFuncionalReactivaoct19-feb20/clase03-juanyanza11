"""
	Dada las siguientes placas, filtrar aquellas que pertenecen a las provincias de :

	Loja, Pichincha, Esmeraldas, Azuay, Imbabura
"""

placas = ["lba-001", "gma-002", "azx-003", "ess-004",  "oro-100", "mab-001", "iaj-002"]

def validar_provincia(x):
	admitidas = ["l","p","e","a","i"]
	letra = x[0]
	if letra in admitidas:
		return True
	else:
		return False
resultado = filter(validar_provincia, placas)

print(list(resultado)) 