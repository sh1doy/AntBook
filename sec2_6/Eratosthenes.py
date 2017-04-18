# Eratosthenes

n=1000000

from math import sqrt
def eratosthenes(num):
	table=[True for i in range(num+1)]
	root = int(sqrt(num))
	for i in range(2,root+1):
		if table[i]:
			for j in range(num+1)[i**2::i]:
				table[j]=False
	return([i for i in range(2,num+1) if table[i]==True])

print(len(eratosthenes(n)))



