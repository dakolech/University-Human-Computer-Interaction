from skimage import data, io, filter, morphology
from skimage.io import Image
from skimage.morphology import square
import skimage as si
from numpy import array
import numpy as np
import matplotlib.pyplot as plt

from skimage import measure
from skimage.filter import threshold_otsu


images = ['samolot00.jpg','samolot01.jpg',
		  'samolot05.jpg','samolot07.jpg','samolot08.jpg',
		  'samolot09.jpg','samolot10.jpg','samolot11.jpg','samolot12.jpg',
		  'samolot16.jpg',
		  'samolot17.jpg', 'samolot18.jpg']

plt.figure(figsize=(100,80))


for index, img in enumerate(images):
		message = "Loaded: " + img
		print(message)
		#planes.append(data.imread(i, as_grey=True))
		r = data.imread(img)
		t = data.imread(img, as_grey=True)
		thresh = threshold_otsu(t)
		binary = t > thresh


		binary = Image(morphology.erosion(binary, square(5)))
		binary = Image(morphology.dilation(binary, square(5)))
		binary = Image(morphology.erosion(binary, square(5)))
		binary = Image(morphology.dilation(binary, square(5)))

		# Find contours at a constant value of 0.8
		contours = measure.find_contours(binary, 5)

		# Display the image and plot all contours found
		fig = plt.subplot(6, len(images)/6, index+1) 
		ax = plt.subplot(6, len(images)/6, index+1) #plt.subplots()
		ax.imshow(r, interpolation='nearest', cmap=plt.cm.gray)

		for n, contour in enumerate(contours):
			ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

		ax.axis('image')
		ax.set_xticks([])
		ax.set_yticks([])
plt.tight_layout()

plt.subplots_adjust(wspace = .00001)

plt.savefig('planes1.jpg')
plt.close()