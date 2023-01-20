global infinity 
infinity = float('inf')

class Node():
    def __init__(self, node: str) -> None:
        self.node = node
        self.visited = False
        self.distance = infinity
        self.previous = None
        self.children = []
    
class Child():
    def __init__(self, data: str, weight: int) -> None:
        self.node = data
        self.weight = weight

graph = {
    'A':Node('A'),
    'B':Node('B'),
    'C':Node('C'),
    'D':Node('D'),
    'E':Node('E'),
    'x':Node('x')
}

graph['A'].children = [Child('B',10), Child('C',7)]
graph['B'].children = [Child('A',10), Child('E',4), Child('D',4)]
graph['C'].children = [Child('A',7), Child('E',3)]
graph['D'].children = [Child('B',4), Child('x',1)]
graph['E'].children = [Child('B',4), Child('C',3), Child('x',6)]
graph['x'].children = [Child('D',1), Child('E',6)]


def Dijkstra(graph, start, goal):
    # set start node
    graph[start].distance = 0
    
    # For each node in the graph
    for node in graph:
        # Find the node with the shortest distance that has not been visited
        shortestDistance = infinity
        shortestNode = None
        for n in graph:
            if graph[n].distance < shortestDistance and not graph[n].visited:
                shortestDistance = graph[n].distance
                shortestNode = n
    
        # For each connected node that has not been visited:
        for child in graph[node].children:
            if not graph[child.node].visited:
                # Calculate the distance from the start
                newDistance = graph[node].distance + child.weight
                
                #If the distance from the start is lower than the current distance for that node
                if newDistance < graph[child.node].distance:
                    # Set the shortest distance to the newly calculated distance
                    shortestDistance= newDistance
                    # Set the "previous node" to be the current node
                    graph[child.node].distance = newDistance
                    graph[child.node].previous = node
                    
        # Set visited attribute to be true
        graph[node].visited = True
            
            
    # Start from the goal node
    path = []
    path.append(graph[goal].node)
    previous = None
    # Repeat until start node is reached 
    while previous is not start:
        # Add the previous node to the start of a list
        previous = graph[path[len(path)-1]].previous
        path.append(graph[previous].node)
    
    # Output the list    
    return path
        
    
print(Dijkstra(graph,'A','x'))

