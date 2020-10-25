from PIL import Image

image = Image.open('GameLogo.png')
new_image = image.resize((720, 405))
new_image.save('GameLogoR.png')

print(image.size) # Output: (1200, 776)
print(new_image.size) # Output: (400, 400)