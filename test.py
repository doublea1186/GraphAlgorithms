import unittest
from collections import deque
from GraphAlgorithms import GraphAlgorithms


class MyTestCase(unittest.TestCase):
    def test_something(self):
        g = GraphAlgorithms(10)
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(0, 4)
        g.addEdge(0, 7)
        g.addEdge(1, 2)
        g.addEdge(2, 0)
        g.addEdge(2, 3)
        g.addEdge(8, 3)
        g.addEdge(9, 4)
        g.addEdge(4, 6)
        g.addEdge(6, 3)
        g.addEdge(2, 9)
        g.addEdge(7, 1)
        g.addEdge(3, 3)
        g.addEdge(1, 2)
        g.addEdge(6, 5)
        g.addEdge(5, 6)
        g.addEdge(9, 2)
        print(g.iterative_bfs())
        print(g.recursive_dfs())

    def test_recursive_iterative(self):
        g = GraphAlgorithms(12)
        print(g.iterative_bfs())
        print(g.recursive_bfs())


if __name__ == '__main__':
    unittest.main()
