import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class LED:
    yellow = 0
    red = 0
    
    def __init__(self, r, y):
        self.red = r
        self.yellow = y

        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.yellow, GPIO.OUT)

    def redOn(self):
        GPIO.output(self.red, True)
        GPIO.output(self.yellow, False)
    
    def yellowOn(self):
        GPIO.output(self.red, False)
        GPIO.output(self.yellow, True)
    
    def redFlashing(self):
        GPIO.output(self.yellow, False)
        
        GPIO.output(self.red, True)
        time.sleep(0.5)
        GPIO.output(self.read, False)
        time.sleep(0.5)
        
    def yellowFlashing(self):
        GPIO.output(self.red, False)
        
        GPIO.output(self.yellow, True)
        time.sleep(0.5)
        GPIO.output(self.yellow, False)
        time.sleep(0.5)
        
    def redyellowFlashing(self):
        GPIO.output(self.yellow, False)
        GPIO.output(self.red, True)
        time.sleep(0.5)
        
        GPIO.output(self.yellow, True)
        GPIO.output(self.red, False)
        time.sleep(0.5)

    def redyellow(self):
        
        GPIO.output(self.yellow, True)
        GPIO.output(self.red, True)
        
    def lightOff(self):
        GPIO.output(self.yellow, False)
        GPIO.output(self.red, False)
