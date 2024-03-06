import paho.mqtt.publish as publish
import time

# MQTT settings
MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "data_pant"

# Fonction pour publier les données
def publish_data(temperature, ambient_humidity, soil_humidity, light):
    data = f"{temperature},{ambient_humidity},{soil_humidity},{light}"
    publish.single(MQTT_TOPIC, payload=data, hostname=MQTT_BROKER, port=MQTT_PORT)

# Boucle pour envoyer des données factices
while True:
    # fausse données
    temperature = 25.5
    ambient_humidity = 60.0
    soil_humidity = 35.0
    light = 8

    # Publier les données
    publish_data(temperature, ambient_humidity, soil_humidity, light)

    # Attendre un certain temps avant d'envoyer les prochaines données
    time.sleep(10)  # attendre 10 secondes avant d'envoyer de nouvelles données
