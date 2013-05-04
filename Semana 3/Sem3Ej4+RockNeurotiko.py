def repite_saludo(n, saludo):
	"""
	Recibe un numero "n" y un saludo, y revuelve el saludo concatenado n veces

	>>> repite_saludo(3, "buenas")
	buenasbuenasbuenas
	"""
	return saludo * n

print(repite_saludo(3, "buenas "))
print(repite_saludo(5, "que tal "))
print(repite_saludo(10, "pues bien "))
