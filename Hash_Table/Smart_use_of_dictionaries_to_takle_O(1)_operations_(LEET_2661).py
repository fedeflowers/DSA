class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        #dic from num to row, col
        nums = {}
        #another dic of row and col sums to determine the first painted?
        #{0 ..m)} for rows and {0...n} for cols
        sums_rows = defaultdict(int)
        sums_cols = defaultdict(int)
        for i in range(m):
            for j in range(n):
                nums[mat[i][j]] = (i,j)
                sums_rows[i] += mat[i][j]
                sums_cols[j] += mat[i][j]


        for i, el in enumerate(arr):
            r, c = nums[el]
            sums_rows[r] -= el
            sums_cols[c] -= el

            if sums_rows[r] == 0 or sums_cols[c] == 0:
                return i
