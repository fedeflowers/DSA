"""
```markdown
## Explanation of the Combinatorial Solution to "Combination Sum"

### 1. Approach

The provided solution employs a depth-first search (DFS) strategy to explore all possible combinations of numbers from the `candidates` list that sum up to the given `target`. The function `combinationSum` initializes an empty list `res` to store the valid combinations. It then defines an inner function `dfs` that performs the recursive searches.

- **Parameters of `dfs`**:
  - `index`: the current position in the `candidates` list being evaluated.
  - `comb`: the current combination being formed.

**Key Steps in the Algorithm**:
- If the sum of `comb` exceeds the `target`, the function returns early to avoid unnecessary computation.
- If the `index` reaches the length of `candidates`, it returns, indicating no more candidates to consider.
- If the sum of `comb` matches the `target`, the current combination is added to `res`.
- The `dfs` function is called twice:
  - First, it adds the current candidate at index `index` to `comb` and continues searching from the same index (allowing for the possibility of using that candidate again).
  - Second, it skips the current candidate and moves to the next one.

Finally, the outer function returns the list of all valid combinations found.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  The time complexity of this algorithm can be quite high, potentially reaching O(2^T) in the worst-case scenario where T is the `target`. This is because each candidate can either be included in the current combination or not, leading to exponential combinations. However, the practical complexity often differs based on the values in the candidates and the target.

- **Space Complexity**: 
  The space complexity primarily results from the recursion stack and the storage of valid combinations. The recursion stack's maximum depth can be O(T) if the function needs to explore deeply enough to reach the target. Additionally, storing valid combinations in `res` may also require space, which can approximate O(N) where N is the number of valid combinations.

### 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **Backtracking**: The use of recursion allows the program to explore potential combinations systematically. If a combination exceeds the target, it stops exploring that path early (pruning), reducing the number of unnecessary calculations.
- **Combination Reusability**: By allowing the same candidate to be reused (by not incrementing the index in the first DFS call), it supports cases where the same number can be part of the sum multiple times, which is specifically required for this problem.
- **Early Exits**: The checks on the sum of `comb` and the index help avoid wasted computational effort, making the process more efficient.
  
Overall, while a complete exploration of combinations can be computationally intensive, the pruning and systematic searching provided by DFS effectively narrows down feasible solutions, rendering it a suitable approach for solving the "Combination Sum" problem.
```

Runtime: undefined
Memory: 17940000
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, comb):
            if sum(comb) > target:
                return
            if index >= len(candidates):
                return
            if sum(comb) == target:
                res.append(comb)
                return
            
            dfs(index, comb + [candidates[index]])
            dfs(index + 1, comb)

        dfs(0, [])
        return res

