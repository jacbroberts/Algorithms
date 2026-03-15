"""Unit Tests for Dijkstra Function"""

from ..algorithms import dijkstra

def test_simple_graph():
    """Tests that dijkstra algorithm correctly gives distances to nodes 
    in conncected graph of 5 nodes."""
    routes = [[0,1,1],[0,3,5],[1,2,2],[2,3,1],[3,4,1]]
    result = dijkstra.dijkstra(5,routes,0)
    assert result == [0,1,3,4,5]
