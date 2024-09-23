def bfs(startNode, destNode, graph):
  queue = [[startNode]]
  visited = []
  while(queue):
    path = queue.pop(0)
    currNode = path[-1]
    if currNode not in visited:
      visited.append(currNode)
      for neighbor in graph[currNode]:
        newPath = list(path)
        newPath.append(neighbor)
        queue.append(newPath)
        if neighbor == destNode:
          return newPath
          

def populateGraph(row, column):
  graph = {}
  for i in range(1, (row*column)+1):
    neighbors = []
    if i != 1 and i % column != 1:
      neighbors.append(i-1)
    if i % column != 0:
      neighbors.append(i+1)
    if i <= column * (row - 1):
      neighbors.append(i+column)
    if i > column:
      neighbors.append(i-column)
    graph[i] = neighbors
  return graph

print(bfs(1, 64, populateGraph(8,8)))