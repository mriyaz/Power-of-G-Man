class PowerCalculator:
    """Performs calculations related to remaining power after movement."""
    INITIAL_POWER = 200
    TURN_COST = 5
    MOVE_COST = 10

    @staticmethod
    def calculate_remaining_power(source, destination):
        """Calculates remaining power after moving from source to destination.

        Args:
            source (list): Source coordinates and direction (e.g., ['2', '1', 'N']).
            destination (list): Destination coordinates (e.g., ['3', '2']).

        Returns:
            int: The remaining power after movement.
        """
        # Parse input
        x1, y1, direction = int(source[0]), int(source[1]), source[2]
        x2, y2 = int(destination[0]), int(destination[1])

        # Calculate positional differences
        dx = x2-x1
        dy = y2-y1

        # calculate moves
        moves = abs(dx) + abs(dy)

        # Direction vectors mapped to 'N', 'E', 'S', 'W'
        direction_vectors = {(0, 1): 'N', (1, 0): 'E',
                             (0, -1): 'S',  (-1, 0): 'W'}

        # Calculate direction vectors for dx and dy
        dx_vector = 0 if dx == 0 else direction_vectors[(dx//abs(dx), 0)]
        dy_vector = 0 if dy == 0 else direction_vectors[(0, dy//abs(dy))]

        # calculate turns
        if dx_vector == 0 and dy_vector == 0:
            turns = 0
        elif direction == dx_vector or direction == dy_vector:
            turns = 1
        else:
            turns = 2

        # calculate cost
        cost = (turns * PowerCalculator.TURN_COST) + \
            (moves * PowerCalculator.MOVE_COST)

        # return remaining power
        return PowerCalculator.INITIAL_POWER - cost
