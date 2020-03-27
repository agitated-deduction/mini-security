#ultra
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class ULTRA:
    
    trig = 0
    echo = 0
    
    def __init__(self, ech, tri):
        self.trig = tri
        self.echo = ech
    
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
       
    def getDistance(self):
 
        GPIO.output(self.trig, False)
        time.sleep(0.1)
    
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
        
        
        pulse_start = time.time()
        pulse_end = time.time()
 
        
        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance,2)
        
        return distance
