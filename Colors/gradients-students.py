#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division             # Division in Python 2.7
import matplotlib
matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math 

from matplotlib import colors

def plot_color_gradients(gradients, names):
    # For pretty latex fonts (commented out, because it does not work on some machines)
    #rc('text', usetex=True) 
    #rc('font', family='serif', serif=['Times'], size=10)
    rc('legend', fontsize=10)

    column_width_pt = 400         # Show in latex using \the\linewidth
    pt_per_inch = 72
    size = column_width_pt / pt_per_inch

    fig, axes = plt.subplots(nrows=len(gradients), sharex=True, figsize=(size, 0.75 * size))
    fig.subplots_adjust(top=1.00, bottom=0.05, left=0.25, right=0.95)


    for ax, gradient, name in zip(axes, gradients, names):
        # Create image with two lines and draw gradient on it
        img = np.zeros((2, 1024, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v)

        im = ax.imshow(img, aspect='auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)

        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='left', fontsize=10)

    fig.savefig('my-gradients.pdf')

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

def gradient_rgb_bw(v):
    return (v, v, v)


def gradient_rgb_gbr(v):
    if v<=0.5:
    	r=0
    	g=1-2*v
    	b=1.5*v
    else:
    	r=2*v+0.01
    	g=0
    	b=1.5*(1-v)	
    return (r,g,b)


def gradient_rgb_gbr_full(v):
    if v<=0.5:
	if v<0.25:
	    	r=0
	    	g=1
	    	b=4*v
		#print(round(v,2),':',round(r,2),',',round(g,2),',',round(b,2),' ')
	else:
		r=0
    		g=4*(0.5-v)
    		b=1
		#print(round(v,2),':',round(r,2),',',round(g,2),',',round(b,2),' ')
    else:
    	if v<0.75:
	    	r=-4*(0.5-v)
	    	g=0
	    	b=1
		#print(round(v,2),':',round(r,2),',',round(g,2),',',round(b,2),' ')
	else:
		r=1
    		g=0
    		b=4*(1-v)
    		#print(round(v,2),':',round(r,2),',',round(g,2),',',round(b,2),' ')	
    return (r,g,b)


def gradient_rgb_wb_custom(v):
    r=abs(math.cos(2*v))
    g=abs(math.sin(4*v))
    b=abs(math.cos(8*v))
    return (r,g,b)


def gradient_hsv_bw(v):
    return hsv2rgb(0, 0, v)


def gradient_hsv_gbr(v):
    return hsv2rgb(v+0.3*(1-v), 1, 1)

def gradient_hsv_unknown(v):
    h=0.34-v/3
    return hsv2rgb(h, 0.5, 1)


def gradient_hsv_custom(v):
    return hsv2rgb(abs(math.cos(8*v)), abs(math.cos(4*v)), abs(math.cos(16*v)))


if __name__ == '__main__':
    def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])
