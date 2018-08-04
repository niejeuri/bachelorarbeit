import random, os
directory = "/home/niejeuri/Bachelorarbeit/Images/NeuralNets/NetForPreprocessing/data/training/PreprocessedImagesWithoutStreets"
destination = "/home/niejeuri/Bachelorarbeit/Images/NeuralNets/NetForPreprocessing/data/evaluation/nostreets/"
number_of_images = 75
files = random.sample(os.listdir(directory), number_of_images)
for current_file in files:
     print(current_file)
     os.rename(directory + "/" + current_file, destination + current_file)
