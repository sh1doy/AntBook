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
		self.prev=[0 for x in range(self.size)]
		self.prev[start]=-1
		yet=list(range(self.size))
		yet.remove(start)
		now=start
		while(yet!=[]):
			nearest_num=0
			nearest_dis=float("inf")
			for i in yet:
				total_dis=distancemap[now][i]+self.distance[now]
				self.distance[i]=min(total_dis, self.distance[i])
				#次に見るものを最小値を探索せずに決められる
				if self.distance[i]<=nearest_dis:
					nearest_dis=self.distance[i]
					nearest_num=i
			yet.remove(nearest_num)
			self.prev[nearest_num]=now
			now=nearest_num

	def route(self,goal):
		route=[]
		while(True):
			route.append(self.prev[goal])
			goal=self.prev[goal]
			if goal==self.start:
				break
		route.reverse()
		return(route)
