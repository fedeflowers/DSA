"""
```markdown
# Explanation of the LeetCode Solution for "Create Binary Tree From Descriptions"

## 1. Approach Explanation

This solution constructs a binary tree from a list of descriptions, where each description indicates the parent-child relationship between nodes and whether the child is a left or right child. 

- **Data Structures Used**:
  - A dictionary named `reference` to map node values to their corresponding `TreeNode` objects.
  - A set called `roots` to track potential root nodes.

- **Process**:
  - For each description in `descriptions`, which is comprised of a parent node, a child node, and a boolean determining if the child is a left child:
    1. Check if the parent node is already in the `reference` dictionary. If not, create a new `TreeNode` and add it to the dictionary and the `roots` set.
    2. Check if the child node is in the `reference` dictionary, and if not, create a new `TreeNode` for the child.
    3. Set the corresponding left or right child of the parent based on the `is_left` value.
    4. If the child node is present in the `roots` set, remove it from the set because it cannot be a root (it has a parent).

- **Final Output**: At the end, the node remaining in the `roots` set is the root of the constructed binary tree, and the method returns that node.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N)
  - The algorithm processes each description once, leading to a linear traversal through the list. Here, N represents the number of descriptions.

- **Space Complexity**: O(N)
  - The solution maintains a dictionary of `TreeNode` objects and a set of root candidates, both of which can grow up to N in size in the worst case.

## 3. Why This Approach is Efficient

- **Direct Mapping**: By using a dictionary to map values to `TreeNode` objects, the solution ensures that access to nodes is done in constant time, leading to efficient updates and checks throughout the processing of the descriptions.
  
- **Tracking Roots**: The use of a set to track root candidates allows for quick removals when a child is assigned, making sure the final output correctly identifies the true root of the tree.

- **Simplicity**: The approach is simple and straightforward, directly leveraging the relationships defined in the input, which minimizes overhead and keeps the code easy to understand and maintain.
```


Runtime: undefined
Memory: 26896000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        reference = {}
        roots = set()
        for parent, child, is_left in descriptions:
            if parent not in reference:
                reference[parent] = TreeNode(parent)
                roots.add(parent)
            if child not in reference:
                reference[child] = TreeNode(child)
            if is_left:
                reference[parent].left = reference[child]
            else:
                reference[parent].right = reference[child]

            if child in roots:
                roots.remove(child)
        return reference[list(roots)[0]]

