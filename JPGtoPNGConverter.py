#pillow Python imaging library
from PIL import Image, ImageFilter,ImageEnhance
import os
import sys

#Grab the first and second argument
image_folder =sys.argv[1]
output_folder=sys.argv[2]

#check if folder exits else create
current_directory = os.getcwd()
image_path=os.path.join(current_directory, image_folder)

output_path = image_folder+output_folder
output_path=os.path.join(current_directory, output_path)

file_path=os.path.join(current_directory, image_path)


if not os.path.isdir(output_path):
    os.makedirs(output_path)
    
print(output_path)
print(os.path.exists(output_path))
print(image_folder,output_folder) 
#loop through images
for filename in os.listdir(image_folder):
    image_file_path=os.path.join(file_path, filename)
    if os.path.isfile(image_file_path):
        img=Image.open(image_file_path)
        clean_name=os.path.splitext(filename)[0]
        img.save(os.path.join(output_path, clean_name)+".png",'png')   
    print(clean_name,image_file_path,filename,'all done')

#convert images to png
#save them in the new folder

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "images/train.jpg"
abs_file_path = os.path.join(script_dir, rel_path)

img=Image.open(abs_file_path)