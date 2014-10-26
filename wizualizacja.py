#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import csv

box_list = []

def rysowanie(nazwa, styl):
	with open(nazwa) as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		next(csvreader)
		effort = []
		run = []
		for row in csvreader:
			#print row[2]
			effort.append(float(row[1])/1000)
			suma=0
			for index in range(len(row)):
				if index>1:
					#print row[index]
					suma+=float(row[index])
			suma/=len(row)-2
			run.append(suma*100)
			#print suma
		box_list.append(suma*100)
	#print effort
	#print run
	

	plt.plot(effort,run, styl)
	

def main():


	plt.figure(figsize=(6, 5), dpi=80)
	
	wyk1 = plt.subplot(121)
	
	rysowanie('rsel.csv', 'b')
	rysowanie('cel-rs.csv', 'g')
	rysowanie('2cel-rs.csv', 'r')
	rysowanie('cel.csv', 'k')
	rysowanie('2cel.csv', 'm')  

	plt.grid(linewidth=0.5, color='grey')
	plt.axis((0,500,60,100), size="small")
	wyk1.tick_params(labelsize="small")

	plt.xlabel('Rozegranych gier (x1000)', size="small")
	plt.ylabel('Odsetek wygranych gier [%]', size="small")	

	legenda = plt.legend(['1-Evol-RS','1-Coev-RS','2-Coev-RS','1-Coev','2-Coev'], loc="lower right", prop={'size':'x-small'}, fancybox=True)

	legenda.get_frame().set_alpha(0.75)
	legenda.get_frame().set_linewidth(0.5)

	wyk2 = plt.twiny()
	plt.axis([0,200,60,100], size="small")
	wyk2.set_xticks([0,40,80,120,160,200])
	wyk2.tick_params(labelsize="small")
	plt.xlabel('Pokolenie', size="small")


	names_list=['1-Evol-RS','1-Coev-RS','2-Coev-RS','1-Coev','2-Coev']
	
	plt.subplot(122)
	#plt.boxplot(box_list, notch = True, labels = names_list, showmeans=True, meanprops=dict(marker='o'))
	frame = plt.gca()
	plt.grid()
	frame.axes.get_yaxis().set_visible(False)
	plt.twinx()
	plt.grid()
	plt.axis([0,6,60,100])
	
	
	plt.savefig('myplot.jpg')
	plt.close()

if __name__ == '__main__':
	main()
