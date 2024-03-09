# 🪴 My Plant

Application qui permet de suivre l'évolution d'une plante avec de nombreux capteurs sur le prototype. <br>

* [Prérequis](#requirements)
* [Installation](#installation)
* [Utilisation](#usage)
* [Ressources](#resources)

# PROJET TERMINÉ ET FONCTIONNEL MAIS DOCUMENTATION EN COURS

## Prérequis
- Python
- Mosquitto
- Arduino IDE
- Tkinter
- Matplotlib
  
## Installation

Ouvrez arduino, puis installez les librairies suivantes : 
- DHT sensor library (pour faire fonctionner le capteur de Temps/Humidité DHT22)
- PubSubClient
- Adafruit Unified Sensor
- WiFiNINA
- WiFi101

<img src="https://github.com/itsKevinJM/myplant/assets/90609887/032a1fd1-f98c-49d7-a4ee-6dcb02303e84" width="550px"/>

Maintenant ouvrez une console (en dehors de arduino) et installez le protocole MQTT (Mosquitto) : 

### __Avec Linux :__ 
``sudo apt install mosquitto mosquitto-clients``

* Mosquito est le broker MQTT
* Mosquito-clients installe le client mosquito_sub pour souscrire à un topic et mosquito_pub pour publier un Topic
  
Le broker MQTT se lance au démarrage, vous n'avez pas d'opération à faire pour recevoir et 
émettre des Topics depuis un autre terminal.

> [!WARNING]
> Vous devez autoriser les connexions anonymes. <br>
> Éditez le fichier mosquitto.conf : `sudo nano /etc/mosquitto/mosquitto.conf` <br>
> Puis ajoutez ces deux lignes : <br>
>```
>àllow_anonymous true
>listener 1883
>```

Sauvegardez le fichier, puis relancer le service Mosquitto : `sudo service mosquitto restart`


### __Avec Python :__ 

Pour Python2: `sudo pip install paho-mqtt` ou `sudo apt install python3-paho-mqtt` <br>
Pour Python3: `sudo pip3 install paho-mqtt` ou `sudo apt install python3-paho-mqtt`

La documentation de la libraire se trouve à l'adresse https://pypi.org/project/paho-mqtt/
3.2 La classe Client
La classe Client contient les méthodes pour se connecter/déconnecter au broker, pour publier un message sur 
un topic, pour souscrire/dé-souscrire d'un topic:
• connect() et disconnecte()
• publish()
• subscribe() et unsubscribe ()
Pour utiliser la classe Client vous devez inclure la librairie au début de votre programme
import paho.mqtt.client as mqtt


#### Le prototype :
<img src="https://github.com/itsKevinJM/myplant/assets/90609887/91eca688-7abf-4f7a-a3e4-aac9e5532e16" width="420px"/>
<br>

#### Les différents capteurs :

- un capteur de température
- un capteur d'humidité
- un capteur d'humidité du sol
- un capteur de luminosité.

## Utilisation

2.2 Test du broker Mosquitto en local avec le client sur la Raspberry 
Ouvrir un terminal et taper la commande ci-dessous pour que le client mosquitto souscrive au 
Topic /test/message
$ mosquitto_sub -h localhost -v -t "test/message" 
Le terminal est dans l'attente de recevoir un message sur ce topic
Ouvrir un autre terminal pour publier un message sur ce topic
$ mosquitto_pub -h localhost -t "test/message" -m "Coucou"
Vous devez voir s'afficher sur le terminal de souscription au Topic le message Coucou

<img src="https://github.com/itsKevinJM/myplant/assets/90609887/e4a19761-51fa-4555-acae-845b20781687" width="420px"/>
<img src="https://github.com/itsKevinJM/myplant/assets/90609887/de6f740f-4d41-41ce-a42a-28c6f9ace506" width="900px"/> 

## Ressources
https://wiki.seeedstudio.com/Grove-Moisture_Sensor/ <br>
https://wiki.seeedstudio.com/Grove-Temperature_and_Humidity_Sensor_Pro/


