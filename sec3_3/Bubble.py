#Bubble
# ありホント解き方ぜんぜんちがう (nlog(n))

# n = 4
# a = [3,1,4,2]

from random import randint

n = 100000
a = [randint(-10000000000000,10000000000000) for i in range(n)]

def solve(n,a):
	i = 1
	while i<n:
		i<<=1
	array = [([],0) for i in range(i*2)]
	for i in range(n):
			array[len(array)//2+i] = ([a[i]],0)

	def merge(i):
		if i >= len(array)//2:
			return(array[i])
		else:
			arr = []
			larr,lval = merge(i*2)
			rarr,rval = merge(i*2+1)
			count = lval + rval
			larr.reverse()
			rarr.reverse()
			while len(larr)>0 and len(rarr)>0:
				if larr[-1] >= rarr[-1]:
					count += 1
					arr.append(rarr.pop())
				else:
					arr.append(larr.pop())
			while len(larr)>0:
				arr.append(larr.pop())
			while len(rarr)>0:
				arr.append(rarr.pop())
			return((arr,count))



	return(merge(1)[1])

from time import time
t0 = time()
print(solve(n,a))
print(time() - t0)