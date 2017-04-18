# Flip Tile

N=4
M=4
t=[ [1,0,0,1],
	[0,1,1,0],
	[0,1,1,0],
	[1,0,0,1]]

def solve(N,M,t):
	opt = [[0 for i in range(M)] for j in range(N)]
	dx = [0,0,0,1,-1]
	dy = [0,1,-1,0,0]
	def binary(i,M):
		return(format(i,"0"+str(M)+"b"))
	smallest = float("inf")
	for fline in [list(map(int,binary(i,M))) for i in range(pow(2,M))]:
		# print(fline)
		tmp = [[y for y in x] for x in t]
		res = [[0 for i in range(M)] for j in range(N)]
		res[0]=fline
		c = sum(fline)
		for i in range(M):
			if fline[i]==1:
				for k in range(5):
					if 0<=i+dx[k] and i+dx[k]<M and j+dy[k]>=0:
						tmp[j+dy[k]][i+dx[k]] = (tmp[j+dy[k]][i+dx[k]]+1)%2
		for j in range(1,N-1):
			for i in range(M):
				if tmp[j-1][i]==1:
					res[j][i]=1
					c+=1
					for k in range(5):
						if 0<=i+dx[k] and i+dx[k]<M:
							tmp[j+dy[k]][i+dx[k]] = (tmp[j+dy[k]][i+dx[k]]+1)%2
		# print(tmp)
		if sum(tmp[N-1])!=0:
			continue
		if c<smallest:
			smallest=c
			opt = res[:]
	if smallest==float("inf"):
		return("IMPOSSIBLE")
	else:
		return(smallest,opt)



	


print(solve(N,M,t))

