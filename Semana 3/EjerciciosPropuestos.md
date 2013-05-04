Ejercicio 1: Multiplicaciones Everywhere!
=============

**Propuesta:** 
>Hacer un método que reciba como parametro un array de numeros (una lista) y devuelva la multiplicaciones de todos ellos.

**Ejemplos:**

	>>>multiplicaLista([5])
	5

	>>>multiplicaLista([1,2,3,4])
	24

	>>>multiplicaLista([-1,1,2,3,4])
    -24


**Dificultad:** baja-media


Ejercicio 2: ¿Seguro que es un numero?
=============

**Propuesta:** 
>Hacer un método que recibe un numero positivo, y devuelve la suma de cada digito.

**Ejemplos:**
	
	>>>suma_digitos(1234)
	10   # 1 + 2 + 3 + 4
	
	>>>suma_digitos(555)
	15


>[Nota: para transformar una variable a string (cadena) se usa la funcion str(x) y para convertir algo a numero se usa int(x)]

**Dificultad:** baja-media


Ejercicio 3: A factorizar!
=============

**Propuesta:**
>Hacer un metodo que recibe un numero entero mayor o igual que 1 y devuelve el factorial (la multiplicacion desde 1 hasta el mismo numero)

**Ejemplos:**

	>>>factorial(4)
	24  # 4 * 3 * 2 * 1

	>>factorial(5)
	120

>[[Nota para los que ya hayan programado antes: Hacerlo solo con bucles for y sin recursividad]]

**Dificultad:** media


Ejercicio 4: Rizando el rizo de las listas.
=============

**Propuesta:**
>Hacer un método que reciba como parametro una lista, donde cada elemento es una lista con tres elementos, el nombre de una empresa, el numero de trabajadores, y el beneficio total.
>El metodo debe devolver tres cosas, el numero total de empresas, el numero total de trabajadores, y el beneficio total.


**Ejemplos:**
	
	ejemplo_lista = [
	["IBM", 5000, 10000],
	["ACM", 2000, 20000],
	["Python", 10000, 100000]
	]

	>>>total_empresas(ejemplo_lista)
	(3,17000,130000)

>[[Nota: No devuelve una lista con los tres valores, sino que devuelve los tres valores]]

**Dificultad:** media-alta

