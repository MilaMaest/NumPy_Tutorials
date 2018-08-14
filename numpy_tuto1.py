'''
    NumPy is all about homogeneous multidimensional array.
    It's element are all the same type.
    indexed by a tuple of positive integers.
    Dimensions are also called axes.
'''
import numpy as np

#   x is an array of 1 dimension
x = np.array([1, 2, 3, 4])
#   y is an array of 2 dimensions
y = np.array([
                [9,8,7,6],
                [1,2,3,4]
            ])

#   ndim : indicates the number of dimensions
print("x number of dimensions : " ,x.ndim)
print("y number of dimensions : " ,y.ndim)

#   shape : returns a tuple of integers that indicate the size of an array in each dimension
print("x shape : " ,x.shape)
print("y shape : " ,y.shape)

#   size : returns the total number of elements
print("x size", x.size)
print("y size", y.size)

#   dtype : returns an object that describs the type of elements in the array
print("x type", x.dtype)
print("y type", y.dtype)

#   itemsize : retruns the size in bytes of each elements of the array
print("the size of each item in bytes in array x :  ", x.itemsize)
print("the size of each item in bytes in array y : ", y.itemsize)

#   type()
print("Type of x : ", type(x), "\nType of y :", type(y))

# arange() : return an ndarray rather than a list with generated values
z = np.arange(7)
z1 = np.arange(7.0)
z2 = np.arange(5, 15)
z3 = np.arange(0,10, 3)
print("z:  ", z)
print("z1: ",z1)
print("z2: ",z2)
print("z3: ",z3)

#   reshape() : gives a new shape to an array without changing its data
print("reshaping z3 : \n", z3.reshape(2,2))

