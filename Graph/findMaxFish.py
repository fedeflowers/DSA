#BFS APPROACH

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        #dfs at starting position
        positions = [(1,0), (0,1), (-1,0), (0,-1)]
        m = len(grid)
        n = len(grid[0])

        def bfs(r,c):
            queue = deque([(r,c)])
            res = grid[r][c]
            grid[r][c] = 0
            while queue:
                x, y = queue.popleft()
                for i,j in positions:
                    new_x = x + i
                    new_y = y + j
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] > 0:
                        res += grid[new_x][new_y] #update res
                        grid[new_x][new_y] = 0 #mark as visited
                        queue.append((new_x, new_y)) #explore neighbours

            return res

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    res = max(res, bfs(i, j))

        return res


#DFS APPROACH


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # Directions for moving up, down, left, right
        positions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            # If the current position is out of bounds or has no fish, return 0
            if grid[x][y] == 0:
                return 0

            # Collect the fish at the current position
            fish = grid[x][y]
            grid[x][y] = 0  # Mark as visited

            # Explore all 4 possible directions
            for i, j in positions:
                if 0 <= i+x < m and 0 <= j+y < n: 
                    fish += dfs(x + i, y + j)

            return fish

        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:  # If there's fish in the cell
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish


