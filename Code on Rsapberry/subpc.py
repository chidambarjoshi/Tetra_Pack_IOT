import paho.mqtt.client as mqtt
from time import sleep
from mongodb import md
import datetime

client=mqtt.Client("subscribe")
count = 0

def on_connect (client,userdata,flags,rc): #rc : responce code
    if rc==0:
        print("successfully conected to borker with Rc: ",rc)
    else :
        print("Unsucessfull connection")
    client.subscribe("ph01")
    #client.subscribe("esp8266/humi",1)

def on_message (clinet,userdata,msg):
    id=msg.topic[slice(2,4)]
    phvalue=msg.payload.decode()
    print(msg.topic)
    print("raw data =",msg.payload)
    print("decoded=",phvalue)
    md.rec_data(id,phvalue)

broker="192.168.1.204"
print("connecting to broker",broker)

client.on_connect=on_connect
client.on_message=on_message
client.connect(broker,1883)


client.loop_forever()
client.disconnect()