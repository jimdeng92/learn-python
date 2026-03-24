from PIL import Image, ImageFilter

image = Image.open('girl.jpg')

print(image.size)

print(image.format)

print(image.mode)

img = image.crop((0, 50, image.size[0], 500))

# for x in range(100, img.size[0] - 100):
#     for y in range(150, 250):
#         img.putpixel((x, y), (255, 255, 255))

img.filter(ImageFilter.FIND_EDGES).show()

# img.rotate(45).show()

# image.thumbnail((108, 108))
#
# image.show()





