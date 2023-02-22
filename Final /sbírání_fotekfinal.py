import numpy as np
import picamera as Picamera 
from datetime import datetime, timedelta
from time import sleep
from orbit import ISS

camera = Picamera()
camera.start_preview()
camera.resolution(1600,90)
                  
counter = 0 
while (now_time < start_time + timedelta(minutes=2)):
    camera.capture("image_%s.jps" % counter)
    sleep(3)
    
location = ISS.coordinates()
print(location)
    
    
    
   
camera.stop_preview()
