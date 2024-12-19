import unittest
from src.graph_analysis import build_graph
import pandas as pd

class TestGraphAnalysis(unittest.TestCase):
    def test_build_graph(self):
        data = pd.DataFrame({
            "sender": ["A", "B", "C"],
            "receiver": ["B", "C", "A"],
            "amount": [100, 200, 300],
            "time": ["2024-01-01", "2024-01-02", "2024-01-03"]
        })
        G = build_graph(data)
        self.assertEqual(len(G.nodes), 3)
        self.assertEqual(len(G.edges), 3)

if __name__ == "__main__":
    unittest.main()
