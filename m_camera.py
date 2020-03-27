#m_camera
import time
import datetime
from picamera import PiCamera


class CAMERA:
    camera = PiCamera()

    def takePicture(self, name=''):
        timestr =time.strftime("%Y%m%d%H%M%S", time.localtime()) if name=='' else name
        self.camera.start_preview()
        time.sleep(5)
        self.camera.capture('/home/pi/mysecurity/security_myrasp/'+timestr+'.jpg')
        self.camera.stop_preview()
    
    def takeContPictures(self, cnt, name=''):
        timestr =time.strftime("%Y%m%d%H%M%S", time.localtime()) if name=='' else name
        self.camera.start_perview()
        for i in range(cnt):
            sleep(5)
            self.camera.capture('/home/pi/mysecurity/security_myrasp/'+timestr+'_'+i+'.jpg')
        self.camera.stop_preview()
    
    def recordVid(self, sec=10,name=''):
        self.camera.start_preview()
        self.camera.start_recording('/home/pi/mysecurity/security_myrasp/'+timestr+'.h264')
        time.sleep(sec)
        self.camera.stop_recording()
        self.camera.stop_preview()
