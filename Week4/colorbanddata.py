import cv2
import numpy as np
import pandas as pd

img = cv2.imread('ra.jpg')

# function to scan the black body on the image
def firstime():
        #Loop to get top and bottom values of the human from the image
    global height
    global width
    global blackmin
    global blackmax

    for j in range(height):
        for i in range(width):
            if (img.item(j,i,0)==0):
                if j>blackmax:
                    blackmax=j
                if j<blackmin:
                    blackmin=j                
    print(blackmin)
    print(blackmax)
    # blackmin = blackmin +250
    # blackmax = blackmax -250

# height, width = img.shape[:2]
# width, height = cv.GetSize(src)
height = np.size(img, 0)
width = np.size(img, 1)
blackmin = height
blackmax = 0
print(width)
print(height)

firstime()

df = pd.read_excel(r'output.xlsx', sheet_name='Sheet1', index_col=0)
# print(df)
toilist = []
toilist = df.index.tolist()

for i in range (len(toilist)):
    donothave = toilist[i]
    # have = 100 - donothave
    # donothave = int((donothave/100))
    have = 100 - donothave

    img = cv2.imread('ra.jpg')

    height0 = blackmin - 4
    height1 = blackmax + 4    
    # height0 = blackmin + 400
    # height1 = blackmax - 300

    # want0 = int(have*((height1-height0)/100))
    want0 = int(have*((height1-height0)/100))
    # want1 = int(2*(height/3))
    # print(want)

    for i in range(width):
        for j in range(height0,want0):
            img.itemset((j,i,2),255)
            img.itemset((j,i,0),255)
    for i in range(width):
        for j in range(want0,height1):
            img.itemset((j,i,1),255)
    # for i in range(width):
    #     for j in range(want0,height):
    #         # img.itemset((j,i,2),255)
            # img.itemset((j,i,0),255)
    cv2.imshow('image',img)
    cv2.waitKey(1)
    # cv2.destroyAllWindows()
cv2.destroyAllWindows()
