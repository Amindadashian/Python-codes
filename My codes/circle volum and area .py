#   مساحت کره=4*پی *شعاع به توان 2
#حجم کره=4/3*پی*شعاع به توان دو
from cmath import pi
import math
radius=float(input('length of radius---> '))
totalarea=4*(pi*(radius**2))
volume=(4/3)*(pi*(radius**2))

print('totalarea is--->  ',totalarea )
print('volume is --->  ',volume)