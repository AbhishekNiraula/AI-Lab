#implement Breadth first search using python

graph = {
    # Commented Graphs -> Lab Work
	# 'A': ['B', 'C'],
	# 'B': ['D', 'E'],
	# 'C': ['F', 'G'],
	# 'D': [],
	# 'E': [],
	# 'F': [],
	# 'G': [],
 
	# 'A': ['B', 'C'], 
	# 'B': ['D', 'E'],
	# 'C':  ['F'],
	# 'D': ['X'],
	# 'E': ['I'],
	# 'F': ['I', 'H'],
	# 'I': [],
	# 'H': [],
	# 'X': [],
 
	# LAB REPORT ASSIGNMENT
 	'A': ['G', 'D', 'B'],
	'B': ['E', 'F'],
	'G': ['E', 'A'],
	'D': ['A', 'F'],
	'F': ['D', 'C'],
	'E': ['B', 'G'],
	'C': ['F'],
}

queue = []

visited = []


def bfs(visited, queue, node):
	visited.append(node)
	queue.append(node)
 
	while queue:
		m = queue.pop(0)
		print(m)
		for p in graph[m]:
			if p not in visited:
				visited.append(p)
				queue.append(p)

bfs(visited, queue, 'A')
