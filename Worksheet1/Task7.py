import numpy as np
A=np.array([[1,2,3],
   [3,7,4],
   [2,5,3]])
b=np.array([1,2,3])

A_T=A.T
print(A_T)

Ab=np.dot(A,b)
print(Ab)

A_inv=np.linalg.inv(A)
print(A_inv)

x=np.linalg.solve(A, b)
print('x är',x)