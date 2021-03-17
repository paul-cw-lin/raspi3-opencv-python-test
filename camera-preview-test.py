from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180 #degrees can be 0, 90, 180, 270

camera.start_preview()
sleep(5)
camera.stop_preview()

camera.close()