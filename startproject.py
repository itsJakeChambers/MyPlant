import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import paho.mqtt.client as mqtt
from tkinter import Label
import time

# MQTT settings
MQTT_BROKER = "192.168.60.166"
MQTT_PORT = 1883
MQTT_TOPIC = "data_plant1"

# Data lists for plotting
timestamps = []
temperatures = []
ambient_humidities = []
soil_humidities = []
lights = []

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload}")
    # Update data lists
    data = str(msg.payload.decode("utf-8")).split(",")
    timestamp = time.time() # Ajout de l'horodotage actuel
    timestamps.append(timestamp) # Ajout de l'horodotage à la liste des horodotages
    temperatures.append(float(data[0]))  # Temperature data
    ambient_humidities.append(float(data[1]))  # Ambient humidity data
    soil_humidities.append(float(data[2]))  # Soil humidity data
    lights.append(float(data[3]))  # Light data

    print("Timestamps:", timestamps)
    print("Temperatures:", temperatures)
    print("Ambient Humidities:", ambient_humidities)
    print("Soil Humidities:", soil_humidities)
    print("Lights:", lights)
    # Update UI
    update_ui()

# Update UI
def update_ui():
    # Mise à jour du texte des boutons avec les dernières valeurs des données
    button_temp.config(text=f"Temperature: {temperatures[-1]}°C 🌡️")
    button_ambient_humidity.config(text=f"Ambient Humidity: {ambient_humidities[-1]}% 💧")
    button_soil_humidity.config(text=f"Soil Humidity: {soil_humidities[-1]}% 🌱")
    button_light.config(text=f"Light: {lights[-1]} 💡")

# Functions to show graphs
def show_temperature_graph():
    if len(timestamps) > 1:
        plt.figure(figsize=(6, 4))
        plt.plot(timestamps, temperatures, marker='o', color='blue')
        plt.xlabel('Time')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature')
        plt.grid(True)
        plt.show()
    else: 
        print("Pas assez de données pour tracer le graphique de température.")

def show_ambient_humidity_graph():
    if len(timestamps) > 1:
        plt.figure(figsize=(6, 4))
        plt.plot(timestamps, ambient_humidities, marker='o', color='green')
        plt.xlabel('Time')
        plt.ylabel('Ambient Humidity (%)')
        plt.title('Ambient Humidity')
        plt.grid(True)
        plt.show()
    else: 
        print("Pas assez de données pour tracer le graphique de température.")

def show_soil_humidity_graph():
    if len(timestamps) > 1:
        plt.figure(figsize=(6, 4))
        plt.plot(timestamps, soil_humidities, marker='o', color='orange')
        plt.xlabel('Time')
        plt.ylabel('Soil Humidity (%)')
        plt.title('Soil Humidity')
        plt.grid(True)
        plt.show()
    else: 
        print("Pas assez de données pour tracer le graphique de température.")

def show_light_graph():
    if len(timestamps) > 1:
        plt.figure(figsize=(6, 4))
        plt.plot(timestamps, lights, marker='o', color='red')
        plt.xlabel('Time')
        plt.ylabel('Light')
        plt.title('Light')
        plt.grid(True)
        plt.show()
    else: 
        print("Pas assez de données pour tracer le graphique de température.")

# MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# UI setup
root = tk.Tk()
root.title("Plant Monitoring App")

# Main frame
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Subframes
frame_temp = tk.Frame(main_frame, width=200, height=200)
frame_temp.grid(row=0, column=0)
frame_ambient_humidity = tk.Frame(main_frame, width=200, height=200)
frame_ambient_humidity.grid(row=0, column=1)
frame_soil_humidity = tk.Frame(main_frame, width=200, height=200)
frame_soil_humidity.grid(row=1, column=0)
frame_light = tk.Frame(main_frame, width=200, height=200)
frame_light.grid(row=1, column=1)

# Define function to add emoji label
def add_emoji_label(frame, temperature):
    emoji = "🙂" if 10 <= temperature <= 30 else "🥵"
    emoji_label = Label(frame, text=emoji, font=("Arial", 40))
    emoji_label.pack(side=tk.LEFT)


# Buttons with values and emoji labels

add_emoji_label(frame_temp, 25)
button_temp = tk.Button(frame_temp, text=f"Temperature: N/A°C 🌡️", command=show_temperature_graph, font=("Arial", 30))
button_temp.pack(expand=True)

add_emoji_label(frame_ambient_humidity, 25)
button_ambient_humidity = tk.Button(frame_ambient_humidity, text=f"Ambient Humidity: N/A% 💧", command=show_ambient_humidity_graph, font=("Arial", 30))
button_ambient_humidity.pack(expand=True)

add_emoji_label(frame_soil_humidity, 4)
button_soil_humidity = tk.Button(frame_soil_humidity, text=f"Soil Humidity: N/A% 🌱", command=show_soil_humidity_graph, font=("Arial", 30))
button_soil_humidity.pack(expand=True)

add_emoji_label(frame_light, 25)
button_light = tk.Button(frame_light, text=f"Light: 8 💡", command=show_light_graph, font=("Arial", 30))
button_light.pack(expand=True)

# Start MQTT client loop
client.loop_start()

# Run UI loop
root.mainloop()
