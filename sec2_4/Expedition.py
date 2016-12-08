#Expedition POJ2431
import queue

N=4
L=31
P=10
A=[10,14,20,21]
B=[10,5,2,4]

def expedition(N,L,P,A,B):
	now = P
	q=queue.PriorityQueue()
	count = 0
	a_end = 0
	while(now < L):
		while(a_end<len(A) and A[a_end]<=now):
			# 降順にできないから負にしてる
			q.put(-B[a_end])
			a_end+=1
		try:
			now+= -q.get_nowait()
		except:
			return(-1) #ガス欠
		count+=1
	return(count)

print(expedition(N, L, P, A, B))
		