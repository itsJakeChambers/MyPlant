import paho.mqtt.client as mqtt
import time

# MQTT settings
MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "data_plant"

# Fonction pour publier les données
def publish_data(temperature, ambient_humidity, soil_humidity, light):
    data = f"{temperature},{ambient_humidity},{soil_humidity},{light}"
    publish.single(MQTT_TOPIC, payload=data, hostname=MQTT_BROKER, port=MQTT_PORT)

# Fonction pour gérer les messages entrants
def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8").split(",")
    temperature = float(data[0])
    ambient_humidity = float(data[1])
    soil_humidity = float(data[2])
    light = float(data[3])

    # Publier les données
    print(f"Temperature: {temperature}°C, Ambient Humidity: {ambient_humidity}%, Soil_humidity: {soil_humidity}%, Light: {light}")

# Créer une instance MQTT client
client = mqtt.Client()

# Attribuer une fonction de rappel pour gérer les messages entrants
client.on_message = on_message

# Se connecter au MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT)

# S'abonner au sujet MQTT
client.subscribe(MQTT_TOPIC)

# Démarrer la boucle de message MQTT
client.loop_forever()

    # Attendre un certain temps avant d'envoyer les prochaines données
    # time.sleep(10)  # attendre 10 secondes avant d'envoyer de nouvelles données

