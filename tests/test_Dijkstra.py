#Unit Tests for Dijkstra Function

from ..Algorithms import Dijkstra

def test_simple_graph():
    routes = [[0,1,1],[0,3,5],[1,2,2],[2,3,1],[3,4,1]]
    result = Dijkstra.Dijkstra(5,routes,0)
    assert result == [0,1,3,4,5]
