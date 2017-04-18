def lake_counting(field):
	field_x_length = len(field)
	field_y_length = len(field[0])
	lake_count = 0
	from queue import Queue
	q = Queue()
	def dfs(x,y):
		if field[x][y] != 0:
			return(None)
		field[x][y] = 1
		for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
			nx = x + dx
			ny = y + dy
			if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and field[nx][ny] == 0):
				q.put((nx,ny))
	for i in range (0, field_x_length):
		for j in range (0, field_y_length):
			if (field[i][j] == 0):
				q.put((i, j))
				while not q.empty():
					dfs(*q.get())
				lake_count+=1
	return(lake_count)

field =[
[0,1,0,0,0,0,0],
[0,1,0,0,1,1,1],
[1,1,0,1,0,0,0],
[0,0,1,0,0,0,0],
[0,0,1,0,0,0,0],
[0,0,1,0,0,0,0]]

print(lake_counting(field))