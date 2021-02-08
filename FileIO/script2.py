import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

my_file = (os.path.join(THIS_FOLDER, 'test.txt'))

with open(my_file, 'w') as my_file:
    text = my_file.write('hey it\s me!')
    print(text)
    
