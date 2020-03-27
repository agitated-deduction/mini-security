import RPi.GPIO as GPIO
import time
import datetime
import diigit as d
from picamera import PiCamera

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

trig = 21
echo = 20
yellow = 18
red = 27

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
disp = d.TM1637(6, 5)
camera = PiCamera()

try:
    while True:
        GPIO.output(trig, False)
        time.sleep(0.01)
        
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
        
        
        pulse_start = time.time()
        pulse_end = time.time()
 
        
        while GPIO.input(echo) == 0:
            pulse_start = time.time()
        while GPIO.input(echo) == 1:
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance,2)
        
        print("distance : ", distance, "cm")
        
        if distance<12:
            GPIO.output(yellow, True)
            GPIO.output(red, False)
            time.sleep(0.3)
            GPIO.output(yellow, False)
            GPIO.output(red, True)
            time.sleep(0.3)
            disp.set_values("BACK");
            
        elif distance<17:
            GPIO.output(red, False)
            GPIO.output(yellow, True)
            time.sleep(0.5)
            GPIO.output(yellow, False)
            time.sleep(0.5)
            disp.clear()
        else:
            GPIO.output(yellow, False)
            GPIO.output(red, False)
            disp.clear()
            
        
        if distance<5:
            timestr = time.strftime("%Y%m%d%H%M%S", time.localtime())
            camera.start_preview()
            time.sleep(5)
            camera.capture('/home/pi/security_myrasp'+timestr+'.jpg')
            camera.stop_preview()
except Keyboardinterrupt:
    GPIO.cleanup()