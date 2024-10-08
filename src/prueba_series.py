import tkinter as tk
import random
from tkinter import scrolledtext
from scipy.stats import chi2

def generate_random_numbers(n):
    random_numbers = []
    for i in range(n):
        random_number = round(random.uniform(0, 1), 5)
        random_numbers.append(random_number)
    return random_numbers

def print_coordinates(random_numbers, intervalos):
    coordenadas_text.delete(1.0, tk.END)  # Limpiar el texto existente
    for i in range(len(random_numbers) - 1):
        x = random_numbers[i]
        y = random_numbers[i+1]
        quadrante = calcular_cuadrante(x, y, intervalos)
        coord_str = f"({x}, {y}) -> Cuadrante {quadrante}\n"
        coordenadas_text.insert(tk.END, coord_str)

def calcular_cuadrante(x, y, intervalos):
    x_intervalo = int(x * intervalos)
    y_intervalo = int(y * intervalos)
    
    if x_intervalo == intervalos:
        x_intervalo -= 1
    if y_intervalo == intervalos:
        y_intervalo -= 1
    
    cuadrante = chr(65 + y_intervalo + x_intervalo * intervalos)
    return cuadrante

def calculate_quadrants(intervalos):
    quadrantes = intervalos ** 2
    return quadrantes

def calcular_frecuencia_esperada(num_elementos, intervalos):
    frecuencia_esperada = ((num_elementos - 1) / intervalos) / intervalos
    return frecuencia_esperada

def calcular_x0_cuadrado(random_numbers, intervalos):
    frecuencia_esperada = calcular_frecuencia_esperada(len(random_numbers), intervalos)
    observados = [0] * (intervalos ** 2)
    
    for i in range(len(random_numbers) - 1):
        x = random_numbers[i]
        y = random_numbers[i+1]
        quadrante = calcular_cuadrante(x, y, intervalos)
        observados[ord(quadrante) - 65] += 1
    
    x0_cuadrado = sum([((obs - frecuencia_esperada) ** 2) / frecuencia_esperada for obs in observados])
    return round(x0_cuadrado, 2)

def generar_elementos():
    num_elementos = int(num_elementos_entry.get())

    # Elimina los campos de entrada anteriores si ya existen
    for entry in elemento_entries:
        entry.destroy()
    elemento_entries.clear()

    # Crea y coloca los nuevos campos de entrada
    for i in range(num_elementos):
        row = i // 5
        column = i % 5

        entry = tk.Entry(frame_elementos, width=10)
        entry.grid(row=row, column=column, padx=5, pady=5)
        elemento_entries.append(entry)

def generar_numeros_aleatorios():
    for entry in elemento_entries:
        num = round(random.uniform(0, 1), 5)  # Genera un número aleatorio entre 0 y 1 con 5 decimales
        entry.delete(0, tk.END)
        entry.insert(0, str(num))

def calcular_cuadrantes():
    intervalos = int(num_subintervalos_entry.get())
    random_numbers = [float(entry.get()) for entry in elemento_entries]

    quadrantes = calculate_quadrants(intervalos)
    output_text.delete(1.0, tk.END)  # Limpiar el texto existente
    output_text.insert(tk.END, f"El plano cartesiano tendrá {quadrantes} cuadrantes.\n\n")

    # Print coordinates in the second text widget
    print_coordinates(random_numbers, intervalos)

def calcular_frecuencia():
    num_elementos = int(num_elementos_entry.get())
    intervalos = int(num_subintervalos_entry.get())

    frecuencia_esperada = calcular_frecuencia_esperada(num_elementos, intervalos)

    output_text.insert(tk.END, f"La frecuencia esperada es: {frecuencia_esperada}\n")

def calcular_x0_cuadrado_wrapper():
    intervalos = int(num_subintervalos_entry.get())
    random_numbers = [float(entry.get()) for entry in elemento_entries]
    x0_cuadrado = calcular_x0_cuadrado(random_numbers, intervalos)
    output_text.insert(tk.END, f"X0 al cuadrado es: {x0_cuadrado}\n")

    porcentaje = float(porcentaje_entry.get())
    grados_libertad = (intervalos ** 2) - 1
    valor_critico = chi2.ppf(1 - porcentaje / 100, grados_libertad)
    output_text.insert(tk.END, f"El valor crítico de chi-cuadrado para un {porcentaje}% de confianza y {grados_libertad} grados de libertad es: {valor_critico}\n")
    output_text.insert(tk.END, "Resultado de la comparación:\n")
    if x0_cuadrado > valor_critico:
        output_text.insert(tk.END, "X0 al cuadrado es mayor que el valor crítico, por lo tanto, se rechaza la hipótesis nula.\n")
    else:
        output_text.insert(tk.END, "X0 al cuadrado es menor que el valor crítico, por lo tanto, no se rechaza la hipótesis nula.\n")

ventana = tk.Tk()
ventana.title("Generador de Cuadrantes")
ventana.resizable(False, True)
ventana.config(padx=50, pady=20)

# Interfaz para ingresar el número de elementos
num_elementos_label = tk.Label(ventana, text="Número de elementos:")
num_elementos_label.grid(row=0, column=0, padx=10, pady=5)

num_elementos_entry = tk.Entry(ventana, width=10)
num_elementos_entry.grid(row=0, column=1, padx=10, pady=5)

# Interfaz para ingresar el número de subintervalos
num_subintervalos_label = tk.Label(ventana, text="Número de subintervalos:")
num_subintervalos_label.grid(row=1, column=0, padx=10, pady=5)

num_subintervalos_entry = tk.Entry(ventana, width=10)
num_subintervalos_entry.grid(row=1, column=1, padx=10, pady=5)

# Interfaz para ingresar el porcentaje de confianza
porcentaje_label = tk.Label(ventana, text="Porcentaje de confianza:")
porcentaje_label.grid(row=2, column=0, padx=10, pady=5)

porcentaje_entry = tk.Entry(ventana, width=10)
porcentaje_entry.grid(row=2, column=1, padx=10, pady=5)

# Botón para generar campos de entrada
generar_elementos_button = tk.Button(ventana, text="Generar Campos", command=generar_elementos)
generar_elementos_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Botón para generar números aleatorios en los campos de entrada
generar_numeros_aleatorios_button = tk.Button(ventana, text="Generar Aleatorios", command=generar_numeros_aleatorios)
generar_numeros_aleatorios_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Frame para contener los campos de entrada de elementos
frame_elementos = tk.Frame(ventana)
frame_elementos.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

elemento_entries = []

# Botón para calcular cuadrantes
calcular_cuadrantes_button = tk.Button(ventana, text="Calcular Cuadrantes", command=calcular_cuadrantes)
calcular_cuadrantes_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Botón para calcular frecuencia esperada
calcular_frecuencia_button = tk.Button(ventana, text="Calcular Frecuencia", command=calcular_frecuencia)
calcular_frecuencia_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Botón para calcular X0 al cuadrado
calcular_x0_cuadrado_button = tk.Button(ventana, text="Calcular X0 al Cuadrado", command=calcular_x0_cuadrado_wrapper)
calcular_x0_cuadrado_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Crear un widget de texto para la salida de cuadrantes
output_text = scrolledtext.ScrolledText(ventana, width=40, height=10)
output_text.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Crear un widget de texto para la salida de coordenadas
coordenadas_text = scrolledtext.ScrolledText(ventana, width=40, height=5)
coordenadas_text.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
