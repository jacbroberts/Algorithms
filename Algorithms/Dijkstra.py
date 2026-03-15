#Dijkstra implemeted in python to solve SSSP

def Dijkstra(numNodes, routes, source):
    #initialize distances as infinity
    distances = [10e9] * numNodes
    #initialize all nodes as unvisited
    visited = [False] * numNodes
    
    #set distance to self to 0
    distances[source] = 0

    
    #visit each node once
    for i in range(numNodes):
        #choose node with minimum distance
        minDist = 10e9
        u = -1 
        for idx,val in enumerate(distances):
            if val < minDist and visited[idx] == False:
                minDist = val
                u = idx
        
        #update distances from chosen node
        for route in routes:
            if route[0] == u and minDist + route[2] < distances[route[1]]:
                distances[route[1]] = minDist + route[2]
        
        #set chosen node to visited
        visited[u] = True
              


    return distances

