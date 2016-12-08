

coin = [1,5,10,50,100,500]

def solve(money):
	c=0
	coin.sort(reverse=True)
	for i in coin:
		c+=int(money/i)
		money=money%i
	return(c)

print(solve(66666))