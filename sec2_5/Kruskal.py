matrix=[\
[-1, 2, 3, 1, -1],\
[2, -1, -1, 4, -1],\
[3, -1, -1, 1, 1],\
[1, 4, 1, -1, 3],\
[-1, -1, 1, 3, -1]\
]

# マージO(n)かかっちゃう
class union_find(object):
 	"""union-find tree"""
 	def __init__(self, length):
 		self.length = length
 		self.unionnumber=0
 		self.unionlist=[[]]
 		self.num=list(-1 for i in range(length))

 	def unite(self,i,j):
 		if self.num[i]==-1:
 			if self.num[j]==-1:
 				self.unionlist[self.unionnumber].extend([i,j])
 				self.num[i]=self.unionnumber
 				self.num[j]=self.unionnumber
 				self.unionnumber+=1
 				self.unionlist.append([])
 			else:
 				tmp=i 
 				i=j 
 				j=tmp 
 		if self.num[i]!=-1:
 			if self.num[j]!=-1:
 				if self.num[i]==self.num[j]:
 					pass
 				else:
 					self.unionlist[self.num[i]].extend(self.unionlist[self.num[j]])
 					tmp=self.num[j]
 					for k in self.unionlist[self.num[j]]:
 						self.num[k]=self.num[i]
 					self.unionlist[tmp]="del"
 			else:
 				self.num[j]=self.num[i]
 				self.unionlist[self.num[i]].append(j)

 	def same(self,i,j):
 		if self.num[i]==-1 or self.num[j]==-1:
 			return(False)
 		else:
 			return(self.num[i]==self.num[j])

# 枝なし=-1 枝行列用
def Kruskal(matrix):
	length=len(matrix)
	edgelist=[]
	for i in range(length):
		for j in range(i+1):
			if matrix[i][j]!=-1:
				edgelist.append([j,i,matrix[i][j]])
	edgelist.sort(key=lambda x:x[2],reverse=True)
	result=[[-1 for i in range(length)] for j in range(length)]
	union=union_find(length)
	while(edgelist!=[]):
		edge=edgelist.pop()
		i,j,score=edge
		if union.same(i,j):
			pass
		else:
			union.unite(i,j)
			result[i][j]=score
			result[j][i]=score	
	return(result)

# 枝用
def Kruskal_(edges,length):
	edgelist=edges
	edgelist.sort(key=lambda x:x[2],reverse=True)
	result=[]
	union=union_find(length)
	while(edgelist!=[]):
		edge=edgelist.pop()
		i,j,score=edge
		if union.same(i,j):
			pass
		else:
			union.unite(i,j)
			result.append(edge)
	return(result)


a=Kruskal(matrix)
from pprint import pprint
pprint(a)
