import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import math

# generar interfaz grafica
ventana = tk.Tk()
ventana.title("Juego de Volados")
ventana.resizable(False, True)
ventana.config(padx=50, pady=20)



table_placeholder = ttk.Treeview(ventana, columns=('#1', '#2', '#3', '#4', '#5'))
def generar_numero_rectangular():
    numero = round(random.uniform(0, 1), 5)
    return numero
def mostrarFinal(vecesMeta, vecesQuiebra, noCorrida):
    numCorridas         = noCorrida -1
    if numCorridas == 0:
        probabilidadMeta = 0
        probabilidadQuiebra = 0
    else:
        probabilidadMeta    = round((vecesMeta / numCorridas) * 100, 2)
        probabilidadQuiebra = round((vecesQuiebra / numCorridas) * 100, 2)
    wrap_length         = screen_width - (screen_width*0.50)
    lbl_Final = tk.Label(
        ventana, 
        text=("Probabilidad de llegar a la meta: "+ str(probabilidadMeta)+ "% \tNo. Metas: " + str(vecesMeta)+
              "\nProbabilidad de llegar a la quiebra: "+str(probabilidadQuiebra)+ "% \tNo. Quiebras: " + str(vecesQuiebra)+
              "\nNumero de Corridas: "+str(numCorridas)
              
              ),
            font=("Arial", 12),
            wraplength=wrap_length,
        justify='left'  # Opcional, para justificar el texto a la izquierda
    )
    lbl_Final.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    return
    

def juegoVolados(tipo, cantidad):
    
    i = 0
    tabla = ttk.Treeview(ventana, columns=('#1', '#2', '#3', '#4', '#5','#6','#7'),  show='headings')
    tabla.column('#0', width=0, stretch=tk.NO)
    tabla.column('#1', width=100, anchor=tk.CENTER)
    tabla.column('#2', width=100, anchor=tk.CENTER)
    tabla.column('#3', width=150, anchor=tk.CENTER)
    tabla.column('#4', width=100, anchor=tk.CENTER)
    tabla.column('#5', width=150, anchor=tk.CENTER)
    tabla.column('#6', width=150, anchor=tk.CENTER)
    tabla.column('#7', width=150, anchor=tk.CENTER)
    # Configurar el estilo para permitir saltos de línea en los encabezados
    tabla.heading('#1', text='Numero de Corrida')
    tabla.heading('#2', text='Cantidad que se tiene antes del volado')
    tabla.heading('#3', text='Apuesta')
    tabla.heading('#4', text='Numero Aleatorio')
    tabla.heading('#5', text='¿Se ganó el volado?')
    tabla.heading('#6', text='Cantidad que se tiene después del volado')
    tabla.heading('#7', text='Se llegó a la meta')
    vecesMeta           = 0
    vecesQuiebtra       = 0
    noCorrida           = 1
    cantidadVolados     = 0
    while noCorrida <= cantidad:
        cantidadAntes   = 50
        apuesta         = 10
        gana            = "Sí"
        cantidadDespues = 50
        meta            = 0
        no_rectangular  = 0
        i=0
        meta = 0
        while meta == 0:
            if tipo ==2 and cantidadVolados>= cantidad:
                return mostrarFinal(vecesMeta, vecesQuiebtra, noCorrida)
            cantidadVolados += 1
            mostarApuesta = apuesta
            no_rectangular  = generar_numero_rectangular()
            if no_rectangular <=0.5:
                gana = "Sí"
                cantidadDespues = cantidadDespues + apuesta
                apuesta = 10
            else:
                gana = "No"
                cantidadDespues = cantidadDespues - apuesta
                if (cantidadDespues - (apuesta * 2) <= 0):
                    apuesta = cantidadDespues
                else:
                    apuesta = apuesta * 2
                    
            if(cantidadDespues<=0):
                mostrarMeta = "QUIEBRA"
                vecesQuiebtra +=1
                meta = 1
            elif cantidadDespues >=80:
                mostrarMeta = "META"
                vecesMeta += 1
                meta = 2
            else:
                mostrarMeta = "-"
            if(i==0):
                mostrarCorrida = str(noCorrida)
            else:
                mostrarCorrida = "-"
            # Crear tabla
            tabla.insert('', 'end', text=str(i + 1), 
                        values=(
                            mostrarCorrida,                                      #Valor Columna 1
                            str(cantidadAntes),                                         #Valor Columna 2
                            str(mostarApuesta),                                       #Valor Columna 3
                            str(no_rectangular),   #Valor Columna 4
                            gana,                                    #Valor Columna 5
                            str(cantidadDespues),
                            str(mostrarMeta)
                            ))
            tabla.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
            ventana.update()
            i += 1
            cantidadAntes = cantidadDespues
            

        noCorrida += 1
    print(cantidadVolados)
    return mostrarFinal(vecesMeta, vecesQuiebtra, noCorrida)
    
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
def main():
    # Obtener las dimensiones de la pantalla
    
    # Establecer el tamaño máximo de la ventana
    ventana.maxsize(screen_width, screen_height)
    # Crear etiquetas
    lbl_titulo = tk.Label(ventana, 
                               text="*** Juego de Volados ***",
                               font=("Arial", 18),
                               )
    # Definir la longitud de envoltura (wraplength) en píxeles
    wrap_length = screen_width - (screen_width*0.50)
    # Crear el Label con el texto largo y la propiedad wraplength
    lbl_explicacion = tk.Label(
        ventana, 
        text=("Explicación: Se tiene una cantidad inicial de $50 y se quiere llegar a la meta de $80, "
            "con una apuesta de $10, la puesta inicial es de $X, si se pierde se apuesta $2X y así sucesivamente. "
            "Se gana el volado cuando el número aleatorio es menor o igual a 0.5 y se pierde cuando es mayor a este. "
            "Al final el programa muestra: ¿Cuál es la probabilidad de llegar a la meta?, ¿Cuántas veces se llegó a la "
            "meta y cuántas veces a la quiebra?, ¿Cuántas corridas se realizaron?"),
            font=("Arial", 12),
            wraplength=wrap_length,
        justify='left'  # Opcional, para justificar el texto a la izquierda
    )
    #radio buttons
    opcion_seleccionada = tk.IntVar()
    opcion_seleccionada.set(1) 
    
    
    
    # make width of the label to 200px
    lbl_cantidad = tk.Label(ventana, text="Cantidad:", font=("Arial", 12), bg="lightblue")
    lbl_tipo = tk.Label(ventana, text="Escoge si quieres correr el programa por numero de volados o por numero de corridas:",
                        font=("Arial", 12),
                        wraplength=400,
                        justify='left',
                        bg="lightblue")

    # Crear campos de texto
    inpt_cantidad = tk.Entry(ventana)
    
    # Crear botón
    btn_generar = tk.Button(ventana, text="Generar", 
                            command=lambda: 
                            generar(
                                   
                                opcion_seleccionada.get(),
                                inpt_cantidad.get(),     
                                ),  
                            bg="lightgreen")

    # Añadir elementos a la ventana de forma que queden centrados
    lbl_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    lbl_explicacion.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    #Campos de entrada
    lbl_tipo.grid(row=2, column=0, padx=10, pady=10)
    contenedor_radio = tk.Frame(ventana)
    # Crear los radio buttons dentro del contenedor
    radio1 = tk.Radiobutton(contenedor_radio, text="No. de corridas", font=("Arial", 12), variable=opcion_seleccionada, value=1)
    radio2 = tk.Radiobutton(contenedor_radio, text="No. de volados",  font=("Arial", 12), variable=opcion_seleccionada, value=2)
    
    radio1.grid(row=0, column=0, padx=(0, 10))  # Se ajusta el padding solo en el lado derecho
    radio2.grid(row=1, column=0, padx=(0, 10)) 

    # Colocar el contenedor en la misma celda de la cuadrícula
    contenedor_radio.grid(row=2, column=1, padx=10, pady=10)
    lbl_cantidad.grid(row=3, column=0, padx=10, pady=10)
    inpt_cantidad.grid(row=3, column=1, padx=10, pady=10)
    
    #Boton
    btn_generar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    

    # Mostrar ventana
    ventana.mainloop()

def generar(tipo, cantidad):
    try:
        a = int(tipo)
        b = int(cantidad)
        if not verify_constraints(a, b):
            print("Los valores ingresados no son válidos")
            return
        juegoVolados(a, b)
    except ValueError:
        messagebox.showerror("Error", "Los valores ingresados no son válidos")
        return

def verify_constraints(a, b):
    if b <= 0:
        messagebox.showerror("Error", "El valor de la cantidad debe ser mayor a 0")
        return False
    if a <= 0:
        messagebox.showerror("Error", "El valor de a debe ser mayor o igual a 0")
        return False
    return True
if __name__ == "__main__":
    main()

