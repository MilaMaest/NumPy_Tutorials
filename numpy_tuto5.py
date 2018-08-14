import numpy as np

x = np.array(
    [51,62,37,94,105,61,7,118,29]
)

print('x[8] = ', x[6])

print('x[2:5] = ', x[2:5] )

print('x[:2:5] = ', x[:5:2] )

#   Assiging every 3rd element to 9999
x[::3] = 9999
print('x',x)

#   reversing x
print('reversed x : ',x[::-1])

print()
# ------------------- Multidimensional Arrays -------------------

#   the random() method generates float values from 0 to 1
#   so when we multiply by 100 it generates random numbers from 0 to 100
#   the round() method rounds floats to int

y = np.round(np.random.random((3,3))*100)
print(y)

z = np.array([
    [3,4,5,6],
    [1,2,1,9],
    [6,5,11,2],
    [36,45,6,7]
])

#   z[rows, columns]
print('z[3,2] = ' ,z[3,2])

#   z[0:2, column]
print('z[0:2, 3] = ',z[0:2, 3])

print('z[0:2, :] = \n',z[0:2, : ]) #  each column in the first and second row

print('the last row', z[-1])


#   Iterating
print('Iterating :')
for row in z: print(row)

#   the flat attribute iterats over all the elements
for e in z.flat: print(e)

#   ravel() : returns the array flattened
print(z.ravel())