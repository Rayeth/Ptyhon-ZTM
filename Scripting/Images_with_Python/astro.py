from PIL import Image

astro = Image.open('./astro.jpg')
astro.thumbnail((400,200))
astro.save('new_astro.jpg')