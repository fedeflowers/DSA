"""
## Explanation of the LeetCode Solution for "Generate Parentheses"

### 1. Approach Explanation

The problem of generating valid parentheses combinations involves using a backtracking approach. The goal is to construct all combinations of parentheses pairs by placing open `(` and closed `)` brackets while ensuring that the combination remains valid (i.e., at no point should the number of closed parentheses exceed the number of open parentheses).

Here's a breakdown of the approach:

- **Backtracking Function**: A nested function `backtrack` is defined, which takes the current partial string `path`, a count of open parentheses `open_count`, and a count of closed parentheses `closed_count`.
- **Base Condition**: If the length of `path` reaches `2 * n`, it means a valid combination of parentheses has been formed because there are `n` pairs (each pair consists of an open and a close).
- **Adding Open Parentheses**: If the count of open parentheses used is less than `n`, it is possible to add an open parenthesis. The function appends `(` to `path`, increments `open_count`, and makes a recursive call. After returning, we remove the last added parenthesis (backtracking).
- **Adding Closed Parentheses**: If the count of closed parentheses is less than the number of open ones, a closed parenthesis can be added. Similar to adding an open parenthesis, the function appends `)` to `path`, increments `closed_count`, and makes a recursive call. Again, backtracking is performed afterward.
- **Result Compilation**: Throughout the process, valid combinations are appended to the `res` list, which is returned after the backtracking process completes.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity is O(4^n / √n). This is because generating the combinations requires traversing a full binary tree of height `2n`, where each level can result in a doubling of combinations until the required number is reached.
  
- **Space Complexity**: The space complexity is O(n) for the recursion stack and the storage of valid combinations. The recursion stack can go as deep as `2n`, and the result list can potentially store up to O(4^n / √n) combinations of parentheses.

### 3. Why This Approach is Efficient

This backtracking technique is efficient for the following reasons:

- **Pruning**: The conditions within the backtrack function effectively prune the search space. For example, the checks to add a closed parenthesis only occur if `closed_count` is less than `open_count`, preventing the formation of invalid combinations.
  
- **Direct Construction**: The method constructs valid strings directly without generating all possible strings first. This direct construction avoids unnecessary overhead and reduces the number of recursive calls.
  
- **Systematic Exploration**: The systematic approach of exploring all potential combinations while maintaining constraints ensures that all valid combinations are captured without redundancy.

Overall, backtracking provides a structured and efficient means of exploring and generating valid parentheses combinations, making it ideal for this specific problem.

Runtime: undefined
Memory: 19340000
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
