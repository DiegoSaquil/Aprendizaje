"""
¿qué es un variable?
Es una función que es capaz de realizar algo
lo que podemos hacer llamarla y hacer que cumpla una tarea

las variables normalmente las nombras en minusculas

snake case es escribir todo en minuscula o usar "_"

"""
# es una función Myvariable = "my string variable"
#
# print(Myvariable)


my_string_variable = "una variable correcta"
print(my_string_variable)


myvariableint = '10334567'
print(myvariableint)

myboolvariable = "true"
print(myboolvariable)

my_int_variable = str(myvariableint) #acá llamammos a la cadena 
print(my_int_variable) #acá llamamos lo de arriba
print(type(my_int_variable)) #acá indica el tipo que llamamos en este caso un string

#concatenar cadenas
print(my_string_variable,myboolvariable,str(myvariableint))

print(type(print("rarete")))


#funciones del sistema

print(len(myboolvariable)) #len lo que hace es contar los caracteres

#concatena, recordemos que la coma es un separador para concatenar
print("es un valor para: ", my_string_variable)

#variables en una sola linea | hay que estar atento con los ordenes en la sintaxis
name, surname, alias, edad = "Diego", "Saquil", "Sacuil", "20"
print("mi nombre es:",name,"mi apodo es:",alias,"mi apellido es:", surname,"mi edad es:", edad)

#inputs se usan para ingresar datos en una consola
name = input("whats your name: ")
age = input("how old are you: ")

print(name)
print(age)

#una variable como indica su nombre puede variar o puede cambiar

#python es de tipado dinamico: Esto significa que el lenguaje de programación se encarga automáticamente de inferir el tipo de dato que contiene una variable en el momento en que se le asigna un valor.

#forzamos el tipo
address: str = "MICASA"
address = 32

print(address) #nos damos cuenta que imprime 32 y no "MICASA"

#para tipar el tipo de entrada que deseas recibir es de la siguiente manera:

cantidad = int(input("Cuátos numeros deseas ingresar: "))
print("el numero de caramelos que deseas es de: ", cantidad)

#entonces la estructura es:
#variable = type(int,float,str,complex, etc)(input(el texto o dejarlo asi))
