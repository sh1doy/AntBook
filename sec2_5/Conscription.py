#Conscription

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

# 枝なし=-1
def Kruskal(edges,length):
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

N=5
M=5
R=[\
[4, 3, 6831],\
[1, 3, 4583],\
[0, 0, 6592],\
[0, 1, 3063],\
[3, 3, 4975],\
[1, 3, 2049],\
[4, 2, 2104],\
[2, 2, 781 ]\
]

def solve(N,M,R):
	for i in range(len(R)):
		R[i][1]+=N
		R[i][2]=-R[i][2]
	res=Kruskal(R,N+M)
	cos=(M+N)*10000
	for i in res:
		cos+=i[2]
	return(cos)

print(solve(N, M, R))

















