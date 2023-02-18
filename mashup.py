import numpy as np
import cv2
from picamera import PiCamera
from time import sleep

# Initialize PiCamera object and start preview
camera = PiCamera()
camera.start_preview()

# Set camera resolution
camera.resolution = (1280, 720)

# Counter to keep track of number of photos taken
counter = 0

# Take 5 photos and save with a unique name
while counter < 5:
    camera.capture('image_%s.jpg' % counter)
    sleep(3)
    counter += 1

# Stop the camera preview
camera.stop_preview()

# Function to perform contrast stretching on an image
def contrast_stretch(im):
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im = cv2.equalizeHist(im)
    return im

# Loop through the captured images and perform contrast stretching on each of them
for i in range(5):
    # Read in the image
    img = cv2.imread('image_%s.jpg' % i)
    
    # Perform contrast stretching
    img_cs = contrast_stretch(img)
    
    # Display the original and contrast-stretched images
    display(img, "Original Image")
    display(img_cs, "Contrast-Stretched Image")
    
    # Save the contrast-stretched image
    cv2.imwrite("output_image_%s.jpg" % i, img_cs)

# Function to display an image
def display(image, image_name):
    image = np.array(image, dtype=float)/float(255)
    shape = image.shape
    height = int(shape[0] / 2)
    width = int(shape[1] / 2)
    image = cv2.resize(image, (width, height))
    cv2.namedWindow(image_name)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
