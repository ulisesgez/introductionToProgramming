"""
Condicionales:
Los condicionales son estructuras de control en programación que permiten ejecutar cierto
bloque de código basado en una condición booleana. La idea fundamental es que el programa
puede tomar decisiones y ejecutar diferentes acciones dependiendo de si una condición es
verdadera o falsa.

En Python, la estructura básica de un condicional utiliza la palabra clave if,
seguida de una expresión booleana, y opcionalmente puede incluir cláusulas elif
(abreviatura de "else if") y una cláusula else que se ejecuta cuando ninguna de
las condiciones anteriores es verdadera. Aquí tienes un ejemplo:
"""
x = 10

if x > 0:
    print("x es positivo")
elif x < 0:
    print("x es negativo")
else:
    print("x es cero")

"""
En este ejemplo, el programa evalúa la condición x > 0. Si es verdadera,
imprime "x es positivo". Si no, pasa a evaluar la siguiente condición x < 0.
Si esta es verdadera, imprime "x es negativo". Si ninguna de las condiciones
anteriores es verdadera, se ejecuta el bloque de código dentro de la cláusula else,
que imprime "x es cero".

Los condicionales son fundamentales para el control del flujo de un programa y
son ampliamente utilizados para tomar decisiones basadas en ciertas condiciones.
"""