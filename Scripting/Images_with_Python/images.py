from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')

print(img)
filtered_image = img.convert('L')
filtered_image.save('grey.png', 'png')
#filtered_image.show()
#filtered_image.rotate(90)