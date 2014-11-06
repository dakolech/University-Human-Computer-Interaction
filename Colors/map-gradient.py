from __future__ import division             # Division in Python 2.7
import matplotlib
matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math 

def hsv2rgb(h, s, v):
    if v == 0:
        return 0, 0, 0
    else:
        h *= 6
        i = min(math.floor(h), 5)
        f = h - i
        p = v*(1 - s)
        q = v*(1 - (s*f))
        t = v*(1 - (s*(1 - f)))
        
        options = {
            0: (v, t, p),
            1: (q, v, p),
            2: (p, v, t),
            3: (p, q, v),
            4: (t, p, v),
            5: (v, p, q),
        }
        return options[i]


def kolor(v):
        

        return hsv2rgb(0.35*(1 - v), 1, 1)

def main():
	f = open('big.dem')

	pierwsza_linia = f.readline()

	linia = pierwsza_linia.strip().split(' ')

	szerokosc 	= int(linia[0])
	wysokosc 	= int(linia[1])
	odleglosc 	= int(linia[2])

	dane = []
	for line in f:
	        dane.append([float(el) for el in line[:-1].strip().split(' ')])

	f.close()
	
	#print(dane[0][0])
	
	minimum = min([min(el) for el in dane])
        maximum = max([max(el) for el in dane])
        
        #print(minimum, maximum)
        
        dane = [[(j - minimum)/(maximum - minimum) for j in i] for i in dane]
        
        img = np.zeros((szerokosc, wysokosc, 3))
        for i in range(1, len(img)):
            for j in range(0, len(img[i]) - 1):
                img[i][j] = kolor(dane[i][j])
        
	plt.figure(figsize=(6, 5), dpi=80)

	plt.axis((0,500,500,0), size="small")
	
	#img=Image(zeros([300,300]))
	
	plt.imshow(img)

	plt.savefig('mapa.jpg')
	plt.close()



if __name__ == '__main__':
	main()