matrix1=[\
[0,1,1],\
[1,0,1],\
[1,1,0]]

matrix2=[\
[0,1,0,1],\
[1,0,1,0],\
[0,1,0,1],\
[1,0,1,0]]

matrix3=[\
[0,1,0,0],\
[1,0,0,0],\
[0,0,0,1],\
[0,0,1,0]]

def bipartite_graph(matrix):
	length=len(matrix)
	stack=[]
	color=[0 for i in range(length)]
	nodelist=list(range(length))	#連結でないときのため
	while(nodelist!=[]):			
		stack.append(nodelist[0])	#最初に1箇所を塗る
		color[nodelist[0]]=1
		while(stack!=[]):			#繋がっているところを塗っていく
			now=stack.pop()
			nodelist.remove(now)
			for i in range(length):
				if matrix[now][i]:
					if color[i]==color[now]:
						return(False)
					elif color[i]==0:
						color[i]=-color[now]
						stack.append(i)
		return(True)

		
print(bipartite_graph(matrix3))