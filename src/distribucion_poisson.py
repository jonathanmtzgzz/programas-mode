import random
from scipy.stats import chi2  # Import for Chi-squared critical value
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
numRowActual = 0
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()




def generar_numero_rectangular():
    numero = round(random.uniform(0, 1), 5)
    return numero

    
def generar_numeros_rectangulares(n):
    numeros_rectangulares = []
    for _ in range(n):
        numero = round(random.uniform(0, 1), 5)
        numeros_rectangulares.append(numero)
    return numeros_rectangulares
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
def juegoVolados(varLambda):
    numeros_rectangulares = generar_numeros_rectangulares(varLambda)
    numCoridas = len(numeros_rectangulares)
    tabla = ttk.Treeview(ventana, columns=('#1', '#2',),  show='headings')
    tabla.column('#0', width=0, stretch=tk.NO)
    tabla.column('#1', width=100, anchor=tk.CENTER)
    tabla.column('#2', width=200, anchor=tk.CENTER)
    
      
    # Configurar el estilo para permitir saltos de línea en los encabezados
    tabla.heading('#1', text='#')
    tabla.heading('#2', text='Numero Aleatorio (R)')
    i=0
    while i<numCoridas:
      a = i +1
      #Validacion en X
      j=0
      
      
      tabla.insert('', 'end', text=str(i + 1), 
                          values=(
                              i+1,
                              numeros_rectangulares[i],
                              "a",
                              "d",
                              ))
      tabla.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
      i+=1
      ventana.update()
    # Configurar el estilo para permitir saltos de línea en los encabezados
    tablaD = ttk.Treeview(ventana, columns=('#1', '#2','#3','#4',),  show='headings')
    tablaD.column('#0', width=0, stretch=tk.NO)
    tablaD.column('#1', width=100, anchor=tk.CENTER)
    tablaD.column('#2', width=100, anchor=tk.CENTER)
    tablaD.column('#3', width=100, anchor=tk.CENTER)
    tablaD.column('#4', width=100, anchor=tk.CENTER)
    tablaD.heading('#1', text='#')
    tablaD.heading('#2', text='Si R >')
    tablaD.heading('#3', text='y Si R es <= ')
    tablaD.heading('#4', text='x ')
    i=0
    numAcumulados = []
    numAcumulado = 0
    x=0
    while numAcumulado<=0.99999:
      #Calculos
      parte_exponencial = math.exp(-varLambda)
      parte_potencia = math.pow(varLambda, x)
      parte_factorial = math.factorial(x)
      numCalculado = (parte_exponencial * parte_potencia)/parte_factorial
      numAcumulado = numAcumulado + numCalculado
      numAcumulados.append(numAcumulado)
      limiteBajo = 0
      limiteAlto = numAcumulados[i]
      if numAcumulados !=[]:
          limiteBajo = numAcumulados[i-1]
      #Validacion en X
      j=0
      tablaD.insert('', 'end', text=str(i + 1), 
                          values=(
                              i+1,
                              limiteBajo,
                              limiteAlto,
                              str(x),
                              ))
      tablaD.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
      i+=1
      x = x +1
      ventana.update()
def main():
    ventana.maxsize(screen_width, screen_height)
    # Crear etiquetas
    lbl_titulo = tk.Label(ventana, 
                               text="*** Distribución Poisson ***",
                               font=("Arial", 18),
                               )
    # Definir la longitud de envoltura (wraplength) en píxeles
    wrap_length = screen_width - (screen_width*0.50)
    # make width of the label to 200px
    lbl_alfa = tk.Label(ventana, text="Ingresa el la cantidad de lambda:", font=("Arial", 12), bg="lightblue")
    # Crear campos de texto
    inpt_lambda = tk.Entry(ventana)
    # Crear botón
    btn_generar = tk.Button(ventana, text="Generar", 
                            command=lambda: 
                            generar(
                                   inpt_lambda.get(),  
                                ),  
                            bg="lightgreen")

    lbl_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    lbl_alfa.grid(row=1, column=0, columnspan=1, padx=10, pady=10)
  
    # Crear campos de texto
    inpt_lambda.grid(row=1, column=2, columnspan=1, padx=10, pady=10)
    #Boton
    btn_generar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    # Mostrar ventana
    ventana.mainloop()

def generar(n):
    try:
        a = int(n)
       
        if not verify_constraints(a):
            print("Los valores ingresados no son válidos")
            return
        juegoVolados(a)
    except ValueError:
        messagebox.showerror("Error", "Los valores ingresados no son válidos")
        return

def verify_constraints(a):
    if a <= 0:
        messagebox.showerror("Error", "El valor de n debe ser mayor o igual a 0")
        return False
   
    return True
if __name__ == "__main__":
    main()

