#main
import diigit as d
import m_ultra as u
import m_camera as c
import led as l
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("stranger")
mqttc.connect('localhost', 1883)

disp = d.TM1637(6, 5)
ultra = u.ULTRA(20, 21)
led = l.LED(27, 18)
camera = c.CAMERA()
try:
    while True:
        dist = ultra.getDistance()
        #print('dist: ',dist)

        mqttc.loop_start()
        if dist<4:
            led.redOn()
            mqttc.publish("home/stranger", "very close")
            camera.takePicture()
        elif dist<12:
            led.redyellowFlashing()
            disp.set_values("BACK");
            mqttc.publish("home/stranger", "closer")
        elif dist<17:
            led.yellowFlashing()
            disp.clear()    
            mqttc.publish("home/stranger", "someone access")
        else:
            led.lightOff()
            
            disp.clear()    
        mqttc.loop_stop() 
        
except KeyboardInterrupt:
    GPIO.cleanup()
