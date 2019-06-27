array = [[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]]


n = len(array)


levels = [0] * n
level = 0
selection = []
forward = True

while levels[0] < n:
	if not forward:
		level -= 1
		selection.pop()
		levels[level] += 1

	if level == n:
		print(selection)
		forward = False
	elif levels[level] < n:
		forward = True
		selection.append(array[levels[level]][level])
		level += 1
	else:
		levels[level] = 0
		forward = False
		if level == 0: 
			break
	# print(levels)