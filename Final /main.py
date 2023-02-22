from picamera import PiCamera 
import time 
#we firstly set the raspberry HQ camera as a variable for the later use
camera = PiCamera()
#starts the camera preview 
camera.start_preview()
#sets the camera resolution to full HD 
camera.resolution(1920,1080)
#counter for naming the taken photos and ending the loop 
counter = 1
#loop takes 3600 photos in the period of 3h while naming the taken photos 
while True:
    camera.capture("image_%s.jpg" % counter)
    time.sleep(2.55)
    counter += 1
    if counter == 3601: 
       break
#stops preview 
camera.stop_preview()