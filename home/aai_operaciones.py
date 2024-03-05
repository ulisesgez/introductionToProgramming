"""
Operaciones entre Variables:
Las operaciones entre variables se refieren a las acciones matemáticas, lógicas o de
comparación que se realizan utilizando los valores almacenados en variables.
Estas operaciones pueden incluir desde cálculos aritméticos simples como sumas,
restas, multiplicaciones y divisiones, hasta operaciones más complejas como comparaciones
de igualdad, desigualdad o combinaciones lógicas como conjunciones, disyunciones y negaciones.

En resumen, las operaciones entre variables permiten manipular y trabajar con los datos
almacenados en las variables para realizar diferentes tipos de tareas, ya sea para
calcular resultados numéricos, realizar comparaciones entre valores o controlar
el flujo de un programa mediante operaciones lógicas.

Operaciones Aritméticas:
Las operaciones aritméticas son aquellas que se realizan entre valores numéricos
para calcular resultados matemáticos. Estas operaciones incluyen la suma, resta,
multiplicación y división, así como otras operaciones más avanzadas como el cálculo
de potencias, raíces cuadradas y operaciones de módulo.
"""
a = 5
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b

print("Suma:", suma)  # Salida: 8
print("Resta:", resta)  # Salida: 2
print("Multiplicación:", multiplicacion)  # Salida: 15
print("División:", division)  # Salida: 1.6666666666666667
print("Módulo:", modulo)  # Salida: 2

"""
Operaciones Relacionales:
Las operaciones relacionales son aquellas que se utilizan para comparar valores
y determinar si son iguales, desiguales, mayores, menores o mayores o iguales
que otros valores. Estas operaciones se utilizan para realizar comparaciones
entre variables y tomar decisiones basadas en los resultados de estas comparaciones.
"""
x = 10
y = 5

igual = x == y
distinto = x != y
mayor = x > y
menor = x < y
mayor_o_igual = x >= y
menor_o_igual = x <= y

print("Igual:", igual)  # Salida: False
print("Distinto:", distinto)  # Salida: True
print("Mayor:", mayor)  # Salida: True
print("Menor:", menor)  # Salida: False
print("Mayor o igual:", mayor_o_igual)  # Salida: True
print("Menor o igual:", menor_o_igual)  # Salida: False

"""
Operaciones Lógicas:
Las operaciones lógicas son aquellas que se utilizan para combinar valores
lógicos (verdadero o falso) y realizar operaciones de conjunción, disyunción
y negación. Estas operaciones se utilizan para controlar el flujo de un programa
mediante la evaluación de condiciones lógicas y la toma de decisiones basadas en
estas condiciones.
"""
p = True
q = False

conjuncion = p and q
disyuncion = p or q
negacion_p = not p
negacion_q = not q

print("Conjunción:", conjuncion)  # Salida: False
print("Disyunción:", disyuncion)  # Salida: True
print("Negación de p:", negacion_p)  # Salida: False
print("Negación de q:", negacion_q)  # Salida: True