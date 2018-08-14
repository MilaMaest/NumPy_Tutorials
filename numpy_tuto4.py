import numpy as np
from math import pi

#   linspace(start, end, steps , ..)
a = np.linspace(0, 10, 11, retstep=True)
print('a : ', a)

#   the sum of all the elements of an array
b = np.array([
    [1,2,3,4]
])

print('the sum of the elements of b : ', b.sum())

c = np.array([
    [3,2,3,2],
    [3,5,0,5],
    [7,0,7,4]
])
print('the sum of the elements of c : ', c.sum())

#   sum() by dimension (dimensions are also called axis)
print('sum axis 0 in c array : ', np.sum(c, axis=0))
print('sum axis 1 in c array : ', np.sum(c, axis=1))


#   get the minimum value in an array
print('the min in c is : ' , c.min())

#   get the maximum value in an array
print('the max in c is : ' , c.max())

m = np.array([
    [5,0,7],
    [5,0,7]
])

#   nonzero : returns a tuple of arrays one for each dimension conntaining the indices of the non-zero elements in that dimension
print('none zero m : \n', np.nonzero(m))

#   transpose: groups the indices by element
print('none zero transpose m :\n ', np.transpose(np.nonzero(m)))

print()

#   condition: if an element is greater than 3 it's gonna return True otherwise False.
print(c>2)
print()


xx = np.array([
    [7,2],
    [9,0]
])
print(np.transpose(np.nonzero(xx>3)))