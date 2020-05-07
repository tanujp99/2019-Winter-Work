

# importing Image class from PIL package 
from PIL import Image 

# creating a object 
image = Image.open(r"ra.jpg") 
image.load() 
r, g, b= image.split()[1] 

# merge funstion used 
im1 = Image.merge('RGB', (r, g, b)) 
im1.show() 
image.putdata(im1)
image.save('im1.png')