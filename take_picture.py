#!/usr/bin/env python
import cv2, sys
from datetime import datetime

# Define constants
DEVICE_NUMBER = 0
IMAGE_FILE = "output_" + str(datetime.now().time()) + ".jpg"

# Initialize webcam
vc = cv2.VideoCapture(DEVICE_NUMBER)

# Check if the webcam works
if vc.isOpened():
    # Try to get the first frame
    retval, frame = vc.read()
else:
    # Exit the program
    sys.exit(1)

# Read in the next frame
retval, frame = vc.read()

# Write the onto the frame
font_typeface = cv2.FONT_HERSHEY_PLAIN
font_scale = 2
font_color = (255,255,255)
x = 0
y = 50
cv2.putText(frame,"THIEF",(x,y),font_typeface,font_scale,font_color)

# Save the frame as an image file
cv2.imwrite(IMAGE_FILE, frame)

# Read the output file
img = cv2.imread(IMAGE_FILE)

# Show the saved image on the screen
cv2.imshow("DragonBoard 410c Workshop", img)

# Exit program after waiting indefinitely for a pressed key
cv2.waitKey(0)
