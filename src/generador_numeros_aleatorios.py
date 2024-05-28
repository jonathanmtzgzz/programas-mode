import tkinter as tk
import random

# Función para generar números aleatorios
def generar_numeros():
    cantidad = int(entry.get())
    numeros = [round(random.random(), 5) for _ in range(cantidad)]
    resultado.config(state=tk.NORMAL)
    resultado.delete(1.0, tk.END)
    for i, numero in enumerate(numeros):
        resultado.insert(tk.END, f"{numero}")
        if i != len(numeros) - 1:
            resultado.insert(tk.END, "\n")
    resultado.config(state=tk.DISABLED)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador De Números Aleatorios")

# Configuración del diseño principal
ventana.geometry("600x600")
ventana.configure(background="lightblue")

# Crear y colocar widgets
tk.Label(ventana, text="Cantidad de números a generar:").pack(pady=5)
entry = tk.Entry(ventana)
entry.pack(pady=5)
entry.insert(0, "")
entry.configure(background="white")

tk.Button(ventana, text="Generar", command=generar_numeros).pack(pady=10)

resultado = tk.Text(ventana, state=tk.DISABLED)
resultado.pack(pady=5, padx=5,  fill=tk.BOTH, expand=True)
resultado.configure(background="white")

# Iniciar el bucle principal de la interfaz
ventana.mainloop()