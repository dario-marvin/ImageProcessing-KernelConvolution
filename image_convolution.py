from PIL import Image
from itertools import chain
import os
import numpy as np
from numpy import loadtxt

im_name = 'brain';
im = Image.open(im_name + '.jpg', 'r')
width, height = im.size
pixel_values = list(im.getdata())
l = list(chain(*pixel_values))

data = open('raw_RGB_input.txt','w')
data.write(str(width) + ' ')
data.write(str(height) + ' ')
for i in l:
	data.write(str(i) + ' ')
data.close()
	
# !!! Choose only one kernel!!!	
	
#~ chosen_kernel = 'Identity'
#~ chosen_kernel = 'Blur'
#~ chosen_kernel = 'Gaussian_blur'
#~ chosen_kernel = 'Sharpen'
chosen_kernel = 'Emboss'
#~ chosen_kernel = 'Edge_detection'
#~ chosen_kernel = 'Laplacian_filter'

kernel = open('kernel.txt','w')
kernel.write(chosen_kernel)
kernel.close()

os.system('g++ -Wall -std=c++0x -o kernel_application kernel_application.cc')
os.system('./kernel_application')

read_data = loadtxt('modified_RGB_data.txt', comments='#', delimiter=', ', unpack=False)

data = np.zeros((height, width, 3), dtype=np.uint8)
counter = 0

for i in range(height):
	for j in range(width):
		data[i,j] = [read_data[counter], read_data[counter+1], read_data[counter+2]]
		counter = counter + 3

img = Image.fromarray(data, 'RGB')
out = Image.new('RGB', (2*width, height))
out.paste(im, (0,0))
out.paste(img, (width,0))
out.save(im_name + '_' +chosen_kernel + '.jpg')
os.system('rm raw_RGB_input.txt modified_RGB_data.txt kernel.txt kernel_application')
out.show()
