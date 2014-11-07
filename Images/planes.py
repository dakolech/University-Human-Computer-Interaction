from skimage import data, io, filter, morphology
from skimage.io import Image
from skimage.morphology import square
import skimage as si
import numpy as np
from numpy import array
import matplotlib.pyplot as pl

def distinct(planes):
	for i, img in enumerate(planes):
		planes[i] = filter.sobel(planes[i])
		planes[i] = Image(morphology.erosion(planes[i], square(3)))
		planes[i] = Image(morphology.dilation(planes[i], square(3)))
		message = "Distincted plane: " + str(i)
		print(message)
	

def show(planes):
    	"Show multiple images in a row"
    	pl.figure(figsize=(80,48))
    	for index, img in enumerate(planes):
        	pl.subplot(2, len(planes)/2, index+1)
		io.imshow(img)
		message = "Rendered plane: " + str(index)
		print(message)
	#img = np.concatenate((planes[0], planes[1]), axis=1)
	#io.imshow(img)


    	pl.savefig('planes.jpg')
    	pl.close()


def main():
	images = ['samolot00.jpg','samolot01.jpg','samolot03.jpg','samolot04.jpg',
		  'samolot07.jpg','samolot08.jpg']
	planes = []
	for i in images:
		message = "Loaded: " + i
		planes.append(data.imread(i, as_grey=True))
		print(message)
	#print(planes)

	distinct(planes)

	
	show(planes)


if __name__ == '__main__':
	main()

