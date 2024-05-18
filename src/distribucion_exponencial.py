import random
import math
import tkinter as tk

def generar_numeros_rectangulares(n):
    numeros_rectangulares = []
    for _ in range(n):
        numero = round(random.uniform(0, 1), 5)
        numeros_rectangulares.append(numero)
    return numeros_rectangulares

def calcular_variables_aleatorias():
    cantidad_numeros = int(input_entry.get())
    media_estadistica = float(media_entry.get())

    numeros_rectangulares = generar_numeros_rectangulares(cantidad_numeros)

    variables_aleatorias = []
    for numero_rectangular in numeros_rectangulares:
        variable_aleatoria = round(-(1/media_estadistica) * math.log(numero_rectangular), 5)
        variables_aleatorias.append(variable_aleatoria)

    result_text.delete(1.0, tk.END)
    for i, variable_aleatoria in enumerate(variables_aleatorias):
        result_text.insert(tk.END, f"Ts{i + 1} = {variable_aleatoria}\n")


    total = round(sum(variables_aleatorias), 5)
    result_text.insert(tk.END, f"\nTtoc = {total}\n")

    media = round(sum(variables_aleatorias) / cantidad_numeros, 5)
    result_text.insert(tk.END, f"\nTpa = {media}\n")

ventana = tk.Tk()
ventana.title("Distrubcuión Exponencial")
ventana.resizable(False, True)
ventana.config(padx=50, pady=20)

input_label = tk.Label(ventana, text="Ingrese la cantidad de números aleatorios que desea generar:")
input_label.grid(row=0, column=0, padx=10, pady=10)

input_entry = tk.Entry(ventana)
input_entry.grid(row=0, column=1, padx=10, pady=10)

media_label = tk.Label(ventana, text="Ingrese la media estadística:")
media_label.grid(row=1, column=0, padx=10, pady=10)

media_entry = tk.Entry(ventana)
media_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(ventana, text="Calcular", command=calcular_variables_aleatorias)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_text = tk.Text(ventana)
result_text.grid(row=3, column=0, columnspan=2)

ventana.mainloop()
