# Domino

n = 3
m = 3

color = [
	[0,0,0],
	[0,1,0],
	[0,0,0]
]

def solfe(n, m, color):
	dp = [[0 for i in range(m)] for i in range(2)]
	