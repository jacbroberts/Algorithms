"""Dijkstra implemeted in python to solve SSSP"""

def dijkstra(num_nodes, routes, source):
    """Returns a list of shortest distance from source to each other node.
    Assumes that routes all have non negative weights.
    
    Parameters:
        num_nodes (int): number of nodes in graph
        routes (list): list of edges in format [from, to, weight]
        source (int): node that distances are counted from.

    Returns:
        list: distane to each node. Distance to source node is always 0.    
    
    
    """
    #initialize distances as infinity
    distances = [10e9] * num_nodes
    #initialize all nodes as unvisited
    visited = [False] * num_nodes

    #set distance to self to 0
    distances[source] = 0


    #visit each node once
    for _ in range(num_nodes):
        #choose node with minimum distance
        min_dist = 10e9
        u = -1
        for idx,val in enumerate(distances):
            if val < min_dist and not visited[idx]:
                min_dist = val
                u = idx

        #update distances from chosen node
        for route in routes:
            if route[0] == u and min_dist + route[2] < distances[route[1]]:
                distances[route[1]] = min_dist + route[2]

        #set chosen node to visited
        visited[u] = True

    return distances
