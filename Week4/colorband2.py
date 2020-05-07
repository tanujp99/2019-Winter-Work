
from PIL import Image

img = Image.open('rb.jpg')
imgsplit = Image.Image.split(img)
width, height = img.size

imgsplit.show()
print(imgsplit)



band1=width* int(height/3)
l0 = list(imgsplit[0])
for r in range (0,band1):
    l0[r]=255

imgsplit[0]=tuple(l0)
img1= Image.merge('RGB', (imgsplit[0],imgsplit[1],imgsplit[2]))
img1.show()