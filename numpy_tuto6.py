import numpy as np

a = np.array([
    [1,1,1],
    [2,2,2]
])

b = np.array([
    [9,9,9],
    [7,7,7]
])

print('Vertical Stacking a over b : \n', np.vstack((a,b)))

print('Horizontal Stacking a over b : \n', np.hstack((a,b)))

print('Column Stacking a over b : \n', np.column_stack((a,b)))

print('Concatenate a and b : \n', np.concatenate((a,b)))

#   splits
c = np.array([
    [9,8,7,6,5,4,3,2,1]
])

print('Horizontal split c into 3 small arrays => ', np.hsplit(c, 3))

