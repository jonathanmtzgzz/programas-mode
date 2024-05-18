import random
import math
import tkinter as tk

def generar_numeros_rectangulares(n):
    numeros_rectangulares = []
    for _ in range(n):
        numero = round(random.uniform(0, 1), 5)
        numeros_rectangulares.append(numero)
    return numeros_rectangulares

def generar_variables_aleatorias():
    cantidad_numeros = int(cantidad_numeros_entry.get())
    a = float(a_entry.get())
    b = float(b_entry.get())

    numeros_rectangulares = generar_numeros_rectangulares(cantidad_numeros)
    variables_aleatorias = []

    for numero_rectangular in numeros_rectangulares:
        variable_aleatoria = round(a + (b - a) * numero_rectangular, 5)
        variables_aleatorias.append(variable_aleatoria)

    variables_aleatorias_text.delete(1.0, tk.END)
    for i, variable_aleatoria in enumerate(variables_aleatorias):
        variables_aleatorias_text.insert(tk.END, f"Te{i + 1} = {variable_aleatoria}\n")

    total = round(sum(variables_aleatorias), 5)
    variables_aleatorias_text.insert(tk.END, f"\nTet = {total}\n")

    media = round(sum(variables_aleatorias) / cantidad_numeros, 5)
    variables_aleatorias_text.insert(tk.END, f"Tep = {media}\n")

ventana = tk.Tk()
ventana.title("Distibución Uniforme")
ventana.resizable(False, True)
ventana.config(padx=50, pady=20)

cantidad_numeros_label = tk.Label(ventana, text="Cantidad de números aleatorios:")
cantidad_numeros_label.grid(row=0, column=0, padx=10, pady=10)

cantidad_numeros_entry = tk.Entry(ventana)
cantidad_numeros_entry.grid(row=0, column=1, padx=10, pady=10)

a_label = tk.Label(ventana, text="Valor mínimo de a:")
a_label.grid(row=1, column=0, padx=10, pady=10)

a_entry = tk.Entry(ventana)
a_entry.grid(row=1, column=1, padx=10, pady=10)

b_label = tk.Label(ventana, text="Valor máximo de b:")
b_label.grid(row=2, column=0, padx=10, pady=10)

b_entry = tk.Entry(ventana)
b_entry.grid(row=2, column=1, padx=10, pady=10)

generar_button = tk.Button(ventana, text="Generar", command=generar_variables_aleatorias)
generar_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

variables_aleatorias_text = tk.Text(ventana)
variables_aleatorias_text.grid(row=4, column=0, columnspan=2,  padx=10, pady=10)

ventana.mainloop()
