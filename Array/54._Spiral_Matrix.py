class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        #(0, 0) : 1 ... (0, 2) : 3 , (1,2): 6 ...
        visited = set()
        curr_el = [0, -1]
        res = []
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)] #directions to follow in order
        curr_dir = 0
        while len(visited) < m*n:
            x, y = curr_el
            dir_x, dir_y = D[curr_dir]
            new_x, new_y = x + dir_x, y + dir_y
            if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                res.append(matrix[new_x][new_y])
                curr_el = [new_x, new_y]
                visited.add(tuple(curr_el))
            else:
                curr_dir = (curr_dir + 1) % len(D)

        return res