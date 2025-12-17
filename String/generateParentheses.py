"""
# Explanation of the LeetCode Solution for "Generate Parentheses"

## 1. Approach Explanation
The solution to the "Generate Parentheses" problem uses a recursive backtracking technique to generate all combinations of well-formed parentheses.

- **Function `generateParenthesis`**: This is the main function that initializes an empty list `res` to store the valid combinations and calls the helper function `backtrack` with an empty path and counts for opened and closed parentheses.

- **Function `backtrack`**: This function is responsible for building the combinations recursively:
  - **Base Case**: When the length of the current combination `path` is equal to `2 * n` (meaning we have used all parentheses), the current combination is valid and added to the `res` list.
  - **Adding Open Parentheses**: If the count of open parentheses (`open_count`) is less than `n`, it adds an opening parenthesis `(` to the path and recursively calls `backtrack`.
  - **Adding Closed Parentheses**: If the count of closed parentheses (`closed_count`) is less than the count of open ones, it adds a closing parenthesis `)` to the path and recursively calls `backtrack`.
  - **Backtracking**: After exploring both possibilities (adding an open or a closed parenthesis), it backtracks by removing the last parenthesis added to explore other combinations.

This recursive strategy effectively explores all potential configurations by ensuring that the parentheses remain balanced.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: The time complexity is O(4^n / sqrt(n)), which represents the number of valid combinations of parentheses pairs. This derives from the fact that for every pair of parentheses added, two choices are available (either adding an open or a close). The maximum depth of recursion can lead to a branching factor that grows exponentially.
  
- **Space Complexity**: The space complexity is O(n) due to the recursion stack and the temporary storage of the current combination in `path`. Additionally, the result storage `res` will also hold all the valid combinations, contributing to space usage. However, since the output size can also be considered, the overall space complexity can also depend on the number of output combinations generated.

## 3. Why This Approach is Efficient
The backtracking approach is efficient for generating combinations of parentheses for several reasons:
- **Pruning**: The algorithm avoids unnecessary paths early by checking the number of open and closed parentheses. If the number of closed parentheses exceeds the number of open ones or if they exceed `n`, those paths are abandoned early, reducing the search space.
- **Balanced Combinations**: By enforcing rules on how many of each type of parenthesis can be added, this solution guarantees that only valid combinations are generated. This means that most invalid combinations are never constructed or stored.
- **Recursion**: Backtracking leverages the call stack to manage the state of the current combination, making it easy to explore and then retract decisions, which naturally fits the problem's requirements.

This structured exploration coupled with early stopping conditions makes the solution both effective and efficient for the problem of generating well-formed parentheses combinations.

Runtime: undefined
Memory: 18120000
"""

# class Solution:
#     def __init__(self):
#         self.res = []
#     def generateParenthesis(self, n: int) -> List[str]:
#         def dfs(path, open, closed):
#             if open == closed == 0:
#                 self.res.append(path)
#                 return
#             if closed == 0:
#                 return
#             if closed < open:
#                 return
#             if open > 0:
#                 dfs(path + "(", open-1, closed)
#             if closed > 0:
#                 dfs(path + ")", open, closed - 1)

#         dfs("", n, n)
#         return self.res

            

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(path, open_count, closed_count):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            
            if open_count < n:
                path.append("(")
                backtrack(path, open_count + 1, closed_count)
                path.pop() # backtrack
                
            if closed_count < open_count:
                path.append(")")
                backtrack(path, open_count, closed_count + 1)
                path.pop() # backtrack

        backtrack([], 0, 0)
        return res
