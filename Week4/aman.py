import cv2
import numpy as np

img =  cv2.imread("D:\\Wallpapers\\silhouette-of-human-male-vector-618740.jpg")

h,w,bpp = np.shape(img)

for py in range(0,h):
    for px in range(0,w):
#can change the below logic of rgb according to requirements. In this 
#white background is changed to #e8e8e8  corresponding to 232,232,232 
#intensity, red color of the image is retained.
        if(img[py][px][0] >200):            
            img[py][px][0]=232
            img[py][px][1]=232
            img[py][px][2]=232

cv2.imshow('matrix', img)
cv2.waitKey(0)
cv2.imwrite('yourNewImage.jpg',img)