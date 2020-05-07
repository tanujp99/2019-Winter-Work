from PIL import Image

# img = Image.open('C:\\Users\\tanuj\\Desktop\\silhouette-of-human-male-vector-618740.jpg')
img = Image.open('ra.jpg')
data = img.getdata()

# Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
r = [(d[0], 0, 0) for d in data]
g = [(0, d[1], 0) for d in data]
b = [(0, 0, d[2]) for d in data]

# print (r)

width, height = img.size

print(height)
print(width)

for i in range(0,width):
    for j in range(0,int(2*height/3)):
        r= (255,0,0)

print(data)
img.putdata(r)
img.save('r.png')
# img.putdata(g)
# img.save('g.png')
# img.putdata(b)
# img.save('b.png')