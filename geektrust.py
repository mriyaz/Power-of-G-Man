import sys
from file_parser import InputParser
from power_calculator import PowerCalculator


def main():
    """Main function to execute the program logic.

    Args:
        file_path (str): The path to the input file.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    for source, destination in InputParser.read_input(file_path):
        result = PowerCalculator.calculate_remaining_power(source, destination)
        print(f"{result}")


if __name__ == "__main__":
    main()
