# ASimpleProblemWithIntegers
l = [1,2,3]

def solve(arr, q):
	n = len(arr)
	i = 1
	while i < n*2:
		i <<= 1

	t = [0 for j in range(i)]
	u = [0 for j in range(i)]
	for j in range(n):
		t[i//2+j] += arr[j]

	def add(a, b, x):
		def foo(k, a, b, l, r):
			if a <= l and r <= b:
				t[k] += x
			elif r <= a or b <= l:
				pass
			else:
				wrap = min(r,b)-max(l,a)
				u[k] += x * wrap
				foo(k * 2, a, b, l, (l + r) // 2)
				foo(k * 2 + 1, a, b, (l + r)//2, r)

		foo(1, a, b + 1, 0, i//2)

	def get(a, b):
		def foo(k, a, b, l, r):
			if a <= l and r <= b:
				return(t[k]*(r-l)+u[k])
			elif r <= a or b <= l:
				return(0)
			else:
				wrap = min(r,b)-max(l,a)
				return(t[k]*(wrap) + 
					foo(k * 2, a, b, l, (l + r) // 2) +
					foo(k * 2 + 1, a, b, (l + r)//2, r))
		return(foo(1,a,b+1,0,i//2))

	res = []
	for que in q:
		if que[0] == 0:
			add(*que[1:])
		else:
			res.append(get(*que[1:]))
	# print([get(j,j) for j in range(100)])
	return(res)

def ans(arr,q):
	res = []
	for qq in q:
		if qq[0]==0:
			for i in range(qq[1],qq[2]+1):
				arr[i] += qq[3]
		else:
			res.append(sum(arr[qq[1]:qq[2]+1]))
	return(res)

# arr = [0 for i in range(8)]
# q=[
# (0,0,6,1),
# (0,1,6,20),
# (0,3,5,5),
# (1,1,5),
# (1,1,1),
# (1,0,8)
# ]
# print(solve(arr,q),ans(arr,q))

n = 10000
arr = [0 for i in range(n)]
q = []

from random import randint
for i in range(10000):
	a,b = sorted([randint(0,n-1),randint(0,n-1)])
	q.append((0,a,b,randint(-10000,10000)))
	a,b = sorted([randint(0,n-1),randint(0,n-1)])
	q.append((1,a,b))



