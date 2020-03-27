import paho.mqtt.client as mqtt

mqttc = mqtt.Client("id")
mqttc.connect('localhost', 1883)
mqttc.loop_start()
mqttc.publish("hello/world", "this is test")
mqttc.loop_stop()
