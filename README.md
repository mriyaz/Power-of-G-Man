**Project Name** : Power of G-Man

**Table of Contents**

* [Project Overview](#project-overview)
* [Pre-requisites](#pre-requisites)
* [How to run the code](#how-to-run-the-code)
* [How to execute the unit tests](#how-to-execute-the-unit-tests)



## Project Overview
This Project is a backend challenge from https://www.geektrust.com/coding/detailed/power-of-g-man

### Context

G-Man is a video game in which G-Man has to move from one point to another on a grid (6 X 6 grid). There could be multiple paths between a source coordinate and destination coordinate and G-Man needs to reach the destination by spending least amount of power.

### Position

1.  G-Man's position is located by the x, y coordinate of the grid.
2.  One of the four compass points N, E, S and W indicates the direction G-Man is facing. Eg: 2, 1 N means the G-Man is at 2 on the x coordinate, 1 on the y coordinate, and facing North.

### 6 X 6 Grid

![](https://geektrust.sgp1.cdn.digitaloceanspaces.com/assets/v2/problems/power-of-g-man/gman-grid.png)

### Moves

At the start of the game, G-Man is given a power of 200 units. His power is reduced for every move and turn he takes.

1.  G-Man can turn left or right 90 degrees at a time to change his direction.
2.  For every turn G-Man makes, his power is reduced by 5.
3.  For every move that G-Man makes by 1 grid point, his power is reduced by 10.
    -   eg: If G-Man moves from 2, 1 E to the destination 4, 1 he loses 20 power points.
    -   eg: If G-Man moves from 2, 1 S to 4, 5; he has to turn twice and move 6 grid points. So he loses 70 power points.

### Goal

Given the source and destination coordinates, G-Man needs to reach the destination by spending least amount of power. And you need to print the remaining power he has after taking the shortest path with minimum number of turns.

### Tips

1.  - All input commands are to be read from a file, and output is to be printed to the console.
2.  - Build a command line application with the location to the text file as parameter.
3.  - No server, DB, UI or in-memory data store required.
4.  - Avoid using third party libraries/frameworks for implementing core logic.


## Pre-requisites
* Python 3.8/3.9
* Pip

## How to run the code

Use `run.sh` if you are Linux/Unix/macOS Operating systems and `run.bat` if you are on Windows.  Both the files run the commands silently and prints only output from the input file `sample_input/input1.txt`. You are supposed to add the input commands in the file from the appropriate problem statement. 

Internally both the scripts run the following commands 

 * `pip install -r requirements.txt` - This will install the dependencies mentioned in the requirement.file
 * `python -m geektrust sample_input/input1.txt` - This will run the solution passing in the sample input file as the command line argument

 ## How to execute the unit tests

 `python -m unittest discover` will execute the unit test cases.

 The unit test coverage is found by the command :
`coverage run -m unittest discover`
