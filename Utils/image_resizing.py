from PIL import Image
import os, sys

path = "/home/niejeuri/Bachelorarbeit/Images/Images/training/ResizedImagesNoStreets/"
dirs = os.listdir( path )

def resize():
    count = 0
    for item in dirs:
        print("Current File: ", path,item)
        if os.path.isfile(path+item) and "resized" not in item:
            print("Is File")
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200,120), Image.ANTIALIAS)
            imResize.save(str(count) + ' resized.jpg', 'JPEG', quality=90)
            count += 1
        else:
            print(item, " is no file")
resize()
