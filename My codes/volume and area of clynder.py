#حجم استوانه =ارتفاع *شعاع به توان 2 *عدد پی 
#(حجم مساحت کل)=2*pi*radius*height+2*(pi*(radius)^2)
from cmath import pi
import math
height=float(input('measerment of height--->  '))
radius=float(input('lenght of radius--->  '))
volume=(pi*height*radius*radius)
total_area=(2*pi*(radius*height))+(2*(pi*(radius)**2))
print('volum is --->',volume)
print('total area is --->',total_area)