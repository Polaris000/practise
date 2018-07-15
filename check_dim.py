import cv2 
import os

#"/home/icameisaticoded/Desktop/blurring_clear_images/"
#"/home/icameisaticoded/Desktop/clear_images/"
path = "/home/icameisaticoded/Documents/Repos/Image-Super-Resolution/train_images/train/y/"
image_list = os.listdir(path)

for i in image_list:
	print(i)
	img = cv2.imread(path + i,cv2.IMREAD_COLOR)
	print(img.shape)
	if img.shape != (128, 128, 3):
		print("***")
		break

	
