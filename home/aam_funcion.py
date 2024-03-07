"""
Funcion:
Son bloques de código que realizan una tarea específica y pueden ser reutilizados en
diferentes partes del programa. Estas funciones toman un conjunto de entradas,
realizan alguna operación sobre ellas y devuelven un resultado.

Declaración de funciones: Se define utilizando una sintaxis específica del lenguaje
de programación que estés utilizando. Por ejemplo, en Python, se usa la palabra clave def,
mientras que en C se utiliza la sintaxis de declaración de función.

Parámetros: Son las entradas que recibe la función. Estos pueden ser opcionales o requeridos,
dependiendo del diseño de la función.

Cuerpo de la función: Es el bloque de código que define lo que hace la función.
Este bloque puede contener cualquier cantidad de instrucciones para realizar la tarea deseada.

Valor de retorno: Es el resultado que la función devuelve después de ejecutar su lógica
interna. No todas las funciones necesariamente devuelven un valor.

Llamada a la función: Es cuando se invoca la función en alguna parte del programa principal
o dentro de otra función. Se proporcionan los argumentos necesarios (si los hay) y se
espera el resultado de la función.
"""
def suma(a, b):
    resultado = a + b
    return resultado

# Llamada a la función
resultado_suma = suma(3, 4)
print(resultado_suma)  # Salida: 7
#Suma es el nombre de la función, a y b son los parámetros que recibe, y devuelve la suma de a y b.