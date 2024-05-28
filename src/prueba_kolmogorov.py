import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
from scipy.stats import kstest
import math

# Generar interfaz gráfica
ventana = tk.Tk()
ventana.title("Prueba de Kolmogorov - Smirnov")
ventana.resizable(False, True)
ventana.config(padx=50, pady=20)

# Crear un placeholder para la tabla
tabla = ttk.Treeview(ventana, columns=('#1', '#2', '#3', '#4'))
tabla.column('#0', width=0, stretch=tk.NO)
tabla.column('#1', width=50, anchor=tk.CENTER)
tabla.column('#2', width=85, anchor=tk.CENTER)
tabla.column('#3', width=100, anchor=tk.CENTER)
tabla.column('#4', width=145, anchor=tk.CENTER)
tabla.heading('#1', text='i')
tabla.heading('#2', text='xi')
tabla.heading('#3', text='F(xi) = i/N')
tabla.heading('#4', text='Dn = MAX/F(xi)-xi/')

tabla.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


def generar_numeros_aleatorios(n):
    numeros_aleatorios = []
    for _ in range(n):
        numero = round(random.uniform(0, 1), 5)
        numeros_aleatorios.append(numero)
    return numeros_aleatorios

def realizar_prueba_ks(alpha, n):
    numeros_aleatorios = generar_numeros_aleatorios(n)
    numeros_aleatorios.sort()

    restas = []
    for i, numero in enumerate(numeros_aleatorios, start=1):
        division = i / n
        resta = abs(division - numero)
        resta = round(resta, 5)
        restas.append(resta)

        tabla.insert('', 'end', values=(i, numero, f"{i}/{n} = {division:.2f}", f"{division:.2f}-{numero} = {resta}"))

    if alpha == 10:
        valor_critico = 1.22 / math.sqrt(n)
    elif alpha == 5:
        valor_critico = 1.36 / math.sqrt(n)
    elif alpha == 1:
        valor_critico = 1.63 / math.sqrt(n)
    else:
        valor_critico = 0

    maxima_resta = max(restas)
    ks_statistic, p_value = kstest(numeros_aleatorios, 'uniform')
    resultado = f"\nMáxima resta: {maxima_resta:.5f}\nValor crítico: {valor_critico:.5f}\n"
    if maxima_resta <= valor_critico:
        resultado += "\nLos números son aceptados."
    else:
        resultado += "\nLos números no son aceptados."

    print(resultado)
    messagebox.showinfo("Resultado de la Prueba KS", resultado)


def main():
    lbl_alpha = tk.Label(ventana, text="α:", bg="lightblue", font=("Helvetica", 16))
    lbl_n = tk.Label(ventana, text="Cantidad de números(N):", bg="lightblue", font=("Helvetica", 16))

    txt_alpha = tk.Entry(ventana)
    txt_n = tk.Entry(ventana)

    btn_generar = tk.Button(ventana, text="Generar", command=lambda: generar(txt_alpha.get(), txt_n.get()), bg="lightgreen")

    lbl_alpha.grid(row=0, column=0, padx=10, pady=10)
    txt_alpha.grid(row=0, column=1, padx=10, pady=10)
    lbl_n.grid(row=1, column=0, padx=10, pady=10)
    txt_n.grid(row=1, column=1, padx=10, pady=10)
    btn_generar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    ventana.mainloop()

def generar(alpha, n):
    try:
        alpha = float(alpha)
        n = int(n)
        if alpha not in [1, 5, 10]:
            messagebox.showerror("Error", "El valor de α debe ser 1, 5 o 10")
            return
        if n <= 0:
            messagebox.showerror("Error", "La cantidad de números debe ser mayor a 0")
            return
        for item in tabla.get_children():
            tabla.delete(item)
        realizar_prueba_ks(alpha, n)
    except ValueError:
        messagebox.showerror("Error", "Los valores ingresados no son válidos")
        return

if __name__ == "__main__":
    main()