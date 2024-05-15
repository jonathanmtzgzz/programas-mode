import tkinter as tk
from tkinter import ttk
from math import log10
from tkinter import messagebox

# generar interfaz grafica
ventana = tk.Tk()
ventana.title("Generador Congruencial Multiplicativo")
ventana.geometry("560x500")
ventana.configure(bg="lightblue")

table_placeholder = ttk.Treeview(ventana, columns=('#1', '#2', '#3', '#4', '#5'))

def congruencial_multiplicativo(a, m, x0):
    xn = x0
    secuencia = []
    print("  n | Xn | ax0mod m | Xn+1 | Numero Rectangular")
    i = 0
    xnplus1 = None
    tabla = ttk.Treeview(ventana, columns=('#1', '#2', '#3', '#4', '#5'))
    tabla.column('#0', width=0, stretch=tk.NO)
    tabla.column('#1', width=50, anchor=tk.CENTER)
    tabla.column('#2', width=100, anchor=tk.CENTER)
    tabla.column('#3', width=150, anchor=tk.CENTER)
    tabla.column('#4', width=100, anchor=tk.CENTER)
    tabla.column('#5', width=150, anchor=tk.CENTER)
    tabla.heading('#1', text='n')
    tabla.heading('#2', text='Xn')
    tabla.heading('#3', text='(ax0)mod m')
    tabla.heading('#4', text='Xn+1')
    tabla.heading('#5', text='Numero Rectangular')
    # calculate the expected period of the generator
    # when is binary or decimal
    # if modulus is a power of 2

    if (m & (m - 1)) == 0:
        expected_period = m // 4
    elif m % 10 == 0:
        d = log10(m)
        if d >= 5:
            expected_period = 5 * 10 ** (d - 2)
        else:
            l5 = (5 ** (d - 1)) * (5 - 1)
            l2 = 1 if d == 1 else 2 if d == 2 else 2 ** (d - 2)
            print(l5, l2)
            expected_period = minimo_comun_multiplo(l5, l2)
    else:
        print("El periodo esperado no se puede calcular, debido a que el modulo no es binario o decimal")

    print("El periodo esperado es:", expected_period)
    while i < expected_period and xnplus1 != x0:
        xnplus1 = (a * xn) % m
        print(f"{str(i + 1).center(4)}|{str(xn).center(4)}| {(str((a * xn) // m) + ' + '+ str(xnplus1) + '/' + str(m)).center(13)}|{str(xnplus1).center(6)}| {(xnplus1/m):.5f}")
        # mostrar en la interfaz grafica la tabla de resultados
        # Crear tabla
        tabla.insert('', 'end', text=str(i + 1), values=(i + 1, xn, f"{(a * xn) // m} + {xnplus1} / {m}", xnplus1, f"{xnplus1}/{m} = {(xnplus1/m):.5f}"))
        tabla.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        ventana.update()

        xn = xnplus1
        secuencia.append(xn / m)
        i += 1

    if xnplus1 == x0:
        if i == expected_period:
            print("El generador es de periodo completo")
        else:
            print(f"El generador es de periodo incompleto, su periodo es {i}")
    else:
        print('El generador congruencial multiplicativo es no confiable')
    return secuencia

def main():

    # Crear etiquetas
    lbl_a = tk.Label(ventana, text="a:", bg="lightblue")
    lbl_x0 = tk.Label(ventana, text="x0:", bg="lightblue")
    lbl_m = tk.Label(ventana, text="m:", bg="lightblue", width=20)

    # Crear campos de texto
    txt_a = tk.Entry(ventana)
    txt_x0 = tk.Entry(ventana)
    txt_m = tk.Entry(ventana)

    # Crear botón
    btn_generar = tk.Button(ventana, text="Generar", command=lambda: generar(txt_a.get(), txt_m.get(), txt_x0.get()), bg="lightgreen")

    # Añadir elementos a la ventana de forma que queden centrados
    lbl_a.grid(row=0, column=0, padx=10, pady=10)
    txt_a.grid(row=0, column=1, padx=10, pady=10)
    lbl_x0.grid(row=1, column=0, padx=10, pady=10)
    txt_x0.grid(row=1, column=1, padx=10, pady=10)
    lbl_m.grid(row=3, column=0, padx=10, pady=10)
    txt_m.grid(row=3, column=1, padx=10, pady=10)
    btn_generar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Mostrar ventana
    ventana.mainloop()

def generar(a, m, x0):
    try:
        a = int(a)
        m = int(m)
        x0 = int(x0)
        if not verify_constraints(a, m, x0):
            print("Los valores ingresados no son válidos")
            return
        congruencial_multiplicativo(a, m, x0)
    except ValueError:
        messagebox.showerror("Error", "Los valores ingresados no son válidos")
        return


def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

def minimo_comun_multiplo(a, b):
    return a * b // maximo_comun_divisor(a, b)

def input_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número entero")

def verify_constraints(a, m, x0):
    if m <= 0:
        messagebox.showerror("Error", "El valor de m debe ser mayor a 0")
        return False
    if a <= 0:
        messagebox.showerror("Error", "El valor de a debe ser mayor o igual a 0")
        return False
    if x0 < 0:
        messagebox.showerror("Error", "El valor de x0 debe ser mayor o igual a 0")
        return False
    if m <= a:
        messagebox.showerror("Error", "El valor de m debe ser mayor a a")
        return False
    if m <= x0:
        messagebox.showerror("Error", "El valor de m debe ser mayor a x0")
        return False
    return True
if __name__ == "__main__":
    main()

