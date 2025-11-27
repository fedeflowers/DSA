"""
## Solution Explanation for "Combination Sum"

### 1. Brief Explanation of the Approach

The given solution employs a Depth-First Search (DFS) strategy to explore all possible combinations of the input numbers (candidates) that can sum up to the specified target. The key components of the approach are as follows:

- **Recursive Function (`dfs`)**: This helper function is responsible for exploring combinations. It takes three parameters:
  - `index`: The current position in the `candidates` list being considered.
  - `comb`: The current combination being formed.
  - `s`: The sum of the current combination.

- **Base Cases**:
  - If the current sum (`s`) exceeds the target, the function returns without taking further action.
  - If the index goes beyond the length of the candidates, the function terminates.
  - If the current sum equals the target, the valid combination is added to the results (`res`).

- **Recursive Calls**:
  - The first recursive call keeps the same index and includes the current candidate in the combination.
  - The second recursive call advances to the next index without including the current candidate.

This exploration continues until all combinations are considered, ultimately leading to the collection of all unique combinations that fulfill the sum requirement.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of this approach can be described as exponential, specifically O(2^N), where N is the number of candidates. In the worst case, you explore every possible subset of candidates, leading to a tree with depth N that branches out maximum at each level due to two choices (include or not include the current candidate).

- **Space Complexity**: The space complexity is O(N), where N represents the depth of the recursion stack. This holds true because the depth can grow to N if all candidates are included in a valid combination. Additionally, the space used for storing the result combinations could contribute to space complexity but is typically not counted separately in analyses as we focus on temporary constructs.

### 3. Why This Approach is Efficient

This approach leverages the recursive exploration of possible combinations, ensuring that all candidates are considered while effectively handling cases where the sum exceeds the target. The pruning of branches (returning early) when the sum exceeds the target contributes significantly to efficiency, as it avoids unnecessary calculations and allows the function to skip over many invalid combinations.

Moreover, the use of a single list (`comb`) for building combinations avoids the overhead of copying entire lists for every combination. Hence, the solution remains clean and focuses on exploring all paths efficiently while discarding unfruitful ones early.

In summary, the DFS approach is efficient for finding all combinations by dividing the problem into manageable subproblems while discarding invalid states quickly.

Runtime: undefined
Memory: 17860000
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

