"""
```markdown
## Explanation of the LeetCode Solution for "Number of Adjacent Elements With the Same Color"

### 1. Brief Explanation of the Approach

The problem requires tracking the number of adjacent elements with the same color in a sequence as we process a series of queries. Each query provides an index and a color, indicating that the element at that index should be updated to the new color.

Here’s how the solution works:

- **Initialization**: An array `colors` of size `n` is initialized to hold the current colors of the elements, initially set to `0` (indicating no color). An integer `count` is initialized to keep track of the number of adjacent pairs with the same color, and a list `ans` is initialized to store results after processing each query.

- **Processing Queries**: For each query `(i, c)`:
  - **Check the Current Color**: If the current color at index `i` is not `0` (indicating it has a color), the algorithm checks the adjacent elements (`i - 1` and `i + 1`) to see if they were adjacent to the current color. If they were, `count` is decremented as the adjacency is broken.
  - **Update Color**: The color at index `i` is updated to the new color `c`.
  - **Check New Adjacent**: After updating, the algorithm checks the same adjacent indices again to see if the new color forms new adjacency pairs. If yes, `count` is incremented.
  - After processing each query, the current count is appended to the `ans` list.
  
- **Return Result**: Finally, the `ans` list containing the count after each query is returned.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity is O(Q), where Q is the number of queries. Each query involves a constant amount of work (a few comparisons and assignments), leading to a linear relationship with the number of queries.

- **Space Complexity**: The space complexity is O(N) due to the `colors` array, which holds the color of each index for the `n` elements. The `ans` list can also take up to O(Q) space in the worst case, thus making the overall space complexity O(N + Q). 

### 3. Why This Approach is Efficient

This approach efficiently keeps track of the count of adjacent pairs by using a direct manipulation of a `count` variable rather than recalculating it entirely for every query. By only checking the immediate adjacent elements for changes in color, the algorithm optimizes performance, leading to a linear time complexity relative to the number of queries. This prevents the need for nested iterations through the `colors` list, making it well-suited for larger inputs in competitive programming settings.
```

Runtime: undefined
Memory: 48720000
"""

class Solution:
    def colorTheArray(self, n: int, queries: list[list[int]]) -> list[int]:
        colors = [0] * n
        ans = []
        count = 0
        for i, c in queries:
            if colors[i]:
                if i > 0 and colors[i] == colors[i - 1]: count -= 1
                if i < n - 1 and colors[i] == colors[i + 1]: count -= 1
            colors[i] = c
            if i > 0 and colors[i] == colors[i - 1]: count += 1
            if i < n - 1 and colors[i] == colors[i + 1]: count += 1
            ans.append(count)
        return ans
