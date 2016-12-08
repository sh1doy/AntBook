# 食物連鎖 POJ1182
N=100
K=7
Info=[]
Info.append(("same",101,1))
Info.append(("eat_",1,2))
Info.append(("eat_",2,3))
Info.append(("eat_",3,3))
Info.append(("same",1,3))
Info.append(("eat_",3,1))
Info.append(("same",5,5))

def food_chain(N,K,Info):
	table=[[3*x, 3*x+1, 3*x+2] for x in range(N)]
	def same(x,y):
		for i in [0,1,2]:
			for j in [0,1,2]:
				if i==j:
					pass
				else:
					if table[x][i]==table[y][j]:
						return(False)
		return(True)

	def eat(x,y):
		for i in [0,1,2]:
			for j in [0,1,2]:
				if not(j-i==1 or j-i==-2):
					if table[x][i]==table[y][j]:
						return(False)
		return(True)

	count=0
	for i in Info:
		x=i[1]
		y=i[2]
		if not(x<100 and y<100):
			count+=1 
			continue
		if i[0]=="same":
			if same(x,y):
				for i in [0,1,2]:
					table[y][i]=table[x][i]
			else:
				count+=1
		elif i[0]=="eat_":
			if eat(x,y):
				for i in [[0,1],[1,2],[2,0]]:
					table[y][i[1]]=table[x][i[0]]
			else:
				count+=1
	return(count)


print(food_chain(N, K, Info))

