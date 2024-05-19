import tkinter as tk
from tkinter import *
import os

def abrir_gcm():
    os.system(r'python .\src\generador_congruencial_multiplicativo.py')

def abrir_gcmx():
    os.system(r'python .\src\generador_congruencial_mixto.py')

def abrir_dex():
    os.system(r'python .\src\distribucion_exponencial.py')

def abrir_dun():
    os.system(r'python .\src\distribucion_uniforme.py')

ventana_principal = tk.Tk()
ventana_principal.title("Programa de Modelado y Simulacion")
# ventana_principal.minsize(717, 690)
ventana_principal.resizable(False, True)
ventana_principal.config(padx=50, pady=20)

uanl_logo = PhotoImage(file=".\\src\\img\\uanl_logo.png")
fime_logo = PhotoImage(file=".\\src\\img\\fime_logo.png")

label_logo_uanl = tk.Label(ventana_principal, image=uanl_logo)
label_logo_fime = tk.Label(ventana_principal, image=fime_logo)
label_logo_uanl.grid(row=0, column=0, sticky='e')
label_logo_fime.grid(row=0, column=4, sticky='w')

label1 = tk.Label(ventana_principal, text="""Universidad Autonoma de Nuevo Leon\nFacultad de Ingenieria Mecanica y Electrica""", font=("Arial", 14))
label1.grid(row=0, column=1, padx=5, columnspan=3, sticky='ew')

label2 = tk.Label(ventana_principal, text="Equipo #1", font=("Arial", 14))
label2.grid(row=1, column=1, columnspan=3, sticky='ew')

label3 = tk.Label(ventana_principal, text="Programa en el cual se encuentran los\nTemas vistos en la clase de Modelado y Simulacion", font=("Arial", 14))
label3.grid(row=2, column=1, pady=20, columnspan=3)

boton_gcm = tk.Button(ventana_principal, text="GCM", command=abrir_gcm, font=("Arial", 12), bg='white', fg='black')
boton_gcm.grid(row=4, column=1)
label4 = tk.Label(ventana_principal, text="Generador\nCongruencial\nMultiplicativo", font=("Arial", 12))
label4.grid(row=5, column=1)

boton_gcmx = tk.Button(ventana_principal, text="GCMX", command=abrir_gcmx, font=("Arial", 12), bg='white', fg='black')
boton_gcmx.grid(row=4, column=2)
label5 = tk.Label(ventana_principal, text="Generador\nCongruencial\nMixto", font=("Arial", 12))
label5.grid(row=5, column=2)

boton_ps = tk.Button(ventana_principal, text="PS", command="", font=("Arial", 12), bg='white', fg='black')
boton_ps.grid(row=4, column=3, pady=10)
label9 = tk.Label(ventana_principal, text="Prueba de\nSeries", font=("Arial", 12))
label9.grid(row=5, column=3)

boton_pp = tk.Button(ventana_principal, text="PP", command="", font=("Arial", 12), bg='white', fg='black')
boton_pp.grid(row=6, column=1, pady=10)
label6 = tk.Label(ventana_principal, text="Prueba de\nPromedio", font=("Arial", 12))
label6.grid(row=7, column=1)

boton_pks = tk.Button(ventana_principal, text="PKS", command="", font=("Arial", 12), bg='white', fg='black')
boton_pks.grid(row=6, column=2, pady=10)
label7 = tk.Label(ventana_principal, text="Prueba de\nKolmogorov-Smirnov", font=("Arial", 12))
label7.grid(row=7, column=2)

boton_pf = tk.Button(ventana_principal, text="PF", command="", font=("Arial", 12), bg='white', fg='black')
boton_pf.grid(row=6, column=3, pady=10)
label8 = tk.Label(ventana_principal, text="Prueba de\nFrecuencias", font=("Arial", 12))
label8.grid(row=7, column=3)

boton_dex = tk.Button(ventana_principal, text="DEX", command=abrir_dex, font=("Arial", 12), bg='white', fg='black')
boton_dex.grid(row=8, column=1, pady=10)
label9 = tk.Label(ventana_principal, text="Distribucion\nExponencial", font=("Arial", 12))
label9.grid(row=9, column=1)

boton_dun = tk.Button(ventana_principal, text="DUN", command=abrir_dun, font=("Arial", 12), bg='white', fg='black')
boton_dun.grid(row=8, column=2, pady=10)
label10 = tk.Label(ventana_principal, text="Distribucion\nUniforme", font=("Arial", 12))
label10.grid(row=9, column=2)

boton_dp = tk.Button(ventana_principal, text="DP", command="", font=("Arial", 12), bg='white', fg='black')
boton_dp.grid(row=8, column=3, pady=10)
label11 = tk.Label(ventana_principal, text="Distribucion de\nPoisson", font=("Arial", 12))
label11.grid(row=9, column=3)

espacio = tk.Label(ventana_principal, text="")
espacio.grid(row=10, column=2)

boton_salir = tk.Button(ventana_principal, text="Salir", command=ventana_principal.quit, font=("Arial", 12), bg='firebrick', fg='white')
boton_salir.grid(row=11, column=2, pady=10)


ventana_principal.mainloop()
