#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import csv

def main():
	'''plt.figure(figsize=(3,3))

	plt.plot([100,200,300,400],[0.1,0.2,0.8,0.9])
	plt.savefig('myplot.pdf')
	plt.close()

	with open('2cel.csv') as f:
	    lines = f.readlines()
	print(lines[0])'''

	plt.figure(figsize=(10,10))

	with open('cel.csv') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		next(csvreader)
		effort = []
		run = []
		for row in csvreader:
			#print row[2]
			effort.append(row[1])
			suma=0
			for index in range(len(row)):
				if index>1:
					#print row[index]
					suma+=float(row[index])
			suma/=len(row)-2
			run.append(suma)
			#print suma
	#print effort
	#print run
	

	plt.plot(effort,run)
	plt.savefig('myplot.pdf')
	plt.close()

if __name__ == '__main__':
	main()
