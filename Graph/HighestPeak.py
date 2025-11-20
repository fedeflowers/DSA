# Multi-source_BFS__same_principle_of_leet_407

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])

        grid = [[float("inf")] * n for _ in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        queue = deque()
        #add water
        for row in range(m):
            for col in range(n):
                if isWater[row][col]:
                    grid[row][col] = 0
                    queue.append((row, col))
                    visited.add((row, col))
        
        while queue:
            x, y = queue.popleft()
            for d in directions:
                new_x = x + d[0]
                new_y = y + d[1]
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                    grid[new_x][new_y] = grid[x][y] + 1
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))

        return grid
