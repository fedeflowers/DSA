"""
```markdown
# Explanation of LeetCode Solution for "Create Binary Tree From Descriptions"

## 1. Brief Explanation of the Approach

The problem requires us to construct a binary tree given a list of descriptions that outline the parent-child relationships within the tree. Each description consists of three values: a parent node's value, a child node's value, and a boolean indicating whether the child is the left or right child of the parent.

The solution proceeds with the following steps:

- **Node Creation:** We maintain a dictionary called `nodes` to map each node's value to its corresponding `TreeNode` object. We also utilize a set called `children` to keep track of all child nodes.
  
- **Processing Descriptions:** For each description:
  - If the parent node isn't already in `nodes`, we create a new `TreeNode` for it.
  - Similarly, if the child node isn't already present, we create a new `TreeNode` for it.
  - Depending on the `is_left` value, we set the child as either the left or right child of the parent in the `TreeNode`.
  - We add the child node's value to the `children` set to track all known child nodes.

- **Identifying the Root:** After processing all descriptions, the root node can be identified as the only node not included in the `children` set. We iterate through our `nodes` dictionary to find a node whose value is not in `children`.

- **Return the Root:** Finally, we return the root node.

## 2. Time and Space Complexity Analysis

- **Time Complexity:** O(N)
  - Each description is processed once, leading to a linear time complexity relative to the number of descriptions (N). Creating and accessing nodes are O(1) operations on average.

- **Space Complexity:** O(N)
  - We create a new node in memory for every unique parent and child. Thus, the space used is proportional to the number of unique nodes which is at most N.

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **Direct Mapping and Access:** By using a dictionary to store the nodes, we can quickly access and create nodes as needed in constant time. This prevents costly search operations that could occur if we used lists.
  
- **Clear Structure Maintenance:** The separation of nodes and children simplifies the identification of the root by leveraging a set to track children. This reduces the complexity of determining which node is the root.

- **Single Pass Element Processing:** The tree is built in a single pass through the descriptions rather than needing multiple iterations, ensuring that it scales linearly with the input size, making it suitable even for larger datasets.

This efficient use of data structures and algorithmic steps makes the solution both straightforward and performant, addressing the problem requirements effectively.
```

Runtime: undefined
Memory: 27772000
"""

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
#         reference = {}
#         roots = set()
#         for parent, child, is_left in descriptions:
#             if parent not in reference:
#                 reference[parent] = TreeNode(parent)
#                 roots.add(parent)
#             if child not in reference:
#                 reference[child] = TreeNode(child)
#             if is_left:
#                 reference[parent].left = reference[child]
#             else:
#                 reference[parent].right = reference[child]

#             if child in roots:
#                 roots.remove(child)
#         return reference[list(roots)[0]]


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            children.add(child)

        root_val = next(val for val in nodes if val not in children)
        return nodes[root_val]
