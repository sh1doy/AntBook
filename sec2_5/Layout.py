#Layout

class Bellman_Ford(object):
	"""
	ベルマンフォード法, O(EV)
	ステータス:distance(list),prev(list),length(int)
	edge=[i, j, cost] のリスト
	"""
	def __init__(self, edge, start, length):
		self.start=start
		self.length=length
		self.distance=[float("inf") for x in range(self.length)]
		self.distance[start]=0
		self.prev=[0 for x in range(self.length)]
		self.prev[start]=-1
		self.solvable=True
		now=start
		def update():
			for i in edge:
				d=self.distance[i[0]]+i[2]
				if d<self.distance[i[1]]:
					self.distance[i[1]]=d 
					self.prev[i[1]]=i[0]
		for i in range(length-1):
			update()
		memo=[]
		for i in self.distance:
			memo.append(i)
		update()
		if memo!=self.distance:
			self.solvable=False

	def route(self,goal):
		route=[]
		while(True):
			route.append(self.prev[goal])
			goal=self.prev[goal]
			if goal==self.start:
				break
		route.reverse()
		return(route)

N=4
ML=2
MD=1
like=[[1,3,10],[2,4,20]]
dislike=[[2,3,3]]

edge=[]
for i in like:
	edge.append([i[0]-1,i[1]-1,i[2]])
for i in dislike:
	edge.append([i[1]-1,i[0]-1,-i[2]])
for i in range(N-1):
	edge.append([i+1, i, 0])

B=Bellman_Ford(edge, 0, N)
if B.solvable==False:
	print(-1)
elif B.distance[N-1]==float("inf"):
	print(-2)
else:
	print(B.distance[N-1])







