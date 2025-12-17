"""
```markdown
# Explanation of LeetCode Solution for "Generate Parentheses"

## 1. Brief Explanation of the Approach

The provided solution uses a Depth-First Search (DFS) approach to generate all valid combinations of parentheses for a given integer `n`, which indicates the number of pairs of parentheses. 

- The algorithm employs a recursive function `dfs(path, open, closed)` where:
  - `path` is the current string representation of parentheses being built.
  - `open` is the number of remaining opening parentheses that can be added to `path`.
  - `closed` is the number of remaining closing parentheses that can still be added to `path`.
  
The recursion carries on building the `path` by adding either an opening parenthesis `(` or a closing parenthesis `)` based on the following rules:
- If both `open` and `closed` counts are zero, it means a valid combination of parentheses has been formed, so `path` is added to the results list `self.res`.
- If there are no closing parentheses left (`closed == 0`), the search stops since we cannot add any more valid parentheses.
- If `closed` is less than `open`, it means we cannot add a closing parenthesis yet (to maintain validity), so the search stops as well.
- If there are remaining `open` parentheses, the function recursively calls `dfs` adding an opening parenthesis, and decrements the `open` count.
- If there are remaining `closed` parentheses, the function recursively calls `dfs` adding a closing parenthesis, and decrements the `closed` count.

The initial call to the function `dfs("", n, n)` starts the search with an empty path and `n` pairs available. Finally, the results are returned as `self.res`.

## 2. Time and Space Complexity Analysis

### Time Complexity
The time complexity of this approach is O(4^n / √n). This arises because each time you can either add an open or a close parenthesis, leading to a structure akin to a binary tree with `2n` levels. Since valid combinations prune invalid paths early, it leads to Catalan number scenarios which result in the final complexity.

### Space Complexity
The space complexity is O(n) for the recursion stack, as the depth of the recursion can go up to `n` levels due to the parentheses being added.

## 3. Why This Approach is Efficient

This DFS approach is efficient due to:
- **Early Pruning**: The search space is pruned effectively by regulating how many opening and closing parentheses are available. It avoids the generation of invalid states early, thus limiting unnecessary recursive calls.
- **Backtracking**: This method uses backtracking to explore potential solutions and only maintains the valid paths for further exploration.
- **Catalan Number Generation**: By directly constructing valid combinations, it adheres to the combinatorial nature of valid parentheses, which corresponds to the Catalan numbers, ensuring efficiency in generating the correct results.

Overall, the combined logic of valid state management and early termination leads to a well-optimized solution.
```

Runtime: undefined
Memory: 17832000
"""

class Solution:
    def __init__(self):
        self.res = []
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(path, open, closed):
            if open == closed == 0:
                self.res.append(path)
                return
            if closed == 0:
                return
            if closed < open:
                return
            if open > 0:
                dfs(path + "(", open-1, closed)
            if closed > 0:
                dfs(path + ")", open, closed - 1)

        dfs("", n, n)
        return self.res

            
