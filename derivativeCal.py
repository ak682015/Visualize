# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:05:20 2018

@author: Arman
"""

from sympy import *
import matplotlib.pyplot as plt


def derCal(func,wrt):
    x = Symbol('x')
    d = Derivative(func,wrt).doit()
    plot(func,d)
    pprint(d)


if __name__=='__main__':
    func = input("Enter the function:")
    wrt = input("Enter wrt :")
    plot(func)
    derCal(func,wrt)