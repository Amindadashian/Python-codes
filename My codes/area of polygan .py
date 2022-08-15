from cmath import pi
import math

from numpy import tan
nsides=int(input('please insert numbers of sides--->   '))
side_length=float(input('side length--->  '))
pArea=nsides*(side_length**2) / (4*tan(pi/nsides))
print('the area of the polygan is --->  ',pArea)
