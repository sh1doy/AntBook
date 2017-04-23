# Fib

import numpy as np

A = [
	[1, 1],
	[1, 0]
]

def matpow(A, n):
	A = np.array(A)
	res = np.array([[1,0],[0,1]])
	i = 1
	while n > 0:
		if n & 1 == 1:
			res = res.dot(A)
		A = A.dot(A)
		n >>= 1

	return(res)

def solve(n):
	return(matpow(A, n-2)[0,:].sum())

print(solve(10**16))



