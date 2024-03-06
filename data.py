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

# Callback function to handle incoming MQTT messages
def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8").split(",")
    temperature = float(data[0])
    ambient_humidity = float(data[1])
    soil_humidity = float(data[2])
    light = float(data[3])

    # Publier les données
    print(f"Temperature: {temperature}°C, Ambient Humidity: {ambient_humidity}%, Soil_humidity: {soil_humidity}%, Light: {light}")

# Create MQTT client instance
client = mqtt.Client()

# Assign callback function to handle incoming messages
client.on_message = on_message

# Connect to MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT)

# Subscribe to MQTT topic
client.subscribe(MQTT_TOPIC)

# Start the MQTT message loop
client.loop_forever()

    # # Attendre un certain temps avant d'envoyer les prochaines données
    # time.sleep(10)  # attendre 10 secondes avant d'envoyer de nouvelles données
