# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:25:54 2018

@author: Arman
"""

from sympy import *

x = Symbol('x')
y = Symbol('y')

expr = x**2+2*x*y+y**2

#print(expr.subs({x:1,y:2}))
f = (expr.subs({x:1,y:x-1}))
print(expr.subs({x:1,y:x-1}))
print(simplify(f))