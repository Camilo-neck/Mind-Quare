from PIL import Image

image = Image.open('Fondo.jpg')
new_image = image.resize((660, 425))
new_image.save('FondoR2.png')

print(image.size) # Output: (1200, 776)
print(new_image.size) # Output: (400, 400)
