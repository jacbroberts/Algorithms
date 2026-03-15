"""
Dijkstra implemeted in python to solve SSSP where each node has a cost
To solve, each node in the  given graph will be converted to two nodes:
1. routes to 2. routes from
inbetween the two created nodes, there will be an edge with the cost of travel
"""
from .dijkstra import dijkstra

def node_cost_dijkstra(num_nodes, delays, routes, source):
    """Returns a list of shortest distance from source to each other node.
    Considers costs at intermediate nodes.
    Assumes that routes all have non negative weights.

    Parameters:
        num_nodes (int): number of nodes in graph
        delays (list): cost of leaving each node.
        routes (list): list of edges in format [from, to, weight]
        source (int): node that distances are counted from.

    Returns:
        list: distance to each originally given node. Distance to source node is always 0.
    """
    for i in range(num_nodes):

        for route in routes:
            if route[0] == i:
                route[0] = i+num_nodes
        if i != source:
            routes.append([i,i+num_nodes,delays[i]])
        else:
            routes.append([i,i+num_nodes,0])


    num_nodes *= 2

    distances = dijkstra(num_nodes, routes, source)

    return distances[0:int(num_nodes/2)]
