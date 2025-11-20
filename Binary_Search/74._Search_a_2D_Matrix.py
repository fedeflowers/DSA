class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #search by col and then search by row or else map index to row = index//n and col = index%n
        #bin search on rows:
        R = len(matrix)
        C = len(matrix[0])

        def _find_row():
            s = 0
            e = R-1

            while s <= e:
                mid = (s+e)//2
                if  matrix[mid][0] <= target <= matrix[mid][C-1]:
                    return mid

                elif matrix[mid][0] > target:
                    e = mid-1
                else:
                    s = mid+1
            return -1

        
        def _find_num(row):
            s = 0
            e = C-1

            while s <= e:
                mid = (s+e)//2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    e = mid -1
                else:
                    s = mid +1

            return False
        
        row = _find_row()
        if row == -1:
            return False
        return _find_num(row)