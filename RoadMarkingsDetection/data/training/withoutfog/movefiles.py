import os
dir = "/home/niels/Repositories/Images/NeuralNets/RoadMarkingsDetection/data/training/withoutfog/"
dest = "/home/niels/Repositories/Images/NeuralNets/RoadMarkingsDetection/data/training/streetmarkings/"
for file in os.listdir(dir):
	if file.endswith(".xml"):
		os.rename(os.path.join(dir, file), os.path.join(dest, file))
		os.rename(os.path.splitext(os.path.join(dir, file))[0] + ".png", os.path.splitext(os.path.join(dest, file))[0] + ".png")
		print(os.path.splitext(os.path.join(dir, file))[0])
