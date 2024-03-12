import unittest
from power_calculator import PowerCalculator


class TestPowerCalculator(unittest.TestCase):
    def test_calculate_remaining_power(self):
        # Test case 1: No movement
        source = ['2', '1', 'N']
        destination = ['2', '1']
        expected_power = 200  # No cost as there's no movement
        result = PowerCalculator.calculate_remaining_power(source, destination)
        self.assertEqual(result, expected_power)

        # Test case 2: Movement with turns and distance
        source = ['2', '1', 'N']
        destination = ['3', '3']
        expected_power = 165  # Calculation based on expected turn and move costs
        result = PowerCalculator.calculate_remaining_power(source, destination)
        self.assertEqual(result, expected_power)


if __name__ == '__main__':
    unittest.main()
