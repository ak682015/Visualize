# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:48:04 2018

@author: Arman
"""

from sympy import *

x = Symbol('x')
y = Symbol('y')

expr1 = x+y-12
expr2 = x-y-32

ans = (solve((expr1,expr2),dict=True))
p = plot(3*x**3,x**3,(x,-10,10), legend=True,show=False)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()
#expr = x**2+3*x+10
#pprint(solve(expr,dict=True))