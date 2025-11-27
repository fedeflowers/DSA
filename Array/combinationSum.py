"""
```markdown
## Explanation of the "Combination Sum" Solution

### 1. Brief Explanation of the Approach
The solution to the "Combination Sum" problem uses a Depth First Search (DFS) approach to explore all possible combinations of the candidate numbers that can sum up to a given target. The algorithm operates as follows:

- **Parameters**: The `combinationSum` method takes two parameters: `candidates` (a list of integers) and `target` (the target sum we want to achieve).
- **Result Storage**: A list `res` is initialized to store the valid combinations.
- **DFS Function**: The `dfs` function is defined to perform the recursive search. It takes three parameters:
  - `index`: The current index in the `candidates` list.
  - `comb`: The current combination being constructed.
  - `s`: The current sum of the `comb`.

The `dfs` function uses the following logic:
- If the current sum `s` exceeds the target, it terminates that branch of exploration.
- If the `index` exceeds the length of the candidates list, it also terminates that path.
- If the current sum `s` is equal to the target, the valid `comb` is added to the results.
- Two recursive calls are made:
  1. Including the current candidate in the combination (i.e., keeping the same index).
  2. Excluding the current candidate and moving to the next index.

The DFS starts with an empty combination and a sum of zero. The function ultimately returns all the combinations found that add up to the target.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The time complexity is difficult to precisely quantify since it can vary significantly based on the input. In general, we can approximate it as `O(2^N)` where `N` is the number of candidates, as each candidate can either be included or excluded in the combination. However, this can be reduced significantly depending on how the candidates and target are structured.
  
- **Space Complexity**: The space complexity is `O(N)` due to the depth of the recursion stack and the storage of potentially valid combinations in the result list. In the worst case, all candidates yield a valid combination, leading to exponential space usage due to deep recursion.

### 3. Why This Approach is Efficient
This approach is efficient because:
- It systematically explores all potential combinations through recursion, allowing for backtracking once a branch exceeds the target or runs out of candidates.
- The use of a helper function (`dfs`) helps maintain clarity in the code while managing state (current index, current combination, and cumulative sum).
- It avoids duplicate computations by not changing the index when the same candidate is included multiple times (unlike situations where combinations need to be distinct).
- The base cases within the recursion efficiently cut off unnecessary exploratory paths that exceed the target or lack available candidates.

Overall, the DFS approach is a suitable technique for problems involving combinations and subset summations, balancing clarity, systematic exploration, and the handling of constraints effectively.
```

Runtime: undefined
Memory: 17808000
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, comb, s):
            if s > target:
                return
            if index >= len(candidates):
                return
            if s == target:
                res.append(comb)
                return
            
            dfs(index, comb + [candidates[index]], s + candidates[index])
            dfs(index + 1, comb, s)

        dfs(0, [], 0)
        return res

