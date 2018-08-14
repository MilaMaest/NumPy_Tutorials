import numpy as np

x = np.array([
                [2,8,6],
                [5,9,3],
                [9,6,7]
            ])
print(x)

y = np.array([
    (1,1,1),
    (2,2,2),
    (3,3,3)
])
print(y)

#       Specify the type of array explicitly
z = np.array([ [7,8,7,8], [5,9,5,9] ], dtype=float)
print(z)

#   zeros()
zeros_array = np.zeros((2,4))
print('Zeros array : \n',zeros_array)

zeros_like_array =np.zeros_like(zeros_array)
print(zeros_like_array)

#   ones()
ones_array = np.ones((3,5))
print('Ones array : \n',ones_array)

#   make an empty array
empty_array = np.empty( (4,4) )
print('Empty array', empty_array) # the values may vary

