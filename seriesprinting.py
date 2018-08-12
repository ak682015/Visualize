# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:14:12 2018

@author: Arman
"""
from sympy import Symbol, pprint, init_printing

def series(n, x_value):
    
    init_printing(order='rev-lex')
    x=Symbol('x')
    a=x
    for i in range(2,n+1):
        a+=(x**i/i)
    pprint(a)
        #print("",end="+")
        
    a_value = a.subs({x:x_value})
    print(a_value)
    
def user_cal(user_expr, terms, x_value):
    expr = sympify(user_expr)
    print(expr.subs({x:x_value}))


if __name__=='__main__':
    user_expr = input("Enter the expression:")
    terms = int(input("Enter the n :"))
    x_value = int(input("Enter the value at which: "))
    #series(terms, x_value)
    user_cal(user_expr, terms, x_value)