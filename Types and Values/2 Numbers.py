from decimal import *
x= .1+ .1 + .1 - .3

print('x is {}'.format(x)) # it is wrong

a = Decimal('.10')
b = Decimal('.30')
y = a+a+a-b

print('y is {}'.format(y))
