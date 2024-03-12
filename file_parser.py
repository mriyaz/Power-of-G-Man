class InputParser:
    """Handles parsing of input files containing source-destination pairs."""
    @staticmethod
    def read_input(file_path):
        """Reads and parses the input file.

        Args:
            file_path (str): Path to the input file.

        Returns:
            list of tuple: Parsed source-destination pairs from the file.
        """
        with open(file_path, 'r') as file:
            inputs = []
            current_input = []

            # Read from the file line by line
            for line in file:
                # strip new line character at the end of line
                clean_line = line.strip()

                # if line is not empty
                if clean_line:
                    # Add it to the current input list
                    current_input.append(clean_line)
                else:
                    # If the line is empty, it signifies the end of an input block
                    # Check if the current input block has exactly 2 lines
                    if len(current_input) == 2:
                        # Append to inputs block
                        inputs.append(
                            (current_input[0].split(), current_input[1].split()))
                        # Reset the current input for the next block
                        current_input = []

            # Check for the last block
            if len(current_input) == 2:
                # Append to inputs block
                inputs.append((current_input[0], current_input[1]))

        return inputs
