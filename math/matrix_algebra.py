# Matrix Algebra

import numpy as np

A = np.matrix([[1, 2, 3], [2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.matrix([[1], [8], [0], [5]])



###1. Matrix Dimensions

##1.1 A
print('Size of A: ' + str(A.shape))
#Answer: (2, 3)

##1.2 B
print('Size of B: ' + str(B.shape))
#Answer: (2, 2)

##1.3 C
print('Size of C: ' + str(C.shape))
#Answer: (3, 2)

##1.4 D
print('Size of D: ' + str(D.shape))
#Answer: (2, 3)

##1.5 u
print('Size of u: ' + str(u.shape))
#Answer: (4,)

##1.6 w
print('Size of w: ' + str(w.shape))
#Answer: (4, 1)


###2. Vector Operations
a = 6

##2.1 u + v
print('u + v = ' + str(u + v))
#Answer: [9  7 -4  9]

##2.2 u - v
print('u - v = ' + str(u - v))
#Answer: [3 -3 -2  1]

##2.3 au
print('au = ' + str(a * u))
#Answer: [36  12 -18  30]

##2.4 uv
print('uv = ' + str(u * v))
#Answer: [18 10  3 20]

##2.5 ||u||
print('||u|| = ' + str(np.sqrt(u.dot(u))))
#Answer: 8.60232526704


###3. Matrix Operations

##3.1 A + C
print('A + C = ' + 'not defined')
#Answer: not defined

##3.2 A - C^T
print('A - C^T = ' + str(A - C.transpose()))
#Answer:
#[[-4 -7 -3]
 #[ 3  6  4]]

##3.3 C^T + 3D
print('C^T + 3D = ' + str(C.transpose() + 3 * D))
#Answer:
#[[14  3  3]
 #[ 2  7  9]]

##3.4 BA
print('BA = ' + str(B.dot(A)))
#Answer:
#[[-1 -5 -1]
 #[ 2  7  4]]

##3.5 BA^T
print('BA^T = ' + 'not defined')
#Answer: not defined

##3.6 BC
print('BC = ' + 'not defined')
#Answer: not defined

##3.7 CB
print('CB = ' + str(C.dot(B)))
#Answer:
#[[ 5 -6]
 #[ 9 -8]
 #[ 6 -6]]

##3.8 B^4
print('B^4 = ' + str(B.dot(B).dot(B).dot(B)))
#Answer:
#[[ 1 -4]
 #[ 0  1]]

##3.9 AA^T
print('AA^T = ' + str(A.dot(A.transpose())))
#Answer:
#[[14 28]
 #[28 69]]

##3.10 D^TD
print('D^TD = ' + str(D.transpose().dot(D)))
#Answer:
#[[10 -4  0]
 #[-4  8  8]
 #[ 0  8 10]]
