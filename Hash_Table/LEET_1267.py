class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])

        
        #sum rows, sum cols
        sum_rows = {}
        sum_cols = {}

        for i in range(m):
            sum_rows[i] = sum(grid[i])
        for j in range(n):
            col = 0
            for i in range(m):
                col += grid[i][j]
            sum_cols[j] = col

        for i in range(m):
            for j in range(n):
                if (sum_rows[i] > 1 or sum_cols[j] > 1 )and grid[i][j]==1:
                    res+=1
                
        return res