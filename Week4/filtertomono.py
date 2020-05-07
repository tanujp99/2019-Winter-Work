import cv2
import numpy as np
import pandas as pd

img = cv2.imread('ra.jpg')

height = np.size(img, 0)
width = np.size(img, 1)
blackmin = height
blackmax = 0
print(width)
print(height)

for i in range(width):
    for j in range(height):
        temp = (img.item(j,i,0))
        if temp in range(1,255):
            img.itemset((j,i,0),255)              
            img.itemset((j,i,1),255)              
            img.itemset((j,i,2),255)              
# print(blackmin)
cv2.imshow('image',img)
cv2.waitKey(0)
# for i in range(width):
#     for j in range(want0,height1):
#         img.itemset((j,i,1),255)