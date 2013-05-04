def repite_saludo(n, saludo):
	"""
	Recibe un numero "n" y un saludo, y escibe el saludo n veces

	>>> repite_saludo(3, "buenas")
	buenas
	buenas
	buenas
	"""
	for i in range(n):
		print(saludo)

repite_saludo(3, "buenas")
repite_saludo(5, "que tal")
repite_saludo(10, "pues bien")