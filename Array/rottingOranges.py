"""
```markdown
# Explanation of the LeetCode Solution for "Rotting Oranges"

## 1. Approach Explanation
The solution employs a **multi-source Breadth-First Search (BFS)** approach to propagate the "rotting" effect of oranges through the grid. 

1. **Initialization:**
   - The function starts by initializing a queue to track the positions of rotten oranges. It iterates over the grid and adds the coordinates of all initially rotten oranges (represented by the value `2`) to the queue, while also marking them as visited.
   - The variable `max_time` keeps track of the maximum time taken for the oranges to rot.

2. **BFS Process:**
   - While the queue is not empty, the algorithm dequeues an entry, which consists of the coordinates of a rotten orange and the time at which it became rotten.
   - It updates `max_time` with the maximum value between the current time and the existing `max_time`.
   - For each rotten orange, it checks its 4 neighboring cells (right, down, left, up) to see if any adjacent oranges are fresh (`1`). If a fresh orange is found, it is turned into a rotten orange (`2`), and its coordinates along with the increased time are added to the queue.

3. **Final Check:**
   - After BFS completes, the algorithm iterates over the grid a final time to check for any remaining fresh oranges. If any are found, it returns `-1`, indicating it's impossible for all oranges to rot.
   - If all oranges could rot, it returns `max_time`, which represents the time taken for all oranges to rot.

## 2. Time and Space Complexity Analysis
- **Time Complexity:**
  - The worst-case scenario involves visiting all cells in the grid, which means the time complexity is **O(R * C)**, where R is the number of rows and C is the number of columns in the grid.

- **Space Complexity:**
  - The space complexity is determined by the queue and the visited set. In the worst case, all oranges may be rotten or fresh, thus requiring **O(R * C)** space for the queue and visited set.
  
Overall, space complexity is also **O(R * C)**.

## 3. Efficiency of the Approach
The BFS approach is efficient for several reasons:
- **Multi-source Propagation:** Starting from all rotten oranges allows for a simultaneous spreading of the rotting process, minimizing unnecessary checks compared to a single-source approach.
- **Level-wise Exploration:** BFS explores in layers (time increments), ensuring that all oranges that can rot at the same time are processed together, leading to a proper time metric for the result.
- **Avoiding Redundant Work:** By maintaining a set of visited positions, the algorithm avoids re-processing the same orange, saving time and effort.
  
This structured and systematic approach ensures that the function captures the spread of rotting in an optimal way while adhering to a clear order of operations, making it highly efficient for the problem at hand.
```

Runtime: undefined
Memory: 19348000
"""

class Solution:
    # def orangesRotting(self, grid: List[List[int]]) -> int:
    #     #Brute force
    #     #update matrix at each step
    #     time = 0
    #     #if all oranges are rotten retun rime
    #     #if the matrix update is the same as previous, then return -1
    #     R = len(grid)
    #     C = len(grid[0])
    #     D = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    #     while True:
    #         #copy state
    #         new_state = [[0] * C for _ in range(R)]
    #         for i in range(R):
    #             for j in range(C):
    #                 new_state[i][j] = grid[i][j]

    #         for i in range(R):
    #             for j in range(C):
    #                 for x, y in D:
    #                     new_x = i+x
    #                     new_y = j+y
    #                     if grid[i][j] == 2 and 0 <= new_x < R and 0 <= new_y < C:
    #                         if new_state[new_x][new_y] == 1: #becomes rotten
    #                             new_state[new_x][new_y] = 2

    #         if new_state == grid:
    #             #check 1s
    #             for i in range(R):
    #                 for j in range(C):
    #                     if new_state[i][j] == 1:
    #                         return -1
    #             return time
            
    #         grid = new_state

    #         time += 1


    ##optimization
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi-source BFS, in-place
        queue = deque()
        R = len(grid)
        C = len(grid[0])
        D = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited = set()
        #1st level, all rotten oranges
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    queue.append([i, j, 0])
                    visited.add((i,j))

        max_time = 0
        while queue:
            start_x, start_y, time = queue.popleft()
            max_time = max(time, max_time)
            for x, y in D:
                    new_x = start_x + x
                    new_y = start_y + y
                    #only rotten oranges are in queue
                    if 0 <= new_x < R and 0 <= new_y < C and (new_x, new_y) not in visited:
                        if grid[new_x][new_y] == 1: #becomes rotten
                            grid[new_x][new_y] = 2
                            queue.append([new_x, new_y, time+1])
                            visited.add((new_x, new_y))
        #check ones
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return -1

        return max_time
