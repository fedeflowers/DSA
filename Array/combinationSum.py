"""
## Explanation of the Solution for "Combination Sum"

### 1. Brief Explanation of the Approach

The solution employs a Depth-First Search (DFS) technique to generate all possible combinations of numbers from the `candidates` list that can sum up to the given `target`. Here’s how the approach works:

- **Initialization**: We create an empty list `res` to store the valid combinations.
- **DFS Function**: A helper function named `dfs` is defined, which takes two parameters: `index` (the current position in the `candidates` list) and `comb` (the current combination being explored).
  
    - **Base Case 1**: If the sum of `comb` exceeds the `target`, the function returns, as this path is not valid.
    - **Base Case 2**: If the `index` is equal to or greater than the length of `candidates`, the function exits since there are no more candidates to check.
    - **Base Case 3**: If the sum of `comb` equals the `target`, the combination is added to the result list `res`.
    
- **Recursive Calls**:
    - The first recursive call explores the scenario where we include the current candidate (`candidates[index]`) in the combination (i.e., `comb + [candidates[index]]`).
    - The second recursive call skips the current candidate and moves on to the next candidate by incrementing the `index`.

The DFS begins with an empty combination and from the 0th index of the `candidates`. The function ultimately returns the list of valid combinations stored in `res`.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The worst-case time complexity of this solution is O(2^N), where N is the number of candidates. This is because for each candidate, we have two options: either to include it in the current combination or to exclude it. In practice, the complexity can be less due to the early termination conditions.

- **Space Complexity**: The space complexity is O(N) for the recursion stack in the DFS. In addition to the stack, the result list can grow to hold multiple combinations, but on average, it will be linear with respect to the output size. Hence, the space complexity can be considered O(N + M), where M is the size of the output.

### 3. Why This Approach is Efficient

The efficiency of this approach lies in its ability to prune unnecessary paths (through the conditions) during the exploration of combinations:

- **Early Exit**: The design includes checks for the sum exceeding the target and for reaching the end of the candidates list, which prevents unnecessary computations.
  
- **Combinatorial Nature**: The use of DFS naturally fits the combinatorial nature of the problem where we explore combinations rather than permutations, making the solution concise and intuitive.

- **Reusability of Candidates**: This solution allows the same candidate to be used multiple times, which aligns with the problem's requirements and thus avoids the need for complex logic to manage the usage count.

Overall, this algorithm effectively explores the solution space for combinations while employing a strategy to cut off unproductive pathways, leading to a well-structured and efficient solution.

Runtime: undefined
Memory: 18040000
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

