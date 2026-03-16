"""
```markdown
# Explanation of the LeetCode Solution for "Maximum Product of Splitted Binary Tree"

## 1. Approach Explanation

The solution to the problem "Maximum Product of Splitted Binary Tree" involves splitting the given binary tree into two subtrees and calculating the maximum product of their sums. The approach employs a recursive function to traverse the binary tree and calculate the sums of all subtrees.

Here's a breakdown of the approach:

- Define a list `sums` that stores the sums of all the subtree values in the binary tree.
  
- Implement a recursive helper function `get_sum(node)` that:
  - Returns 0 if the node is `None` (base case).
  - Recursively calculates the sum of the subtree rooted at the current node by adding its value to the sums of its left and right children.
  - Appends the calculated sum to the `sums` list and returns the sum.

- Call the `get_sum` function starting from the root node to populate the `sums` list and get the total sum of the entire tree.

- Iterate through the `sums` list. For each captured subtree sum `s`, calculate the product of the sum of that subtree and the remaining tree (i.e., `s * (total_sum - s)`), keeping track of the maximum product found.

- Finally, return the maximum product obtained, ensuring the result is modulo \(10^9 + 7\) to avoid overflow.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: \(O(N)\)
  - Each node in the binary tree is visited once to compute its subtree sum, resulting in a linear time complexity where \(N\) is the number of nodes in the tree.

- **Space Complexity**: \(O(N)\)
  - The space complexity arises from storing sums of all the subtrees in the `sums` list. In the worst case, if the tree is skewed, the list could grow to hold sums for all \(N\) nodes. Additionally, the recursive stack may also require \(O(H)\) space, where \(H\) is the height of the tree, but since \(H \leq N\), the overall space complexity remains \(O(N)\).

## 3. Efficiency of the Approach

The proposed approach is efficient due to its linear time complexity, which allows it to handle large binary trees effectively. By traversing each node only once and making use of a simple list to store subtree sums, it avoids redundant calculations and minimizes overhead. 

Moreover, calculating products based on subtree sums only requires a single additional traversal of the `sums` list after the initial sum calculations, making the solution optimal in terms of both time and space. The implementation also accounts for possible large numbers with the modulo operator, thus maintaining efficiency and preventing overflow.
```

Runtime: undefined
Memory: 46296000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []
        
        def get_sum(node):
            if not node:
                return 0
            subtree_sum = node.val + get_sum(node.left) + get_sum(node.right)
            sums.append(subtree_sum)
            return subtree_sum
        
        total_sum = get_sum(root)
        max_prod = 0
        
        for s in sums:
            max_prod = max(max_prod, s * (total_sum - s))
            
        return max_prod % (10**9 + 7)
