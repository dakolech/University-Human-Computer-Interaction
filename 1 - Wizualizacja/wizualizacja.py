#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import csv
import numpy

pudelkowe = []

def rysowanie(nazwa, styl):
	with open(nazwa) as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		next(csvreader)
		effort = []
		run = []
		
		for row in csvreader:
			effort.append(float(row[1])/1000)
			suma=0
			for index in range(len(row)):
				if index>1:
					suma+=float(row[index])
			suma/=len(row)-2
			run.append(suma*100)
		
		wiersz = []
		for index in range(len(row)):
			if index>1:
				wiersz.append(float(row[index]))

		pudelkowe.append(wiersz)	 
			

	plt.plot(effort,run, styl, markevery=25)
	

def main():


	plt.figure(figsize=(6, 5), dpi=80)
	
	wyk1 = plt.subplot(121)
	
	rysowanie('rsel.csv', '-bo')
	rysowanie('cel-rs.csv', '-gv')
	rysowanie('2cel-rs.csv', '-rD')
	rysowanie('cel.csv', '-ks')
	rysowanie('2cel.csv', '-md')  

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
	
	wyk3 = plt.subplot(122)
	plt.boxplot(pudelkowe,True,'b+')
	wyk3.tick_params(labelsize="small")
	plt.xticks(range(1,6),names_list,rotation=20,size="x-small")
	frame = plt.gca()
	frame.axes.get_yaxis().set_visible(False)
	plt.twinx()
	wyk3.grid(linewidth=0.5, color='grey')
        wyk3.yaxis.tick_right()
	plt.grid(linewidth=0.5, color='grey')
	plt.axis([0,6,60,100], size="small")

	i = 1
	for k in pudelkowe:
		plt.scatter(i,reduce(lambda x, y: x + y, k) / len(k))
		i += 1
	
	
	plt.savefig('myplot.jpg')
	plt.close()

if __name__ == '__main__':
	main()
