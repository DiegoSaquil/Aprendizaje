import tkinter as tk
from tkinter import messagebox

def mostrar_resultado(opcion):
    if opcion == 1:
        resultado_var.set(er)
    elif opcion == 2:
        resultado_var.set(cadena)
    elif opcion == 3:
        resultado_var.set(automata)
    elif opcion == 4:
        root.quit()
    else:
        resultado_var.set("Opción no válida, por favor seleccione un número entre 1 y 4.")

#obtener la expresión regular del input
def obtener_expresion_regular():
    global er
    er = er_var.get()
    if er:
        messagebox.showinfo("Información", "Expresión regular almacenada con éxito.")
    else:
        messagebox.showerror("Error", "Por favor ingrese una expresión regular.")

#variables
er = ""
cadena = "La cadena de la expresión regular es la siguiente: "
automata = "El AFN y AFD de la expresión regular es el siguiente: "

#ventana principal
root = tk.Tk()
root.title("Automatas grupo 2")
root.geometry("500x400")

titulo_label = tk.Label(root, text=" BIENVENIDO ", font=("roman", 20))
titulo_label.pack(pady=10)

#para ingresar la expresión regular
er_var = tk.StringVar()
er_entry = tk.Entry(root, textvariable=er_var, width=50)
er_entry.pack(pady=10)

#boton para guardar la expresión regular
guardar_btn = tk.Button(root, text="Guardar Expresión Regular", command=obtener_expresion_regular)
guardar_btn.pack(pady=10)

#etiqueta para mostrar el resultado
resultado_var = tk.StringVar()
resultado_label = tk.Label(root, textvariable=resultado_var, font=("Arial", 12))
resultado_label.pack(pady=10)

#botones de opciones
boton1 = tk.Button(root, text="Mostrar Expresión Regular", command=lambda: mostrar_resultado(1))
boton1.pack(pady=5)

boton2 = tk.Button(root, text="Mostrar Cadena", command=lambda: mostrar_resultado(2))
boton2.pack(pady=5)

boton3 = tk.Button(root, text="Mostrar Autómata", command=lambda: mostrar_resultado(3))
boton3.pack(pady=5)

boton4 = tk.Button(root, text="Salir", command=lambda: mostrar_resultado(4))
boton4.pack(pady=5)

root.mainloop()