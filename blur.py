"""
This is a python script to blur an image using cv2(opencv-python)
Writing this program also requires use of the os module to:
	1) read and write an image in a particular directory
	2) get a list of all files present at a path (unix: ls)
"""


import cv2 
import os

#please set
sharp_path = ""

#list of all image names in given path
image_list = os.listdir(sharp_path)

for i in image_list:
	#read image
	clear_img = cv2.imread(sharp_path + i,cv2.IMREAD_COLOR)
	blurred_img = cv2.blur(clear_img, (10, 10)) # blur image
	cv2.imwrite(str(i), blurred_img) # save modified image with file name i
