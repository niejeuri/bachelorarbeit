from PIL import Image
import os, sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "/home/niejeuri/Bachelorarbeit/Images/NeuralNets/NetForPreprocessing/data/resources/ResizedImages/"
dirs = os.listdir( path )

def preprocessing():
    count = 0
    for item in dirs:
        print("Current File: ", path,item)
        if os.path.isfile(path+item):
            print("Is File")
            im = cv2.imread(path+item)
            f, e = os.path.splitext(path+item)
            sobel_filtered_image = cv2.Sobel(im,cv2.CV_8U,1,0,ksize=5)
            combinedImage = cv2.addWeighted(im,0.5,sobel_filtered_image,0.5,0)
            cv2.imwrite(str(count) + ' combined.png', combinedImage)
            count += 1
        else:
            print(item, " is no file")
preprocessing()

