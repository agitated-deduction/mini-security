#main
import diigit as d
import m_ultra as u
import m_camera as c
import led as l
import RPi.GPIO as GPIO

disp = d.TM1637(6, 5)
ultra = u.ULTRA(20, 21)
led = l.LED(27, 18)
camera = c.CAMERA()
try:
    while True:
        dist = ultra.getDistance()
        print('dist: ',dist)
        if dist<4:
            led.redOn()
            camera.takePicture()
        elif dist<12:
            led.redyellowFlashing()
            disp.set_values("BACK");
        elif dist<17:
            led.yellowFlashing()
            disp.clear()    
        else:
            led.lightOff()
            
        disp.clear()    
        
except KeyboardInterrupt:
    GPIO.cleanup()