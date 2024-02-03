import unittest
import time
from c3po.c3po import C3PO

class TestC3PO(unittest.TestCase):
    
    def setUp(self):
        # Common setup for the millennium falcon data
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
        # Setup for Example 1
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
        
        # Start timing
        start_time = time.time()
        actual_odds = c3po.give_me_the_odds(empire_data)
        # End timing
        end_time = time.time()

        # Print the runtime
        print(f"Runtime of test_example_1: {end_time - start_time} seconds")
        # Assert that the actual odds match the expected odds
        self.assertEqual(actual_odds, expected_odds)

    def test_example_2(self):
        # Setup for Example 2
        empire_data = {
            "countdown": 8,
            "bounty_hunters": [
                {"planet": "Hoth", "day": 6},
                {"planet": "Hoth", "day": 7},
                {"planet": "Hoth", "day": 8}
            ]
        }
        # Expected result for Example 2
        expected_odds = 0.81
        # Test code similar to test_example_1

    def test_example_3(self):
        # Setup for Example 3
        empire_data = {
            "countdown": 9,
            "bounty_hunters": [
                {"planet": "Hoth", "day": 6},
                {"planet": "Hoth", "day": 7},
                {"planet": "Hoth", "day": 8}
            ]
        }
        # Expected result for Example 3
        expected_odds = 0.9
        # Test code similar to test_example_1

    def test_example_4(self):
        # Setup for Example 4
        empire_data = {
            "countdown": 10,
            "bounty_hunters": [
                {"planet": "Hoth", "day": 6},
                {"planet": "Hoth", "day": 7},
                {"planet": "Hoth", "day": 8}
            ]
        }
        # Expected result for Example 4
        expected_odds = 1
        # Test code similar to test_example_1

# This allows the tests to be run from the command line
if __name__ == '__main__':
    unittest.main()
