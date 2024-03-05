"""
Estructuras Repetitvas:
Las estructuras repetitivas, también conocidas como bucles o ciclos, son fundamentales en
la programación para ejecutar una secuencia de instrucciones varias veces.

Los bucles son herramientas poderosas pero deben usarse con cuidado para evitar
bucles infinitos. Además, es importante asegurarse de que el bucle eventualmente termine,
ya sea porque la condición se vuelve falsa o porque se utiliza una declaración de
interrupción para salir del bucle.

Hay principalmente tres tipos de estructuras repetitivas en algoritmos:

Bucle while: Este bucle se ejecuta mientras una condición específica sea verdadera.
La estructura básica es:

while condición:
    # Bloque de código a ejecutar mientras la condición sea verdadera
Por ejemplo:
"""
print("Bucle while")

contador = 0
while contador < 5:
    print(contador)
    contador += 1

"""
Bucle for: Este bucle se utiliza cuando se conoce la cantidad exacta de veces que se
desea repetir un bloque de código. La estructura básica es:

for variable in secuencia:
    # Bloque de código a ejecutar para cada elemento de la secuencia
Por ejemplo:
"""
print("Bucle for")

for i in range(5):
    print(i)

"""
Bucle do-while (no presente en todos los lenguajes de programación, pero comúnmente usado):
Este bucle ejecuta un bloque de código al menos una vez y luego comprueba si se debe
continuar ejecutando en función de una condición. Por ejemplo, en Python,
no hay una construcción do-while nativa, pero se puede emular:
"""
print("Bucle do-while")

contador = 0
while True:
    print(contador)
    contador += 1
    if contador >= 5:
        break