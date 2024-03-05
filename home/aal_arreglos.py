"""
Arreglos
Los arreglos son una estructura de datos fundamental en la informática y la programación.
Son conjuntos ordenados de elementos del mismo tipo que se almacenan en una secuencia
contigua de memoria. Aquí tienes algunas definiciones clave relacionadas con los arreglos:

Arreglo: También conocido como vector o array, un arreglo es una estructura de datos que
contiene una colección de elementos, todos del mismo tipo de datos. Los elementos de un
arreglo están organizados en posiciones numeradas consecutivamente, y cada posición tiene
una dirección única.

Elemento del arreglo: Cada valor individual dentro de un arreglo se denomina elemento.
Los elementos de un arreglo están indexados, lo que significa que cada elemento tiene
una posición única dentro del arreglo.

Índice: El índice es la posición numérica que indica la ubicación de un elemento dentro
del arreglo. El primer elemento generalmente tiene un índice de 0 en muchos lenguajes
de programación, aunque en algunos casos puede empezar en 1.

Longitud del arreglo: Es la cantidad total de elementos que contiene un arreglo.
La longitud se puede determinar al declarar el arreglo o durante la ejecución del programa.

Tipo de datos del arreglo: Es el tipo de datos que todos los elementos del arreglo deben
tener. Puede ser un tipo de datos primitivo (como entero, flotante, carácter, etc.)
o un tipo de datos compuesto (como una estructura o un objeto).

Acceso y manipulación de elementos: Los elementos de un arreglo se pueden acceder y
manipular utilizando su índice. Esto permite leer, escribir o modificar valores
específicos dentro del arreglo.

Operaciones comunes con arreglos: Incluyen la inicialización del arreglo,
la asignación de valores a los elementos, la lectura de valores de los elementos,
la búsqueda de elementos, la inserción de elementos, la eliminación de elementos
y la ordenación de los elementos.

Los arreglos son una herramienta poderosa y versátil en la programación y se utilizan en
una amplia variedad de aplicaciones, desde la manipulación de datos hasta la implementación
de algoritmos complejos.

Arreglos unidimensionales: También conocidos como vectores, son arreglos que contienen
una sola fila de elementos. Cada elemento se puede acceder utilizando un solo índice.
Los arreglos unidimensionales son comúnmente utilizados para almacenar listas simples
de elementos del mismo tipo.
"""
print("Arreglos unidimensionales")
# Declaración e inicialización de un arreglo unidimensional
arreglo_unidimensional = [1, 2, 3, 4, 5]

"""
Arreglos bidimensionales: También conocidos como matrices, son arreglos que contienen filas
y columnas de elementos. Los elementos de una matriz se pueden acceder utilizando dos índices:
uno para la fila y otro para la columna.
Se pueden visualizar como una cuadrícula o una tabla.
"""
print("Arreglos bidimensionales")
# Declaración e inicialización de una matriz bidimensional
matriz_bidimensional = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
"""
En esta matriz, matriz_bidimensional[0][0] representa el elemento en la primera fila
y primera columna, que es 1, matriz_bidimensional[1][2] representa el elemento en la
segunda fila y tercera columna, que es 6, y así sucesivamente.

Arreglos multidimensionales: Son arreglos que tienen más de dos dimensiones.
Esto significa que contienen elementos organizados en tres o más niveles de profundidad.
Por ejemplo, una matriz tridimensional sería un arreglo que contiene filas,
columnas y niveles.
"""
print("Arreglos multidimensionales")
# Declaración e inicialización de una matriz tridimensional
matriz_tridimensional = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]
"""
En esta matriz, matriz_tridimensional[0][0][0] representa el primer elemento en
la primera fila y primera columna del primer nivel, que es 1, y así sucesivamente.
"""