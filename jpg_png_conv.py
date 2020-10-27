import sys
import os
from PIL import Image,ImageFilter

folder1_name, folder2_name = sys.argv[1], sys.argv[2]

print('folder1 name is', folder1_name)
print('folder2 name is', folder2_name)

# create directory
try:
    os.mkdir(folder2_name + '\\')
except FileExistsError:
    print('Directory already exists')

for file_name in os.listdir(folder1_name):
    print(file_name)
    img = Image.open(folder1_name+'\\'+file_name)
    name = file_name.split('.')
    img.save(folder2_name + '\\' + name[0] + '.png')



