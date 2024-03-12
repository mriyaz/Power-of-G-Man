import unittest
from file_parser import InputParser


class TestInputParser(unittest.TestCase):
    def test_read_input(self):
        # Use a temporary file to simulate reading inputs
        with open('test_input.txt', 'w') as file:
            file.write(
                "2 1 N\n3 2\n\n4 3 E\n5 5\n\n")
        expected_output = [(['2', '1', 'N'], ['3', '2']),
                           (['4', '3', 'E'], ['5', '5'])]
        output = InputParser.read_input('test_input.txt')
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
