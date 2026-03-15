#Dijkstra implemeted in python to solve SSSP where each node has a cost
#To solve, each node in the  given graph will be converted to two nodes: 
# one for every route in and one for every route out
# inbetween the two created nodes, there will be an edge with the cost of travel



def NodeCostDijkstra(numNodes, delays, routes, source):
    #for each node
    #   all routes in stay same
    #   all routes from node get routed to new node
    #   create route to new node with delay as cost
    for i in range(numNodes):
        
        for route in routes:
            if route[0] == i:
                route[0] = i+numNodes
        if i != source:
            routes.append([i,i+numNodes,delays[i]])
        else:
            routes.append([i,i+numNodes,0])
    
    print(routes)

    numNodes *= 2
    

    ## Dijkstra
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
        if u == -1:
            break
        
        #update distances from chosen node
        for route in routes:
            if route[0] == u and minDist + route[2] < distances[route[1]]:
                distances[route[1]] = minDist + route[2]
        
        #set chosen node to visited
        visited[u] = True
              


    return distances[0:int(numNodes/2)]