import numpy as np
import pandas as pd
import warnings
import tkinter as tk
from tkinter import ttk, messagebox

warnings.simplefilter(action='ignore', category=FutureWarning)

# Define probability distributions
num_trucks_prob = {0: 0.50, 1: 0.25, 2: 0.15, 3: 0.10}
interarrival_times = [20, 25, 30, 35, 40, 45, 50, 55, 60]
interarrival_probs = [0.02, 0.08, 0.12, 0.25, 0.20, 0.15, 0.10, 0.05, 0.03]

service_times_3 = {20: 0.05, 25: 0.10, 30: 0.12, 35: 0.25, 40: 0.20, 45: 0.10, 50: 0.08, 55: 0.06, 60: 0.04}
service_times_4 = {15: 0.05, 20: 0.15, 25: 0.20, 30: 0.20, 35: 0.15, 40: 0.12, 45: 0.08, 50: 0.04, 55: 0.01}
service_times_5 = {10: 0.10, 15: 0.18, 20: 0.22, 25: 0.18, 30: 0.10, 35: 0.08, 40: 0.06, 45: 0.05, 50: 0.03}
service_times_6 = {5: 0.12, 10: 0.15, 15: 0.26, 20: 0.15, 25: 0.12, 30: 0.08, 35: 0.06, 40: 0.04, 45: 0.02}

# Define constants
hourly_rate = 25
overtime_rate = 37.50
truck_wait_cost = 100
warehouse_operating_cost = 500

# Function to get Intervalo de tiempo based on probabilities
def get_interarrival_time():
    rand_num = np.random.random()
    cumulative_prob = 0
    for time, prob in zip(interarrival_times, interarrival_probs):
        cumulative_prob += prob
        if rand_num <= cumulative_prob:
            return rand_num, time

# Function to calculate service time based on team size
def get_service_time(team_size):
    rand_num = np.random.random()
    cumulative_prob = 0
    if team_size == 3:
        for time, prob in service_times_3.items():
            cumulative_prob += prob
            if rand_num <= cumulative_prob:
                return rand_num, time
    elif team_size == 4:
        for time, prob in service_times_4.items():
            cumulative_prob += prob
            if rand_num <= cumulative_prob:
                return rand_num, time
    elif team_size == 5:
        for time, prob in service_times_5.items():
            cumulative_prob += prob
            if rand_num <= cumulative_prob:
                return rand_num, time
    elif team_size == 6:
        for time, prob in service_times_6.items():
            cumulative_prob += prob
            if rand_num <= cumulative_prob:
                return rand_num, time

# Function to simulate the queue system
def simulate_queue(team_size):
    total_cost = 0
    trucks_serviced = 0
    idle_time = 0
    wait_time = 0
    current_time = 0
    truck_queue = []  # Initialize truck queue as a list

    # DataFrame to store results
    results = pd.DataFrame(columns=[
        "Numero de camion", "Numero rectangular (Tiempo de llegada)", "Intervalo de tiempo", 
        "Tiempo de llegada", "Numero rectangular (Tiempo de servicio)", "Tiempo de servico", 
        "Comienzo Tiempo de servico", "Finalizacion Tiempo de servico", "Tiempo de espera del camion", 
        "Cola de camiones"
    ])

    truck_number = 0
    next_service_start_time = 0

    while current_time < 8 * 60:  # 8 hours in minutes
        # Determine number of trucks arriving
        num_trucks = np.random.choice(list(num_trucks_prob.keys()), p=list(num_trucks_prob.values()))

        for _ in range(num_trucks):
            truck_number += 1
            
            # Determine interTiempo de llegada
            rand_num_arrival, interarrival_time = get_interarrival_time()
            current_time += interarrival_time
            arrival_time = current_time

            # Add truck to the queue
            truck_queue.append((truck_number, arrival_time))

        # Process trucks in the queue
        while truck_queue and current_time < 8 * 60:
            if next_service_start_time < truck_queue[0][1]:  # If the next truck arrives after the current time
                next_service_start_time = truck_queue[0][1]

            # Get next truck in queue
            truck_number, arrival_time = truck_queue.pop(0)

            # Determine service time
            rand_num_service, service_time = get_service_time(team_size)
            start_service_time = next_service_start_time
            end_service_time = start_service_time + service_time

            # Check if overtime is required



            trucks_serviced += 1

            # Calculate idle time
            if start_service_time >= 3 * 60 and start_service_time <= 3.5 * 60:
                idle_time += max(0, start_service_time - 3 * 60)
            elif start_service_time > 3.5 * 60:
                idle_time += 30

            # Calculate wait time
            truck_wait_time = max(0, start_service_time - arrival_time)
            wait_time += truck_wait_time

            # Add row to the DataFrame
            new_row = pd.DataFrame({
                "Numero de camion": [truck_number],
                "Numero rectangular (Tiempo de llegada)": [rand_num_arrival],
                "Intervalo de tiempo": [interarrival_time],
                "Tiempo de llegada": [arrival_time],
                "Numero rectangular (Tiempo de servicio)": [rand_num_service],
                "Tiempo de servico": [service_time],
                "Comienzo Tiempo de servico": [start_service_time],
                "Finalizacion Tiempo de servico": [end_service_time],
                "Tiempo de espera del camion": [truck_wait_time],
                "Cola de camiones": [len(truck_queue)]
            })
            results = pd.concat([results, new_row], ignore_index=True)

            # Update next service start time to the end of current service
            next_service_start_time = end_service_time

    # Calculate costs
    total_cost += wait_time * truck_wait_cost / 60
    total_cost += idle_time * hourly_rate / 60
    total_cost += warehouse_operating_cost * 8
    if end_service_time > 8.5 * 60:  # 7:30 AM in minutes
                total_cost += overtime_rate * ((end_service_time - 510) / 60) * team_size
                print(end_service_time)
                print(total_cost)

    total_cost += hourly_rate * (450 / 60) * team_size
    print(total_cost)
    return total_cost, results

# Function to display results
def display_results(total_cost, results):
    results_window = tk.Toplevel(root)
    results_window.title("Resultados de la Simulación")

    text = tk.Text(results_window, wrap='none')
    text.insert(tk.END, "Costo total: ${:.2f}\n\n".format(total_cost))
    text.insert(tk.END, results.to_string(index=False))
    text.pack(expand=True, fill=tk.BOTH)

    scrollbar_y = tk.Scrollbar(results_window, orient=tk.VERTICAL, command=text.yview)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    text.config(yscrollcommand=scrollbar_y.set)

    scrollbar_x = tk.Scrollbar(results_window, orient=tk.HORIZONTAL, command=text.xview)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
    text.config(xscrollcommand=scrollbar_x.set)

# Function to start simulation
def start_simulation():
    try:
        team_size = int(team_size_entry.get())
        if team_size not in [3, 4, 5, 6]:
            raise ValueError("El tamaño del equipo debe ser 3, 4, 5, o 6.")
        total_cost, results = simulate_queue(team_size)
        display_results(total_cost, results)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Main window
root = tk.Tk()
root.title("Simulación de Colas")

# Title Label
title_label = tk.Label(root, text="Simulación de Colas", font=("Helvetica", 16))
title_label.pack(pady=10)

# Explanation Label
explanation = ("Explicación del ejemplo: Una cadena de supermercados es abastecida por un almacén central. "
               "La mercancía llega a este almacén durante la noche. El personal encargado de descargar la mercancía "
               "está formado por un equipo de X personas, las cuales trabajan un turno de 8 horas. El salario por hora "
               "que perciben es de $25. El almacén solo recibe mercancía hasta las 8 1/2 horas de jornada. Si se requiere "
               "tiempo extra para descargar los camiones, el salario percibido será de $37.50 la hora. Finalmente, se "
               "estima que el costo de espera de un camión es de $100 por hora y el costo de tener operando el almacén "
               "es de $500 la hora. Cuando el almacén abre sus puertas a las 11:00 p.m., puede suceder que haya más de "
               "un camión esperando a ser descargado.")
explanation_label = tk.Label(root, text=explanation, wraplength=600, justify="left")
explanation_label.pack(pady=10)

# Team size input
team_size_label = tk.Label(root, text="Escoga la cantidad de personal en el equipo (3, 4, 5, o 6):")
team_size_label.pack(pady=5)

team_size_entry = tk.Entry(root)
team_size_entry.pack(pady=5)

# Start simulation button
start_button = tk.Button(root, text="Iniciar Simulación", command=start_simulation)
start_button.pack(pady=20)

# Run the application
root.mainloop()