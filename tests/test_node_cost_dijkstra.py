"""Unit Tests for NodeCostDijkstra Function"""

from ..algorithms import node_cost_dijkstra

def test_simple_graph_with_costs():
    """Tests that dijkstra algorithm correctly gives distances to nodes 
    in conncected graph of 5 nodes with processing delays at intermediate nodes.
    """
    num_nodes = 3
    delays = [0,1,0]
    routes = [[0,1,1],[1,2,1]]
    source = 0

    result = node_cost_dijkstra.node_cost_dijkstra(num_nodes, delays, routes, source)
    assert result == [0,1,3]
