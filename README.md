# Robot Path Planning Application

## Project Overview
This project is a Python-based Robot Path Planning Application that helps a robot find the shortest path from a starting point to a destination in a grid while avoiding obstacles.

It uses the **A* (A-Star) Pathfinding Algorithm** to calculate the shortest path and Matplotlib to visualize the robot's movement.

## Features
- Create a grid using NumPy.
- Enter grid size and obstacle positions.
- Set the robot's starting point and destination.
- Find the shortest path using the A* algorithm.
- Use Manhattan distance as the heuristic.
- Display grid data using Pandas.
- Visualize the path using Matplotlib.
- Display a message if no valid path is found.
- Retry with a different grid without restarting the program.

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Heapq
- A* Pathfinding Algorithm

## Installation

```bash
pip install numpy pandas matplotlib
```

## How to Run

1. Clone or download this repository.
2. Open the project folder.
3. Run the Python file:

```bash
python robot_path_planning.py
```

4. Enter the number of rows and columns.
5. Enter the number and positions of obstacles.
6. Enter the starting point and destination.
7. The program will calculate and display the shortest path.

## Grid Representation

| Value | Meaning |
|---|---|
| 0 | Free Space |
| 1 | Obstacle |
| 2 | Robot Path |

## Visualization

- **Black:** Obstacles
- **Red:** Robot's path
- **Green:** Starting point
- **Blue:** Destination
- **White:** Free space

## A* Algorithm

The A* algorithm uses the following formula:

**f(n) = g(n) + h(n)**

- **g(n):** Actual distance travelled from the starting point.
- **h(n):** Estimated distance to the destination using Manhattan distance.
- **f(n):** Total estimated cost.

The algorithm explores the grid and finds the shortest available path while avoiding obstacles.

## Project Type
Academic Mini Project

## Author
**Harleen Kaur**
