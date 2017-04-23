# Minimizing maximizer

n = 40
m = 6
s, t = zip(*[(20,30),(1,10),(10,20),(20,30),(15,25),(30,40)])

class RMQ(object):
	def __init__(self, data):
		self.NAN = float("inf")
		self.FUNC = min
		size = len(data)
		self.n = 1
		while size > self.n: #2のべき乗にしておく(実装が簡単)array[0]は使わない
			self.n <<= 1
		self.array = [self.NAN for i in range(self.n*2)]
		self.array  
		self.array[self.n:self.n+size] = data
		def heapify(m):
			if self.n <= m:
				return self.array[m]
			else:
				self.array[m] = self.FUNC(heapify(2*m),heapify(2*m+1))
				return self.array[m]
		heapify(1)

	def get(self,a,b):	#[a,b]を調べる
		def foo(k,a,b,l,r): #[a,b)を調べる
			if b <= l or r <= a:
				return(self.NAN)
			elif a <= l and r <= b:
				return(self.array[k])
			else:
				return(self.FUNC(
					foo(2*k,a,b,l,(r+l)//2),
					foo(2*k+1,a,b,(r+l)//2,r)
					))

		return(foo(1,a,b+1,0,self.n))

	def put(self,a,x):
		a += self.n
		self.array[a] = x
		while a!=1:
			a //= 2
			self.array[a] = self.FUNC(self.array[a], x)


def solve(n,m,s,t):
	inf = float("inf")
	data = [inf for _ in range(n)]
	data[0] = 0

	q = RMQ(data)
	for l,h in zip(s,t):
		q.put(h-1, min(q.get(l-1,h-1)+1, q.get(h-1,h-1)))

	return(q.get(h-1,h-1))

print(solve(n,m,s,t))













