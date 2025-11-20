# TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:


    def dfs(self, root):
        if root and root.left:
            root.left.val = 2* root.val + 1
            self.values.add(root.left.val)
            self.dfs(root.left)
        if root and root.right:
            root.right.val = 2* root.val + 2
            self.values.add(root.right.val)
            self.dfs(root.right)

    def __init__(self, root: Optional[TreeNode]):
        if root:
            self.root = root
            self.values = set([0])
            root.val = 0
            self.dfs(root)
        

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)