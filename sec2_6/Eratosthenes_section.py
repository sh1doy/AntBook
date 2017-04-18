# Eratosthenes_section
# [a,b)

a=22801763489
b=22801787297

from math import sqrt
def eratosthenes_section(a,b):
	if a<2:
		a=2
	rootb = int(sqrt(b))
	maintable=[True for i in range(b-a)]
	btable=[True for i in range(rootb+1)]
	for i in range(2,rootb+1):
		if btable[i]:
			for j in range(rootb+1)[i**2::i]:
				btable[j]=False
			for j in range(a,b)[-a%i::i]:
				if j!=i:
					maintable[j-a]=False
	return([i for i in range(a,b) if maintable[i-a]==True])

print(len(eratosthenes_section(a,b)))



