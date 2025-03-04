# 🪴 My Plant

Application that allows to follow the evolution of a plant with many sensors on the prototype. <br>

[Prerequisites](#prerequisites)<br>
[Installation](#installation)<br>
[Usage](#usage)<br>
[Result](#result)<br>
[Resources](#resources)<br>
  <br>
>[!IMPORTANT]
>## Prerequisites
>- Python
>- Mosquitto
>- Arduino IDE
>- Tkinter
>- Matplotlib
  
## Installation

Open arduino, then install the following libraries :
- DHT sensor library (to run the DHT22 Time/Humidity sensor)
- PubSubClient
- Adafruit Unified Sensor
- WiFiNINA
- WiFi101

<img src="https://github.com/itsKevinJM/myplant/assets/90609887/032a1fd1-f98c-49d7-a4ee-6dcb02303e84" width="550px"/>

Now open a console (outside arduino) and install the MQTT protocol (Mosquitto) : 

### __With Linux :__ 
``sudo apt install mosquitto mosquitto-clients``

* Mosquito is the MQTT broker
* Mosquito-clients installs the Mosquito_sub client to subscribe to a topic and Mosquito_pub to publish a topic
  
The MQTT broker starts at startup, you do not have to do anything to receive and issue Topics from another terminal.

> [!WARNING]
> You must allow anonymous connections. <br>
> Edit the mosquitto.conf file : `sudo nano /etc/mosquitto/mosquitto.conf` <br>
> Then add these two lines : <br>
>```
>àllow_anonymous true
>listener 1883
>```

Save the file, then restart the Mosquitto service: sudo service mosquitto restart : `sudo service mosquitto restart`


### __With Python :__ 

For Python2: `sudo pip install paho-mqtt` or `sudo apt install python3-paho-mqtt` <br>
For Python3: `sudo pip3 install paho-mqtt` or `sudo apt install python3-paho-mqtt`

The library documentation can be found at https://pypi.org/project/paho-mqtt/.

The Client class contains the methods to connect/disconnect to the broker, to publish a message on a topic, to subscribe/unsubscribe from a topic :

- connect() and disconnect()
- publish()
- subscribe() and unsubscribe ()

To use the Client class you must include the library at the beginning of your program : `import paho.mqtt.client as mqtt`<br>
![Capture du 2024-03-10 00-22-17](https://github.com/itsKevinJM/myplant/assets/90609887/f0bbe8c9-05e0-423c-9e3d-b06a1ea9c8e2)


#### The prototype :
<img src="https://github.com/itsKevinJM/myplant/assets/90609887/91eca688-7abf-4f7a-a3e4-aac9e5532e16" width="420px"/>
<br>

>[!NOTE]
>#### The different sensors :
> - a temperature sensor
> - a humidity sensor
> - a soil humidity sensor
> - a brightness sensor

## Usage

Test the Mosquitto broker locally with the client on the Raspberry. 
Open a terminal and type the command : `mosquitto_sub -h localhost -v -t "test/message` so that the mosquitto client subscribes to the Topic /test/message.
The terminal is waiting to receive a message on this topic
<br><br>
Open another terminal and type the command : `mosquitto_pub -h localhost -t "test/message" -m "Coucou"` to publish a message on this topic.

__You should see the message "Coucou" displayed on the terminal subscribing to the Topic__
![Capture du 2024-03-10 00-47-13](https://github.com/itsKevinJM/myplant/assets/90609887/7724dc42-d10d-4bb1-86e2-0df449820409)

## Result

### __Prototype and sensors connected to our plant :__ <br>
<img src="https://github.com/itsKevinJM/myplant/assets/90609887/e4a19761-51fa-4555-acae-845b20781687" width="420px"/>
<br><br>

### __Graphical display of our application with real-time data :__ <br>
<img src="https://github.com/itsKevinJM/myplant/assets/90609887/de6f740f-4d41-41ce-a42a-28c6f9ace506" width="900px"/> 

## Resources
https://mosquitto.org/man/mosquitto_sub-1.html
https://pypi.org/project/paho-mqtt/
https://pypi.org/project/paho-mqtt/#constructor-reinitialise
https://docs.arduino.cc/libraries/pubsubclient/
https://wiki.seeedstudio.com/Grove-Moisture_Sensor/ <br>
https://wiki.seeedstudio.com/Grove-Temperature_and_Humidity_Sensor_Pro/


