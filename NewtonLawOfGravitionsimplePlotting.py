# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 13:31:48 2018

@author: Arman
"""
#import pylab
'''from pylab import plot, show, legend, title, xlabel, ylabel 

#x_coordinates = [1,2,2.5]
#y_coordinates = [7,6.7,6.7]
#plot(x_coordinates, y_coordinates, marker = 'o')

#nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
#years = range(2000,2013)
#plot( years, nyc_temp, marker = 'o') 


nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]

months = range(1,13)

plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
legend([2000,2006,2012])
title('AVERAGE MONTHLY')
xlabel('MONTHS')
ylabel('TEMP')

show()

'''

''' The relationship between gravitational force and distance between two bodies '''
import matplotlib.pyplot as plt
# Draw the graph 
def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distance')
    plt.show()
    
def generate_F_r():    
    # Generate values for r u
    r = range(100, 1001, 50)     
    # Empty list to store the calculated values of F    
    F = []
    # Constant, G    
    G = 6.674*(10**-11)    
    # Two masses    
    m1 = 0.5    
    m2 = 1.5
    # Calculate force and add it to the list, F v     
    for dist in r:        
        force = G*(m1*m2)/(dist**2)        
        F.append(force)
    # Call the draw_graph function w     
    draw_graph(r, F)
if __name__=='__main__':    
    generate_F_r()