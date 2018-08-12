# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 21:39:07 2018

@author: Arman
"""

from matplotlib_venn import venn2 
import matplotlib.pyplot as plt 
from sympy import FiniteSet

def draw_venn(sets):
    venn2(subsets=sets)
    plt.show()
    
if __name__=='__main__':
    s1 = FiniteSet(*range(1,20,2))
    s2 = FiniteSet(2,3,5,7,11,13,17,19)
    
    draw_venn([s1,s2])