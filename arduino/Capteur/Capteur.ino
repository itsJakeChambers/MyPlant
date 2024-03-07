#include <DHT.h>
#include <SPI.h>
#include <WiFiNINA.h>
#include <PubSubClient.h>

#include "arduino_secrets.h" 

void printCurrentNet();
void printWifiData();
void reconnect();
 
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;
int status = WL_IDLE_STATUS;

byte mac[] = {0xDE, 0xED, 0xBA, 0xFE, 0xFE, 0xED};
IPAddress server(192, 168, 60, 166);

WiFiClient WClient;
PubSubClient client(WClient);

#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

unsigned long previousMillis = 0; // Variable for storing previous time
const long interval1 = 10000;     // Interval for publishing data every 10 seconds
const long interval2 = 600000;    // Interval for publishing data every 10 minutes

void setup()
{
  Serial.begin(9600);
  dht.begin();

  if (WiFi.status() == WL_NO_MODULE)
  {
    Serial.println("Communication with WiFi module failed!");
    while (true);
  }

  String fv = WiFi.firmwareVersion();
  if (fv < WIFI_FIRMWARE_LATEST_VERSION)
  {
    Serial.println("Please upgrade the firmware");
  }

  while (status != WL_CONNECTED)
  {
    Serial.print("Attempting to connect to WPA SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
    delay(10000);
    client.setServer(server, 1883);
  }

  Serial.print("You're connected to the network");
  printCurrentNet();
  printWifiData();
}

void printCurrentNet() {
  // Print network details
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  Serial.print("Signal Strength (RSSI): ");
  Serial.println(WiFi.RSSI());
}

void printWifiData() {
  // Print MAC address
  byte mac[6];
  WiFi.macAddress(mac);
  Serial.print("MAC Address: ");
  for (int i = 0; i < 5; i++) {
    Serial.print(mac[i], HEX);
    Serial.print(":");
  }
  Serial.println(mac[5], HEX);
}

void reconnect() {
  // Loop until reconnected to MQTT broker
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect to MQTT broker
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
      // Once connected, subscribe to a topic
      client.subscribe("esp/test");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}


void loop()
{
  unsigned long currentMillis = millis();

  // Reading temperature or humidity takes about 250 milliseconds!
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t))
  {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  int moisture = analogRead(A0);
  int light = analogRead(A2);
  
  // Check if 10 seconds have passed
  if (currentMillis - previousMillis >= interval1)
  {
    previousMillis = currentMillis;
    // Publish data to MQTT
    String data = String(t) + "," + String(h) + "," + String(moisture) + "," + String(light); // Format: "temperature,humidity"
    client.publish("data_plant1", data.c_str());
  }

  // Check if 10 minutes have passed
  if (currentMillis - previousMillis >= interval2)
  {
    previousMillis = currentMillis;
    // Publish data to MQTT
    String data = String(t) + "," + String(h); // Format: "temperature,humidity"
    client.publish("data_plant1", data.c_str());
  }

  // Maintain MQTT connection
  if (!client.connected())
    reconnect();
  client.loop();

  // Wait a few seconds between measurements.
  delay(2000);
}
