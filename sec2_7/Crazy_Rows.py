# Crazy_Rows
import random
n = 4
l = [[0,0,1,0],[1,1,0,0],[1,1,0,0],[1,0,0,0]]

def solve(l):
	l1=[]
	for i in l:
		n=0
		for j in range(len(i)):
			if i[j]==1:
				n=j+1
		l1.append(n)
	c=0
	for i in range(len(l1)):
		if l1[i]>i+1:
			for j in range(i+1,len(l1)):
				if l1[j]<=i+1:
					l1.insert(i,l1.pop(j))
					c+=j-i
					break
	return(c)

print(solve(l))