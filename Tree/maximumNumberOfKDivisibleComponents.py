"""
```markdown
## Explanation of the Solution for "Maximum Number of K-Divisible Components"

### 1. Approach Explanation
The problem "Maximum Number of K-Divisible Components" involves determining the number of connected components in a tree structure (represented by nodes and edges) where the sum of the values in those components is divisible by a given integer \( k \).

The solution uses Depth-First Search (DFS) to traverse the tree. Here's a step-by-step breakdown:

- **Adjacency List Construction:** We create an adjacency list to represent the tree structure from the edges provided. This allows for easy traversal of the graph.

- **DFS Traversal:** The algorithm uses a recursive DFS function:
  - Each node starts with its own value.
  - As the DFS explores the tree, it aggregates the values of its children.
  - After processing all children, it checks if the total sum of the node's value and its children's values is divisible by \( k \). If it is, this indicates a valid k-divisible component, so we increment the `components` counter.
  
- **Returning Values:** If the total sum is divisible by \( k \), we return 0 to signify a "cut" at this node, indicating that the parent's running total shouldn't include this sum. Otherwise, the function returns the total sum up to that point to be included in the parent's computation.

### 2. Time and Space Complexity Analysis
- **Time Complexity:** 
  - The DFS function visits each node exactly once, and each edge is also traversed once. Thus, the time complexity can be expressed as \( O(N) \), where \( N \) is the number of nodes in the tree.

- **Space Complexity:**
  - The space complexity is determined by the storage used for the adjacency list and the recursive call stack of DFS. The adjacency list uses \( O(N) \) space and the call stack in the worst case also requires \( O(N) \) space, leading to an overall space complexity of \( O(N) \).

### 3. Efficiency of the Approach
This approach is efficient for several reasons:
- **Single Traversal:** The use of DFS allows for a single traversal of the tree to both build the graph and compute the sums, making the algorithm straightforward and efficient.
- **Early Stopping on Divisibility:** By returning a sum of 0 when a component is found to be k-divisible, the algorithm prevents unnecessary computations and avoids redundant checks in subsequent parts of the tree, focusing only on relevant information.
- **Simplicity and Directness:** The structure of the adjacency list combined with a clear and direct DFS implementation results in a solution that is easy to understand and maintain while being performant.

Overall, this solution leverages the properties of trees and modular arithmetic efficiently, making it suitable for the problem at hand.
```

Runtime: undefined
Memory: 40952000
"""

from collections import defaultdict
from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # 1. Build Adjacency List
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.components = 0

        # 2. Bottom-Up DFS
        def dfs(curr, parent):
            # Start with the node's own value
            total_sum = values[curr]

            # Aggregate values from children
            for child in adj[curr]:
                if child != parent:
                    total_sum += dfs(child, curr)

            # 3. Check divisibility
            if total_sum % k == 0:
                self.components += 1
                return 0  # Edge cut: return 0 to parent so this sum isn't counted twice
            
            return total_sum  # Pass remainder up

        dfs(0, -1)
        return self.components
