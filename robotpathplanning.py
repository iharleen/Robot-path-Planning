#Name- Harleen Kaur
#Roll no.- 1025230010
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import heapq


# Function to calculate Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* algorithm
def astar(grid, start, goal):

    open_list = []
    heapq.heappush(open_list, (0, start))

    visited = set()
    parent = {}

    g = {start: 0}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while open_list:

        f, current = heapq.heappop(open_list)

        if current in visited:
            continue

        if current == goal:

            path = []
            while current != start:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path

        visited.add(current)

        for dr, dc in directions:

            r = current[0] + dr
            c = current[1] + dc

            # Check boundaries and obstacles
            if (0 <= r < grid.shape[0] and
                0 <= c < grid.shape[1] and
                grid[r][c] == 0):

                neighbor = (r, c)

                if neighbor in visited:
                    continue

                new_g = g[current] + 1

                if new_g < g.get(neighbor, float('inf')):

                    g[neighbor] = new_g
                    parent[neighbor] = current

                    h = heuristic(neighbor, goal)
                    f = new_g + h

                    heapq.heappush(open_list, (f, neighbor))

    return None


# Function to display and visualize grid
def display_grid(grid, path, start, goal):

    final_grid = grid.copy()

    if path:
        for r, c in path:
            if (r, c) != start and (r, c) != goal:
                final_grid[r][c] = 2

    print("\nFinal Grid:")
    print(pd.DataFrame(final_grid))

    # Create grid visualization
    image = np.ones((grid.shape[0], grid.shape[1], 3))

    image[grid == 1] = [0, 0, 0]

    plt.figure(figsize=(7, 7))
    plt.imshow(image, origin='upper')

    # Draw path
    if path:
        x = [p[1] for p in path]
        y = [p[0] for p in path]

        plt.plot(x, y, 'ro-', label='Robot Path')

    # Start and destination
    plt.scatter(start[1], start[0], color='green',
                s=150, label='Start')

    plt.scatter(goal[1], goal[0], color='blue',
                s=150, label='Destination')

    plt.xticks(range(grid.shape[1]))
    plt.yticks(range(grid.shape[0]))

    plt.grid(True)
    plt.title("Robot Path Planning using A*")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.legend()
    plt.show()


# Main program
while True:

    print("\n===== ROBOT PATH PLANNING =====")

    # Input grid size
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    grid = np.zeros((rows, cols), dtype=int)

    # Input obstacles
    n = int(input("Enter number of obstacles: "))

    print("Enter obstacle positions (row column):")

    for i in range(n):

        r, c = map(int, input().split())

        if 0 <= r < rows and 0 <= c < cols:
            grid[r][c] = 1
        else:
            print("Invalid position. Try again.")
            continue

    # Display initial grid
    print("\nInitial Grid:")
    print(pd.DataFrame(grid))

    # Input start and destination
    start = tuple(map(int, input("Enter start position (row column): ").split()))

    goal = tuple(map(int, input("Enter destination (row column): ").split()))

    # Validate positions
    if (len(start) != 2 or len(goal) != 2 or
        not (0 <= start[0] < rows and 0 <= start[1] < cols) or
        not (0 <= goal[0] < rows and 0 <= goal[1] < cols) or
        start == goal or grid[start] == 1 or grid[goal] == 1):

        print("Invalid start or destination position.")
        continue

    # Find shortest path
    path = astar(grid, start, goal)

    if path:

        print("\nShortest Path:")
        print(path)

        print("Total Path Cost:", len(path) - 1)

    else:

        print("\nNo valid path found!")

    # Display final grid and visualization
    display_grid(grid, path, start, goal)

    # Retry option
    choice = input("\nDo you want to try again? (yes/no): ").lower()

    if choice != 'yes':
        print("Thank you for using Robot Path Planning!")
        break
