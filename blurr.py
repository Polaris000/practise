import cv2 
import os


sharp_path = "/home/icameisaticoded/Documents/Repos/Image-Super-Resolution/train_images/validation/y/"
blurr_path = "/home/icameisaticoded/Documents/Repos/Image-Super-Resolution/train_images/validation/X"
image_list = os.listdir(sharp_path)

for i in image_list:
	clear_img = cv2.imread(sharp_path + i,cv2.IMREAD_COLOR)
	blurred_img = cv2.blur(clear_img, (10, 10))
	blurred_small = cv2.resize(blurred_img, (64, 64))
	cv2.imwrite(str(i), blurred_small)