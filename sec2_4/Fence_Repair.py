#Fence Repair PKU 3253
N=20000
L=[]
from random import randint
for i in range(N):
	L.append(randint(1,50000))

from queue import PriorityQueue

def fence_repair(N,L):
	q=PriorityQueue()
	for i in L:
		q.put(i)
	count=0
	while(q.qsize()!=1):
		a=q.get()
		b=q.get()
		q.put(a+b)
		count+=a+b
	return(count)

print(fence_repair(N, L))

