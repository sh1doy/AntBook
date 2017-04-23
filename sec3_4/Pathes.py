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
		[0, 1, 1, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1],
		[1, 0, 0, 0]
	]

	return(pow(int(matpow(A, n).sum()),1,10007))

print(solve(10**9))



