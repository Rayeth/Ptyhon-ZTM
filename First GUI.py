#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


# # list to append newly created list with converted values
# full_picutre = []

# #loop the enter each list in picutre
# for item in picture:
#     #list to append newly converted values of pixel
#     empty_list = []

#     for pixel in item:
        
#         if pixel == 0:

#             pixel = ' '

#             empty_list.append(pixel)

#         else pixel == 1:

#             pixel = '*'

#             empty_list.append(pixel)
    
#     full_picutre.append(empty_list)

# print(full_picutre, end:)

for image in picture:
  for pixel in image:
    if (pixel):
      print('*', end ="")
    else:
      print(' ', end ="")
  print('')