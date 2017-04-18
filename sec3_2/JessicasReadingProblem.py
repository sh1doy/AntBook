P = 10
a = [1,3,2,5,3,4,2,3,1,2]

def solve(P, a):
	s = set(a)
	right = P
	left = 0
	while right-left>1:
		center = (right+left)//2
		if set(a[:center]) == s:
			right = center
		else:
			left = center
	d = {}
	for i in a[:center]:
		d[i] = 0
	for i in a[:center]:
		d[i] += 1
	
	left = 0
	right = center-1
	minlen = right-left+1

	while right<len(a):
		d[a[left]] -= 1
		if d[a[left]] == 0:
			while d[a[left]] == 0:
				right+=1
				if right>=P:
					return(minlen)
				d[a[right]] += 1
		left+=1
		minlen = min(minlen, right-left+1)


print(solve(P,a))














