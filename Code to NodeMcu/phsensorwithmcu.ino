#include <Wire.h>
#include <PubSubClient.h>
#include <ESP8266WiFi.h>
const char* ssid = "AshokJoshi";              // wifi ssid
const char* password =  "Atreya$321";         // wifi password
const char* mqttServer = "192.168.1.204";    // IP adress Raspberry Pi
const int mqttPort = 1883;                  // port number of mqtt
//const char* mqttUser = "username";      // if you don't have MQTT Username, no need input
//const char* mqttPassword = "12345678";  // if you don't have MQTT Password, no need input

WiFiClient client1;
PubSubClient client(client1);
int pHSense = A0;

void setup() {
  {
  Serial.begin(115200);
  WiFi.begin(ssid, password);// connect to wifi
  while (WiFi.status() != WL_CONNECTED) { 
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
  client.setServer(mqttServer, mqttPort); //Connecting to mqtt server

  while (!client.connected()) { 
   Serial.println("Connecting to MQTT...");

    if (client.connect("ESP8266Client")) {

      Serial.println("connected");
    } else
    {
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);
    }
  }
  }} 
  


void loop(){
    int measuringVal = analogRead(pHSense);// reading from ph sensor from pin A0

    double vltValue = (5/1024.0 * measuringVal); //  converting anlog value to voltage

    float P0 = 7 + ((2.5 - vltValue) / 0.18);// converting  voltage  to Digital value 
    Serial.print("");
    Serial.print("pH Value > ");
    Serial.println(P0,3);// ph display

    
    Serial.print("vltValue");// voltage display
    Serial.println(vltValue,2);

    client.publish("ph01", String(P0).c_str()); // publishing ph snesor data on the topic "ph01"
    delay(3000);
}
