g = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

stack = ['A']  
visited = [] 
while stack: 
    i = stack.pop() 
    if i not in visited:
        visited.append(i)
        for j in g[i][::-1]: 
            stack.append(j) 
    print("Visited:", visited, "| Stack:", stack)

print("Finally  :", visited)