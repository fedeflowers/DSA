# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
        #i'm checking all positions but it's too slow, i should just check rows
        # #is the board valid
        # def valid(board):
        #     '''
        #     board = nxn board
        #     a board it's valid if the queens do not attack each other
        #     '''
        #     #if there is a queen check row, col and diagonals
        #     for i in range(n):
        #         for j in range(n):
        #             if board[i][j] == 'Q':
        #                 #check row
        #                 for k in range(0, n):
        #                     if k != j:
        #                         if board[i][k] == 'Q':
        #                             return False
        #                 #check col
        #                 for k in range(0, n):
        #                     if i != k:
        #                         if board[k][j] == 'Q':
        #                             return False

        #                 #check diagonals
        #                 diags = [(-1,-1), (1,1), (-1,1), (1, -1)]
        #                 for d in diags:
        #                     temp_i = i
        #                     temp_j = j
        #                     while 0 <= temp_i < n and 0 <= temp_j <n:
        #                         x, y = d
        #                         if temp_i != i and temp_j != j and board[temp_i][temp_j] == 'Q':
        #                             return False
        #                         temp_i -= x
        #                         temp_j -=y
        #     return True 

        # #try all possible combinations until n == 0 and valid
        # base = [['.'] * n for _ in range(n)]
        # res = []
        # def backtrack(queens, board, row):
        #     if queens == 0:
        #         res.append(["".join(r) for r in board])
        #         return

        #     for i in range(row, n):  # row-level pruning
        #         for j in range(n):
        #             board[i][j] = "Q"
        #             if valid(board):
        #                 backtrack(queens - 1, board, i + 1)  # move to next row
        #             board[i][j] = "."  # backtrack

        # backtrack(n, base, 0)
        # return res


class Solution:
    def solveNQueens(self, n):
        # Making use of a helper function to get the
        # solutions in the correct output format
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(row, diagonals, anti_diagonals, cols, state):
            # Base case - N queens have been placed
            if row == n:
                ans.append(create_board(state))
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                # If the queen is not placeable
                if (
                    col in cols
                    or curr_diagonal in diagonals
                    or curr_anti_diagonal in anti_diagonals
                ):
                    continue

                # "Add" the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                state[row][col] = "Q"

                # Move on to the next row with the updated board state
                backtrack(row + 1, diagonals, anti_diagonals, cols, state)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                state[row][col] = "."

        ans = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans