import sys
import os
from PIL import Image

#grab first and second argument
sys.argv

# cwd = os.getcwd()
# print(cwd)

image_folder = sys.argv[1]
new_folder = sys.argv[2]

#get full path of a folder provided as argument
imf_path = os.path.abspath(image_folder)
nwf_path = os.path.abspath(new_folder)

#print(os.path.exists(image_folder))

# chek if folder exists
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# loop thru all files ni directory
for filename in os.listdir(image_folder):

    # open each file
    image = Image.open(f'{imf_path}\{filename}')
    # splirt filename into name and extension in a tuple
    clean_name = os.path.splitext(filename)[0]
    

    # convert images to .png
    # save them to the new folder
    image.save(f'{nwf_path}\{clean_name}.png', 'png')
    print('all done!')





