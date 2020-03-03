# This is the problem for First technical round for the role of Computer Vision Engineer at Vectorly
# More details at https://www.linkedin.com/jobs/view/1629909785/
#
# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure" 
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
# 
# Note that you don't need to extract the text, the output is an image with only 
# the overlay visible and everything else (background) white
#
# You can use the snipped below (in python) to get started if you like 
# Python is not required but is preferred. You are free to use any libraries or any language


#####################
import cv2
import numpy as np
from skimage import data
import matplotlib.pyplot as plt
from skimage import io

def getTextOverlay(input_image):
    output = np.zeros(input_image.shape, dtype=np.uint8)
    # Write your code here for output
    input_image = cv2.bitwise_not(input_image)
    upper = np.array([255,255,255])
    lower = np.array([220,220,220])
    mask = cv2.inRange(input_image, lower, upper)
    output = cv2.bitwise_and(input_image, input_image, mask=mask)
    output = cv2.bitwise_not(output)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4,8))
    output = cv2.morphologyEx(output, cv2.MORPH_CLOSE, kernel)


    return output

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    img_not = cv2.bitwise_not(image)

    cv2.imwrite('simpons_text.png', output)

#####################

