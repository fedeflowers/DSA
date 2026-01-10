"""
# The Maze Solution Explanation

## 1. Brief Explanation of the Approach

The solution for "The Maze" problem involves using a Breadth-First Search (BFS) algorithm to determine if there is a valid path in a maze from a starting position to a destination position. The maze is represented as a grid, where `0` indicates an open cell and `1` indicates a wall.

### Key Steps:
- **Rolling Mechanism**: The ball "rolls" in a given direction until it hits a wall (i.e., a cell containing `1`). This means that instead of moving one step at a time, the algorithm moves continuously in one direction until it can no longer proceed.
- **Visited Tracking**: To avoid cycles and revisit positions, a set called `visited` keeps track of the cells the ball has already stopped at.
- **Queue for BFS**: A deque (`collections.deque`) is used to facilitate the BFS. The BFS explores all possible directions (up, down, left, right) from the current position in a loop to find the destination.

The algorithm continues until either the destination is found or there are no more positions to explore.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N), where N is the number of cells in the maze. In the worst case, each cell may be visited once, and exploring all possible directions from a single cell takes constant time due to rolling.
  
- **Space Complexity**: O(N) as well, where N is the number of cells. The space is mainly used by the `visited` set and the BFS queue. In the worst case, all cells may be stored in memory if they are reachable.

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:

1. **Reduced Redundant Movements**: By implementing the rolling mechanism, the algorithm eliminates unnecessary back-and-forth movements—jumping directly to the last valid position. This significantly reduces the number of checks and updates made during execution.

2. **BFS Guarantees Shortest Path**: BFS naturally finds the shortest path in an unweighted grid, ensuring that once the destination is reached, it is confirmed as the best solution.

3. **No Cycles**: The use of a visited set prevents cycles and redundant explorations, optimizing the exploration process and avoiding infinite loops.

4. **Simple and Clear Logic**: The algorithm clearly separates the concerns of pathfinding (BFS) and movement mechanics (rolling to walls), which makes the code easier to understand and maintain.

In summary, the BFS with a rolling mechanism effectively explores the maze, efficiently determines pathways, and avoids unnecessary computational overhead.

Runtime: undefined
Memory: 19996000
"""

# class Solution:
#     def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
#         # bfs, evita di tornare da dove sei arrivato, e una funzione che data una direzione mi trova dove sarà la palla andando verso quella direzione
#         # evito pure di mettere quelle pos che hanno start == end
#         def find_next_pos(start, direction):
#             x, y = start
#             if direction == "left":
#                 while y >= 0:
#                     if maze[x][y] == 1:
#                         break
#                     y -= 1
                    
#                 return (x, y+1)
#             elif direction == "right":
#                 while y < len(maze[0]):
#                     if maze[x][y] == 1:
#                         break
#                     y += 1
                    
#                 return (x, y-1)

#             elif direction == "up":
#                 while x >= 0:
#                     if maze[x][y] == 1:
#                         break
#                     x -= 1
                    
#                 return (x+1, y)

#             elif direction == "down":
#                 while x < len(maze):
#                     if maze[x][y] == 1:
#                         break
#                     x += 1
#                 return (x-1, y)

#         q = Deque([(start, None)])
#         opposite = {"left": "right", "right": "left", "up": "down", "down": "up"}
#         visited = set()
#         while q:
#             pos, prev = q.popleft()
#             if tuple(pos) in visited:
#                 continue

#             visited.add(tuple(pos))

#             if pos == tuple(destination):
#                 return True
#             if not prev:
#                 for d in ("down", "left", "up", "right"):
#                     q.append((find_next_pos(pos, d), d))
#             else:
#                 for d in ("down", "left", "up", "right"):
#                     if d != prev and opposite[d] != prev:
#                         q.append((find_next_pos(pos, d), d))

#         return False

from collections import deque
from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols = len(maze), len(maze[0])
        start_tuple = tuple(start)
        dest_tuple = tuple(destination)
        
        # Use a set to keep track of stopped positions to avoid cycles
        visited = {start_tuple}
        q = deque([start_tuple])
        
        while q:
            curr = q.popleft()
            if curr == dest_tuple:
                return True
            
            # Try all 4 directions from the current stopped position
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = curr
                
                # Roll the ball until it hits a wall
                while 0 <= x + dx < rows and 0 <= y + dy < cols and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                
                new_pos = (x, y)
                
                # Only add to queue if we haven't stopped at this position before
                if new_pos not in visited:
                    visited.add(new_pos)
                    q.append(new_pos)
                    
        return False
