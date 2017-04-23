# number of path

import numpy as np


def matpow(A, n):
	A = np.array(A)
	res = np.eye(A.shape[1])
	while n > 0:
		if n & 1 == 1:
			res = res.dot(A)
		A = A.dot(A)
		n >>= 1

	return(res)

def solve(n):
	A = [
		[0, 1],
		[1, 1]
	]
	n+=1
	size = len(A)
	z = np.zeros(np.array(A).shape)
	e = np.eye(z.shape[1])

	A = np.c_[np.r_[A,e], np.r_[z,e]]

	return(matpow(A, n)[size:2*size, :size]-e)

print(solve(2))



