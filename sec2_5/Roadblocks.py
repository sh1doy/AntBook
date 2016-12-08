#Roadblocks

class Dijkstra(object):
	"""
	ダイクストラ法,(N^2)
	ステータス:distance(list),prev(list),size(int)
	distancemap[i][j]->Distance of edge i to j
	"""
	def __init__(self, distancemap, start):
		self.start=start
		self.size=len(distancemap)
		self.distance=[float("inf") for x in range(self.size)]
		self.distance[start]=0
		self.distance2=[float("inf") for x in range(self.size)]
		self.distance2[start]=0
		self.prev=[0 for x in range(self.size)]
		self.prev[start]=-1
		yet=list(range(self.size))
		yet.remove(start)
		now=start
		while(True):
			nearest_num=0
			nearest_dis=float("inf")
			#もどったりするわけなのでyetに入ってるの以外も見ないと
			for i in [x for x in range(self.size) if distancemap[now][x]!=float("inf")]:
				#min(元の,最短で来たの)だったが、2番めから来たのも考える
				total_dis=distancemap[now][i]+self.distance[now]
				total_dis2=distancemap[now][i]+self.distance2[now]
				l=sorted([total_dis,total_dis2,self.distance[i]],reverse=True)
				self.distance[i]=l.pop()
				self.distance2[i]=l.pop()
				#次に見るものを最小値を探索せずに決められる
				if i in yet and self.distance[i]<=nearest_dis:
					nearest_dis=self.distance[i]
					nearest_num=i
			if yet==[]:
				break
			yet.remove(nearest_num)
			self.prev[nearest_num]=now
			now=nearest_num
			

inf=float("inf")
matrix=[\
[inf, 100, inf, inf], \
[100, inf, 250, 200],\
[inf, 250, inf, 100],\
[inf, 200, 100, inf]\
]

a=Dijkstra(matrix,0)
print(a.distance2.pop())



