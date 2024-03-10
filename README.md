**Project Name** : Power of G-Man

**Table of Contents**

* [Project Overview](#project-overview)
* [Dependencies](#dependencies)
* [Development Setup](#development-setup)
* [Project Structure](#project-structure)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Project Overview
This Project is a backend challenge from https://www.geektrust.com/coding/detailed/power-of-g-man

### Context
-------

G-Man is a video game in which G-Man has to move from one point to another on a grid (6 X 6 grid). There could be multiple paths between a source coordinate and destination coordinate and G-Man needs to reach the destination by spending least amount of power.

### Position
--------

1.  G-Man's position is located by the x, y coordinate of the grid.
2.  One of the four compass points N, E, S and W indicates the direction G-Man is facing. Eg: 2, 1 N means the G-Man is at 2 on the x coordinate, 1 on the y coordinate, and facing North.

### 6 X 6 Grid
----------

![](https://geektrust.sgp1.cdn.digitaloceanspaces.com/assets/v2/problems/power-of-g-man/gman-grid.png)

### Moves
-----

At the start of the game, G-Man is given a power of 200 units. His power is reduced for every move and turn he takes.

1.  G-Man can turn left or right 90 degrees at a time to change his direction.
2.  For every turn G-Man makes, his power is reduced by 5.
3.  For every move that G-Man makes by 1 grid point, his power is reduced by 10.
    -   eg: If G-Man moves from 2, 1 E to the destination 4, 1 he loses 20 power points.
    -   eg: If G-Man moves from 2, 1 S to 4, 5; he has to turn twice and move 6 grid points. So he loses 70 power points.

### Goal
-----

Given the source and destination coordinates, G-Man needs to reach the destination by spending least amount of power. And you need to print the remaining power he has after taking the shortest path with minimum number of turns.

### Tips
-----
1.  - All input commands are to be read from a file, and output is to be printed to the console.
2.  - Build a command line application with the location to the text file as parameter.
3.  - No server, DB, UI or in-memory data store required.
4.  - Avoid using third party libraries/frameworks for implementing core logic.

## Dependencies

This project relies on the following Python libraries:

```
# List your project's dependencies here, one per line
dependency1
dependency2
```

You can install them using pip:

```bash
pip install -r requirements.txt
```

## Development Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<username>/<project-name>.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd <project-name>
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
<project-name>
├── README.md (This file)
├── requirements.txt (List of dependencies)
├── src/
│   ├── __init__.py (Optional: Empty file to indicate a Python package)
│   ├── your_module1.py
│   └── your_module2.py (Add additional modules as needed)
├── tests/
│   ├── test_your_module1.py
│   └── test_your_module2.py (Unit tests for your modules)
└── main.py (Entry point for your backend application)
```

- **src:** Contains the source code for your backend application, organized into modules (optional `__init__.py` for Python packages).
- **tests:** Houses unit tests for your modules to ensure correct functionality (using a testing framework like `unittest` or `pytest`).
- **main.py:** Serves as the entry point for your backend application, typically importing modules from `src` and defining logic for execution.
- **requirements.txt:** Lists all project dependencies for easy installation using `pip install -r requirements.txt`.

## Usage

<-- Provide clear instructions on how to run or use your backend application, including any command-line arguments or configuration options. -->


## Contributing

We welcome contributions to this project! Please follow these guidelines:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and write unit tests to verify them.
4. Submit a pull request with a clear description of your changes.

We'll review your pull request and merge it if it meets our standards.

## License

This project is licensed under the MIT license.
