#implement Depth first search using python

graph = {
    # LAB Exercises
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
 
	# 'A': ['B', 'C'],
	# 'B': ['D', 'E'],
	# 'C': ['F', 'G'],
	# 'D': ['H', 'I'],
	# 'H': [],
	# 'I': [],
	# 'E': ['J', 'K'],
	# 'J': [],
	# 'K': [],
	# 'F': ['L', 'M'],
	# 'L': [],
	# 'M': [],
	# 'G': ['N', 'O'],
	# 'N': [],
	# 'O': [],
 
	# LAB REPORT ASSIGNMENT
	'A': ['G', 'D', 'B'],
	'B': ['E', 'F'],
	'G': ['E', 'A'],
	'D': ['A', 'F'],
	'F': ['D', 'C'],
	'E': ['B', 'G'],
	'C': ['F'],
}

stack = []

visited = []


def dfs(visited, stack, graph, node):
	stack.append(node)
  
	while stack:
		m = stack.pop()
		if m not in visited:
			print(m)
			visited.append(m)
			for n in reversed(graph[m]):
				if n not in visited:
					stack.append(n)  

dfs(visited, stack, graph, 'A')