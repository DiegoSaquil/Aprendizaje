print("******* BIENVENIDO *******")

er = str(input("Por favor ingrese su expresión regular: "))

cadena = "La cadena de la expresión regular es la siguiente: "
automata = "El AFN y AFD de la expresión regular es el siguiente: "

while True:
 print("\n\n******** Por favor seleccione la opción deseada ********")
 print("1: Mostrar la expresión regular")
 print("2: Mostrar la cadena de la expresión regular")
 print("3: Mostrar el autómata determinista")
 print("4: Salir")


 menu = int(input("Seleccione una opción con los numeros 1 al 4: "))

 if menu == 1:
    print(er)
 elif menu == 2:
    print(cadena)
 elif menu == 3:
    print(automata)
 elif menu == 4:
   print("Saliendo del programa...")
   break
 else:
    print("Opción no válida, por favor seleccione un número entre 1 y 5.")
