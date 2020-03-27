import paho.mqtt.client as mqtt
import time
import led

l = led.LED(27, 18)

def on_connect(client, userdata,flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("bit/led")

    #client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
    print(msg.topic+ " " + str(msg.payload))
    if str(msg.payload) == 'red':
        l.redOn()
    elif str(msg.payload) == 'yellow':
        l.yellowOn()
    elif str(msg.payload) == 'both':
        l.redyellow()
    else:
        l.lightOff()


addr = "192.168.1.25"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(addr, 1883)

client.loop_forever()

