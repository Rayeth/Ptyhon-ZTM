import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = open(os.path.join(THIS_FOLDER, 'test.txt'))


print(my_file.read())
my_file.seek(0)
print(my_file.read())
print(my_file.readline())
print(my_file.readlines())
my_file.close()









#open_file = open(r'c:\Users\nopa\OneDrive - H. Lundbeck A S\Desktop\Git\Python-ZTM\FileIO\test.txt')


