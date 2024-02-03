import unittest
import time
from c3po.c3po import C3PO

class TestC3PO(unittest.TestCase):
    
    def setUp(self):
        self.millennium_falcon_data = {
            "autonomy": 6, 
            "routes": [
                {"origin": "Tatooine", "destination": "Dagobah", "travelTime": 6},
                {"origin": "Dagobah", "destination": "Endor", "travelTime": 4},
                {"origin": "Dagobah", "destination": "Hoth", "travelTime": 1},
                {"origin": "Hoth", "destination": "Endor", "travelTime": 1},
                {"origin": "Tatooine", "destination": "Hoth", "travelTime": 6}
            ]
        }

    def test_example_1(self):
        
        empire_data = {
            "countdown": 7,
            "bounty_hunters": [
                {"planet": "Hoth", "day": 6},
                {"planet": "Hoth", "day": 7},
                {"planet": "Hoth", "day": 8}
            ]
        }
        # Expected result for Example 1
        expected_odds = 0
        # Create an instance of C3PO and calculate the odds
        c3po = C3PO(self.millennium_falcon_data)
        
        # Assert that the actual odds match the expected odds
        self.assertEqual(actual_odds, expected_odds)

    def test_example_2(self):
        
        empire_data = {
            "countdown": 8,
            "bounty_hunters": [
                {"planet": "Hoth", "day": 6},
                {"planet": "Hoth", "day": 7},
                {"planet": "Hoth", "day": 8}
            ]
        }
        
        expected_odds = 0.81

    def test_example_3(self):
        
        empire_data = {
            "countdown": 9,
            "bounty_hunters": [
                {"planet": "Hoth", "day": 6},
                {"planet": "Hoth", "day": 7},
                {"planet": "Hoth", "day": 8}
            ]
        }
        
        expected_odds = 0.9

    def test_example_4(self):
        
        empire_data = {
            "countdown": 10,
            "bounty_hunters": [
                {"planet": "Hoth", "day": 6},
                {"planet": "Hoth", "day": 7},
                {"planet": "Hoth", "day": 8}
            ]
        }
        
        expected_odds = 1

if __name__ == '__main__':
    unittest.main()
