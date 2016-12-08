# マージO(n)かかっちゃうやつ
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
 		return(self.num[i]==self.num[j])




