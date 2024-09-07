#print ("hello world") #al poner un punto de interrupción la ejecucion se para o si queremos hacer un debug (sirve para depurar)

#Los comentarios los asignamos con el signo "#"

""" 
Podemos poner un comentario extenso
de la siguiente manera con los signos 

"""


#print ('podemos ejecutar texto con comillas simples')

print (type("hola mundo")) #type nos muestra el tipo de dato en este caso un string

print(type(1234456789)) #type nos muestra como dijimos el tipo de dato en este caso un int

print(type(0.5)) #type nos muestra que es un tipo de dato float o sea tipos de datos que no son objetos ni numericos

print(type(False)) #type nos muestra que es un booleano

print(type(3+4j)) #type nos muestra que es un omplejo

"""
1. Float (flotante):
Descripción: Es un número que tiene una parte decimal. Los flotantes se utilizan para representar valores con precisión decimal, como 3.14, 0.001, etc.
Formato: Está compuesto por una parte entera y una parte decimal separadas por un punto (.) decimal.
Ejemplo: 3.14, 0.001, -2.5.
Uso común: Se usa principalmente para cálculos matemáticos que requieren decimales, como operaciones financieras, mediciones, o cualquier situación que implique fracciones.
Rango: Su capacidad depende de la implementación del lenguaje, pero suelen tener límites en el número de dígitos significativos que pueden almacenar (precisión).

2. Números complejos:
Descripción: Un número complejo es un número que tiene dos componentes: una parte real y una parte imaginaria. Se escribe en la forma a + bj, donde a es la parte real y b es la parte imaginaria, y j (o i en matemáticas) representa la unidad imaginaria (raíz cuadrada de -1).
Formato: Compuesto por dos números, uno real y uno imaginario.
Ejemplo: 3 + 4j, -2 + 0.5j, 1 - 3j.
Uso común: Se utiliza principalmente en campos como la ingeniería, física, y matemáticas avanzadas (por ejemplo, en el análisis de señales o en electromagnetismo) donde las magnitudes con parte real e imaginaria son importantes.
Operaciones: Se pueden realizar operaciones entre números complejos, como suma, resta, multiplicación, etc., donde ambas partes (real e imaginaria) se manejan de manera separada.

Diferencia principal:
Un float representa un número con una parte decimal.
Un número complejo tiene tanto una parte real como una parte imaginaria, y se utiliza para resolver problemas más avanzados que involucran números imaginarios.
En lenguajes como Python, puedes usar el tipo float para números decimales y el tipo complex para números complejos.

"""