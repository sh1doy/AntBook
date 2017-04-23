# Blocks

import numpy as np


def matpow(A, n):
	A = np.array(A)
	res = np.eye(3)
	while n > 0:
		if n & 1 == 1:
			res = res.dot(A)
		A = A.dot(A)
		n >>= 1

	return(res)

def solve(n):
	A = [
		[2, 1, 0],
		[2, 2, 2],
		[0, 1, 2]
	]

	return(pow(int(matpow(A, n)[0,0].sum()),1,10007))

print(solve(2))



