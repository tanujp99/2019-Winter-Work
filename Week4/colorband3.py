import cv2
import numpy as np

img = cv2.imread('rb.jpg')
px = img [100,100]
print (px)

blue = img [100,100,1]
print(blue)

width, height = img.size
print(width)