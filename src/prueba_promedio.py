import random
import tkinter as tk
from scipy.stats import norm

# Variables globales
n = 0
suma = 0
numeros = []
promedio = 0
valorTabla = 0.4750
formula = r"Zo = [(x̄ - 1/2)(n^1/2)]/[(1/12)^1/2]"

def generarNumeros(n):
    global numeros
    numeros = [round(random.random(), 5) for _ in range(n)]

def imprimirNumeros():
    listNumbers.delete(0, tk.END)
    for numero in numeros:
        listNumbers.insert(tk.END, numero)

def sumarNumeros():
    global suma
    suma = round(sum(numeros), 5)

def promediar():
    global promedio
    promedio = round(suma / n, 5)

def saveNumber():
    global n
    n = int(entrada.get())
    generarNumeros(n)
    imprimirNumeros()
    sumarNumeros()
    promediar()
    datos.config(text=f'Σ = {suma}  x̄ = {promedio}')
    formula_actualizada = f"Zo = [({promedio} - 1/2)({n}^1/2)]/[(1/12)^1/2]"
    formulaGeneral.config(text=formula_actualizada)
    calcularEstadistico()

def calcularEstadistico():
    global valorTabla
    try:
        alpha = float(alphaEntry.get())
        valorTabla = norm.ppf(1 - alpha / 2)  # Obteniendo el valor crítico Zα/2
    except ValueError:
        valorTabla = norm.ppf(1 - 0.05 / 2)  # Valor por defecto si la entrada no es válida

    numerador = (promedio - 1/2) * (n ** 0.5)
    denominador = (1/12) ** 0.5
    calculo = numerador / denominador

    if abs(calculo) < valorTabla:
        resultado = "Los números son aceptados"
    else:
        resultado = "Los números no son aceptados"

    estadisticos.config(text=f"Zo = {calculo:.5f} < Zα/2 = {valorTabla:.4f} - {resultado}")

# Configuración de la ventana
ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title('Prueba de Promedios')

# Widgets
alphaLabel = tk.Label(text='α (por ejemplo, 0.05):')
alphaEntry = tk.Entry(ventana)
alphaEntry.insert(0, '0.05')  # Valor inicial de alpha

pregunta = tk.Label(text='¿Cuántos números quieres generar?')
entrada = tk.Entry(ventana)
botonGenerar = tk.Button(text='Generar', command=saveNumber)
listNumbers = tk.Listbox(ventana)
datos = tk.Label(text=f'Σ = {suma}  x̄ = {promedio}')
formulaGeneral = tk.Label(text=formula)
estadisticos = tk.Label(text="Zo < Zα/2")

# Colocar widgets en la ventana
alphaLabel.pack()
alphaEntry.pack()
pregunta.pack()
entrada.pack()
botonGenerar.pack()
listNumbers.pack()
datos.pack()
formulaGeneral.pack()
estadisticos.pack()

# Ejecutar la aplicación
ventana.mainloop()