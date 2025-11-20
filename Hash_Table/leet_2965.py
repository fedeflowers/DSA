class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        possibilities = set([i for i in range(1, n*n +1)])
        elements = defaultdict(int)
        a = 0

        for i in range(n):
            for j in range(n):
                elements[grid[i][j]] += 1
                if grid[i][j] in possibilities:
                    possibilities.remove(grid[i][j])
                if elements[grid[i][j]] >= 2:
                    a = grid[i][j]


        return [a, next(iter(possibilities))]
