import numpy as np 
from matplotlib import image as mpimg 
from matplotlib import pyplot as plt 
from picamera import PiCamera
import time 
from datetime import datetime, timedelta 
from time import sleep 

start_time = datetime.now()
now_time = datetime.now()

camera = PiCamera()
# Start the camera preview
camera.start_preview()

camera.resolution =(1280,720)
# Counter to keep track of the number of photos taken
counter = 0

# Loop to take photos until 5 photos are taken
while True:
    # Take the photo and save it with a unique name
    camera.capture('image_%s.jpg' % counter)
    time.sleep(3)   
    counter += 1
    if counter == 6:
       break

# Stop the camera preview
camera.stop_preview()

img = mpimg.imread("/home/miker/Desktop/zkoušky/image_%s.jpg" % counter)

output_img = np.zeros_like(img)

# Convert the input image to grayscale
gray_img = np.dot(img, [0.2989, 0.5870, 0.1140])

# Set the green channel of the output image to be the same as the green channel of the input image
output_img[:, :, 1] = img[:, :, 1]

# Set the other two channels of the output image to be the same as the grayscale image
output_img[:, :, 0] = gray_img
output_img[:, :, 2] = gray_img * 0.95

# Display the resulting image
plt.imshow(output_img)
plt.show()
