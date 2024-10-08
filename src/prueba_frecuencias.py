import random
from scipy.stats import chi2
import tkinter as tk
from tkinter import messagebox

def prueba_frecuencias(numeros, n_subintervalos, alfa):
  """
  Función que realiza la prueba de frecuencias de números aleatorios.

  Argumentos:
    numeros (lista): Lista de números aleatorios.
    n_subintervalos (int): Número de subintervalos para la prueba.
    alfa (float): Nivel de significancia.

  Retorno:
    bool: True si los números parecen provenir de una distribución uniforme, False en caso contrario.
  """

  # Verificar si la lista está vacía
  if not numeros:
    return False

  # Calcular el tamaño de la muestra y el rango de números
  n_muestra = len(numeros)
  rango_min = min(numeros)
  rango_max = max(numeros)

  # Validar el número de subintervalos
  if n_subintervalos <= 0:
    messagebox.showerror("Error", "El número de subintervalos debe ser mayor a 0.")
    return False
  elif n_subintervalos >= n_muestra:
    messagebox.showerror("Error", "El número de subintervalos debe ser menor que la cantidad de números.")
    return False

  # Dividir el rango en subintervalos iguales
  ancho_subintervalo = (rango_max - rango_min) / n_subintervalos

  # Contar frecuencias en cada subintervalo
  frecuencias_observadas = [0] * n_subintervalos
  for numero in numeros:
    # Corrección del cálculo de indice_subintervalo
    indice_subintervalo = min(int((numero - rango_min) // ancho_subintervalo), n_subintervalos - 1)
    frecuencias_observadas[indice_subintervalo] += 1

  # Calcular frecuencias esperadas
  frecuencias_esperadas = [n_muestra / n_subintervalos] * n_subintervalos

  # Calcular estadístico Chi-cuadrado
  chi_cuadrado = 0
  for i in range(n_subintervalos):
    diferencia = (frecuencias_observadas[i] - frecuencias_esperadas[i]) ** 2
    chi_cuadrado += diferencia / frecuencias_esperadas[i]

  # Calcular valor crítico de Chi-cuadrado
  grados_libertad = n_subintervalos - 1
  valor_critico = chi2.ppf((1 - alfa), grados_libertad)

  # Interpretar resultado
  if chi_cuadrado < valor_critico:
    return True  # No se rechaza la hipótesis de uniformidad
  else:
    return False  # Se rechaza la hipótesis de uniformidad

def realizar_prueba():
  numeros_string = numeros_entry.get()
  numeros = [float(numero) for numero in numeros_string.split()]

  n_subintervalos = int(subintervalos_entry.get())
  alfa = float(alfa_entry.get())

  resultado = prueba_frecuencias(numeros, n_subintervalos, alfa)

  if resultado:
    messagebox.showinfo("Resultado", "Los números son aceptados.")
  else:
    messagebox.showinfo("Resultado", "Los números no son aceptados.")

# Crear ventana principal
window = tk.Tk()
window.title("Prueba de Frecuencias")
window.geometry("400x200")

# Crear etiquetas y campos de entrada
numeros_label = tk.Label(window, text="Ingrese una lista de números aleatorios separados por espacios:")
numeros_label.pack()

numeros_entry = tk.Entry(window)
numeros_entry.pack()

subintervalos_label = tk.Label(window, text="Ingrese el número de subintervalos para la prueba (menor que la cantidad de números):")
subintervalos_label.pack()

subintervalos_entry = tk.Entry(window)
subintervalos_entry.pack()

alfa_label = tk.Label(window, text="Ingrese el nivel de significancia (alfa):")
alfa_label.pack()

alfa_entry = tk.Entry(window)
alfa_entry.pack()

# Crear botón para realizar la prueba
prueba_button = tk.Button(window, text="Realizar Prueba", command=realizar_prueba)
prueba_button.pack()

# Iniciar bucle de eventos
window.mainloop()
