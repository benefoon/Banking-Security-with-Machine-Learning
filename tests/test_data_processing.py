import unittest
from src.data_processing import clean_data

class TestDataProcessing(unittest.TestCase):
    def test_clean_data(self):
        data = clean_data("tests/sample_transactions.csv")
        self.assertFalse(data.isnull().values.any())

if __name__ == "__main__":
    unittest.main()
