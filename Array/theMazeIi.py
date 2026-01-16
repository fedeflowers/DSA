"""
## Explanation of the LeetCode Solution for "The Maze II"

### 1. Brief Explanation of the Approach

The provided solution for the "The Maze II" problem uses Dijkstra's algorithm to find the shortest distance from a starting point to a destination in a maze represented by a 2D grid. The maze consists of open paths (represented by 0) and walls (represented by 1). The main objective is to roll through the maze until hitting a wall, and the algorithm tracks the shortest distance required to reach the destination.

**Key Steps in the Implementation:**

- **Initialization:**
  - The number of rows and columns in the maze is calculated.
  - A priority queue (min-heap) is initialized to explore paths based on distances. It starts with the starting point, initialized to a distance of 0.
  - A dictionary named `distances` keeps track of the minimum distance to reach each cell from the start.

- **Main Loop:**
  - While there are elements in the priority queue, the algorithm pops the element with the smallest distance.
  - If the current position matches the destination, the function returns the current distance as it guarantees the shortest path has been found.
  - If the popped distance is greater than the previously recorded shortest distance, it is skipped.
  
- **Rolling in Four Directions:**
  - For each direction (up, down, left, right), the algorithm rolls until it hits a wall, counting the distance rolled.
  - If the distance to the new position (`nx`, `ny`) is less than any previously recorded distance, it updates the distance and adds this new position to the priority queue.

- **Completion:**
  - If the destination is unreachable, the function returns -1.

### 2. Time and Space Complexity Analysis

**Time Complexity:**
- In the worst case, the algorithm explores all cells in the maze. Each cell can potentially be processed multiple times depending on the direction it is rolled. Hence, the time complexity can be approximated to O(N log N), where N is the number of cells. Each cell can be inserted and removed from the priority queue once.

**Space Complexity:**
- The space complexity mainly arises from the storage used for:
  - The priority queue, which can grow to store all N cells.
  - The `distances` dictionary, which also stores a value for every cell in the maze. Thus the space complexity is O(N).

### 3. Why This Approach is Efficient

This approach is efficient due to the following reasons:

- **Dijkstra’s Algorithm:** It is well-suited for finding the shortest paths in weighted graphs, where each move can be seen as moving through edges with weights (the distance traveled).
  
- **Using Priority Queue:** The priority queue ensures that the cell with the smallest distance is always processed first, allowing the algorithm to find the shortest path without exhaustively checking every possible route.

- **Rolling Mechanism:** By rolling as far as possible in each of the four directions until a wall is reached, the algorithm effectively reduces the number of unnecessary checks. It prioritizes direct paths, which minimizes the number of states that need to be explored.

Overall, this solution leverages a well-known graph traversal technique, ensuring it can efficiently navigate the maze to find the shortest route while managing the complexities of direction and wall boundaries.

Runtime: undefined
Memory: 21044000
"""

import heapq

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        # Priority Queue stores: (distance, row, col)
        pq = [(0, start[0], start[1])]
        # Track minimum distance to each cell
        distances = { (row, col): float('inf') for row in range(rows) for col in range(cols) }
        distances[(start[0], start[1])] = 0
        
        while pq:
            d, r, c = heapq.heappop(pq)
            
            # If we reached the destination, return the distance (guaranteed min by Dijkstra)
            if [r, c] == destination:
                return d
            
            # If current path is longer than already found shortest path, skip
            if d > distances[(r, c)]:
                continue
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = r, c
                dist = 0
                
                # Roll until wall
                while 0 <= nx + dx < rows and 0 <= ny + dy < cols and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                    dist += 1
                
                new_dist = d + dist
                if new_dist < distances[(nx, ny)]:
                    distances[(nx, ny)] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))
                    
        return -1
