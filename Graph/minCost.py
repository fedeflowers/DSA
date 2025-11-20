# GRAPH_SHORTEST_PATH

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = [(0,1,1), (0,-1,2), (1,0,3), (-1,0,4)]
        queue = deque([(0,0,0)]) # row, col , path
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        while queue:
            r, c, path = queue.popleft()
            if (r,c) == (rows-1, cols-1):
                return path
            if (r,c) in visited:
                continue
            visited.add((r,c))

            for x,y,d in directions:
                if 0 <= x + r < rows and 0 <= y + c < cols and (r+x, c+y):
                    if d == grid[r][c]:
                        queue.appendleft((r+x, c+y, path))
                    else:
                        queue.append((r+x, c+y, path + 1))