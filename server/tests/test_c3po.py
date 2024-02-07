import unittest
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
        expected_odds = 0
        c3po = C3PO(self.millennium_falcon_data)
        actual_odds = c3po.calculateOdds(empire_data)
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
        c3po = C3PO(self.millennium_falcon_data)
        actual_odds = c3po.calculateOdds(empire_data)
        self.assertEqual(actual_odds, expected_odds)

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
        c3po = C3PO(self.millennium_falcon_data)
        actual_odds = c3po.calculateOdds(empire_data)
        self.assertEqual(actual_odds, expected_odds)

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
        c3po = C3PO(self.millennium_falcon_data)
        actual_odds = c3po.calculateOdds(empire_data)
        self.assertEqual(actual_odds, expected_odds)

if __name__ == '__main__':
    unittest.main()
