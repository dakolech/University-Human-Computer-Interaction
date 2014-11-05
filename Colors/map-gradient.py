from __future__ import division             # Division in Python 2.7
import matplotlib
matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math 

def main():
	f = open('big.dem')

	pierwsza_linia = f.readline()

	linia = pierwsza_linia.strip().split(' ')

	szerokosc 	= linia[0]
	wysokosc 	= linia[1]
	odleglosc 	= linia[2]

	dane = []
	for line in f:
		dane.append(line)

	f.close()

	plt.figure(figsize=(6, 5), dpi=80)

	plt.axis((0,500,500,0), size="small")

	plt.savefig('mapa.jpg')
	plt.close()



if __name__ == '__main__':
	main()