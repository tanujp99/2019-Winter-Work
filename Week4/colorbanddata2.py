import cv2
import numpy as np
import pandas as pd
# from matplotlib import pyplot as plt 

img = cv2.imread('rac.jpg')
# img0 = cv2.imread('rad.jpg')
# img = cv2.fastNlMeansDenoisingColored(img0,None,10,10,7,21)

# function to clear any pixels other than values 0 & 255
def filterimage():
    for i in range(width):
        for j in range(height):
            if (img.item(j,i,0)>10):
                img.itemset((j,i,0),255)
                img.itemset((j,i,1),255)
                img.itemset((j,i,2),255)
            else:
                img.itemset((j,i,0),0)
                img.itemset((j,i,1),0)
                img.itemset((j,i,2),0)


#Loop to get top and bottom values of the human from the image
def deepblacks():
    global height
    global width
    global blackmin
    global blackmax

    for i in range(width):
        for j in range(height):
            if (img.item(j,i,0)==0):
                if j>blackmax:
                    blackmax=j
                if j<blackmin:
                    blackmin=j                
    print(blackmin)
    print(blackmax)
    # blackmin = blackmin +250
    # blackmax = blackmax -250

#Loop to get top and bottom values of the Chest from the Human
def ribskamaxnmin():
    global height
    global width
    global ribmin
    global ribmax
    for i in range(int(height/2)):
        pixc = 0
        pixlastval = 255
        for j in range(width):
            if (img.item(i,j,0)==pixlastval):
                pixlastval = img.item(i,j,0)
            else:
                pixlastval = img.item(i,j,0)    
                pixc = pixc + 1

        # print(pixc)    
        if pixc == 6:    
            if i > ribmax:
                ribmax= i

            if i < ribmin:
                ribmin = i    

# Confine the code to the Chest only (column-wise constraining)
def bajuwalascene(row):
    global height
    global width
    global leftwalibaju
    global rightwalibaju
    global ribmin
    global ribmax

    # for i in range(ribmin,ribmax):
    pixc = 0
    pixlastval = 255
    for j in range(width):
        if (img.item(row,j,0)==pixlastval):
            pixlastval = img.item(i,j,0)
        else:
            pixlastval = img.item(i,j,0)    
            pixc = pixc + 1

            if pixc == 3:    
                leftwalibaju = j
            if pixc == 4:    
                rightwalibaju = j

# height, width = img.shape[:2]
# width, height = cv.GetSize(src)
height = np.size(img, 0)
width = np.size(img, 1)
blackmin = height
blackmax = 0

leftwalibaju = 0
rightwalibaju = 0

ribmin = height
ribmax = 0

print(width)
print(height)


# deepblacks()
filterimage()

ribskamaxnmin()

print(ribmax)
print(ribmin)

df = pd.read_excel(r'output.xlsx', sheet_name='Sheet1', index_col=0)

toilist = []
toilist = df.index.tolist()

for i in range (len(toilist)):
    donothave = toilist[i]
    # have = 100 - donothave
    # donothave = int((donothave/100))
    have = 6 - int(donothave % 6)

    img = cv2.imread('rac.jpg')
    # img0 = cv2.imread('rad.jpg')
    # img = cv2.fastNlMeansDenoisingColored(img0,None,10,10,7,21)


    # height0 = blackmin - 4
    # height1 = blackmax + 4        
    height0 = ribmin
    height1 = ribmax 
    # height0 = blackmin + 400
    # height1 = blackmax - 300

    # want0 = int(have*((height1-height0)/100))
    want0 =int(have*((height1-height0)/6))
    # want1 = int(2*(height/3))
    # print(want)




    # for i in range(height0,(height0 + want0)):
    #     for j in range(int(width)):
    #         img.itemset((i,j,2),255)
    #         img.itemset((i,j,0),255)
    # for i in range((height0 + want0),height1):
    #     for j in range(int(width)):
    #         img.itemset((i,j,1),255)
   
   
 
 
    # for i in range(height0,(height0 + want0)):
    #     for j in range(int(5*width/9) , int(6*width/9)):
    #         img.itemset((i,j,2),255)
    #         img.itemset((i,j,0),255)
    # for i in range((height0 + want0),height1):
    #     for j in range(int(5*width/9) , int(6*width/9)):
    #         img.itemset((i,j,1),255)

   
   
    for i in range(height0,(height0 + want0)):
        bajuwalascene(i)
        for j in range(int(leftwalibaju) , int(rightwalibaju)):
            img.itemset((i,j,2),255)
            img.itemset((i,j,0),255)
    for i in range((height0 + want0),height1):
        bajuwalascene(i)
        for j in range(int(leftwalibaju) , int(rightwalibaju)):
            img.itemset((i,j,1),255)

 
    # for i in range(width):
    #     for j in range(want0,height):
    #         # img.itemset((j,i,2),255)
            # img.itemset((j,i,0),255)
    cv2.imshow('image',img)
    cv2.waitKey(1)
    # cv2.destroyAllWindows()
cv2.destroyAllWindows()




