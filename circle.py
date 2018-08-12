# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 21:47:48 2018

@author: Arman
"""

import matplotlib.pyplot as plt

def create_circle():
    circle1 = plt.Circle((0,0),radius=0.5)
    circle2 = plt.Circle((1,1),radius=0.3)
    return circle1,circle2

def show_shape(patch1,patch2):
    ax = plt.gca()
    ax.add_patch(patch1)
    ax.add_patch(patch2)
    plt.axis('scaled')
    plt.show()
    
if __name__=='__main__':
    c1,c2 = create_circle()
    show_shape(c1,c2)