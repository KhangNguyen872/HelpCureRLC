from PIL import Image

img = Image.open('finally.png')

print(img.format)
print(img.size)
print(img.mode)

img.show()