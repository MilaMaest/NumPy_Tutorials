import numpy as np

x = np.array([ [1,2,3,4], [10, 20, 30, 40] ])
y = np.array([ [2,3,7,8] ])
z = np.array([[1,2,3,4]])

#   Addition
print('x + y = \n', x+y)

#   Subtraction
print('x - y = \n', x-y)

#   Multiplication : elementwise product
print('x * y = \n', x*y)

#   Division and then rounding up
print('x / y = \n', np.round(x/y))

#   getting the remainder using modulo
print('x % y = \n', x%y)

#   y**2
print('y**2 = \n', y**2)

#   ' += ,*=, /=, -= ' operations modify an existing array instead of creating a new one

z *= 3
print('z *= 3 :\n ',z)

