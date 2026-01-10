"""
# Explanation of LeetCode Solution for "The Maze"

## 1. Approach

The solution uses a breadth-first search (BFS) strategy to determine if there is a path from a starting point to a destination in the maze, which is represented by a 2D grid where `0` indicates an empty space and `1` indicates a wall. The BFS explores possible paths by rolling the ball in four directions until it hits a wall. The key steps in the code are:

- **Find Next Position**: The function `find_next_pos` is defined to determine the next valid position the ball can reach in a specific direction without hitting a wall. It keeps moving in the given direction until it encounters a `1` (a wall).
  
- **Queue Initialization**: The BFS utilizes a queue (deque) to explore all positions that can be reached by rolling the ball, starting from the `start` position.

- **Visited Set**: A set is used to keep track of already visited positions, ensuring that the same position is not revisited, which would create loops.

- **Direction Handling**: The BFS iterates through each direction. If it is not the previous direction taken, it pushes potential new positions into the queue for further exploration.

- **Destination Check**: If the current position matches the destination, the function returns `True`. If the queue is exhausted without finding the destination, it returns `False`.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N * M), where N is the number of rows and M is the number of columns in the maze. In the worst case, each cell might be processed once, and since the ball can roll without obstruction until it hits a wall or the edge of the maze, it might check multiple positions in each direction.

- **Space Complexity**: O(N * M) as well for the `visited` set and the queue in the BFS. In the worst-case scenario, all positions in the maze could be stored in memory.

## 3. Efficiency of the Approach

This approach is efficient because:

- **Immediate Exploration**: Rolling the ball directly to the farthest reachable position in each direction without obstructing walls minimizes unnecessary checks and iterations.

- **Avoiding Cycles**: By maintaining a set of visited positions, the solution avoids revisiting cells, which prevents infinite loops and redundant calculations.

- **BFS Nature**: BFS systematically explores all potential paths at a particular distance from the starting point before moving further. This ensures the shortest path is found if it exists.

- **Direction Constraints**: By considering the last direction taken and avoiding revisiting it immediately (ensuring the ball rolls in a new direction), the algorithm helps to prune unnecessary paths early on, improving efficiency. 

Overall, these elements combine to create an effective and optimal solution for finding a path in the maze.

Runtime: undefined
Memory: 20080000
"""

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # bfs, evita di tornare da dove sei arrivato, e una funzione che data una direzione mi trova dove sarà la palla andando verso quella direzione
        # evito pure di mettere quelle pos che hanno start == end
        def find_next_pos(start, direction):
            x, y = start
            if direction == "left":
                while y >= 0:
                    if maze[x][y] == 1:
                        break
                    y -= 1
                    
                return (x, y+1)
            elif direction == "right":
                while y < len(maze[0]):
                    if maze[x][y] == 1:
                        break
                    y += 1
                    
                return (x, y-1)

            elif direction == "up":
                while x >= 0:
                    if maze[x][y] == 1:
                        break
                    x -= 1
                    
                return (x+1, y)

            elif direction == "down":
                while x < len(maze):
                    if maze[x][y] == 1:
                        break
                    x += 1
                return (x-1, y)

        q = Deque([(start, None)])
        opposite = {"left": "right", "right": "left", "up": "down", "down": "up"}
        visited = set()
        while q:
            pos, prev = q.popleft()
            if tuple(pos) in visited:
                continue

            visited.add(tuple(pos))

            if pos == tuple(destination):
                return True
            if not prev:
                for d in ("down", "left", "up", "right"):
                    q.append((find_next_pos(pos, d), d))
            else:
                for d in ("down", "left", "up", "right"):
                    if d != prev and opposite[d] != prev:
                        q.append((find_next_pos(pos, d), d))

        return False


