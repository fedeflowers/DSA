# BINARY_TREE

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        q = deque([self.root])
        while q:
            node = q.popleft()
            if not node.left:
                node.left = new_node
                return
            elif not node.right:
                node.right = new_node
                return
            else:
                q.append(node.left)
                q.append(node.right)

    def search(self, value):
        if not self.root:
            return None
        q = deque([self.root])
        while q:
            node = q.popleft()
            if node.value == value:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return None

    def inorder(self):
        def _inorder(node):
            if not node:
                return []
            return _inorder(node.left) + [node.value] + _inorder(node.right)
        return _inorder(self.root)

    def remove(self, value):
        if not self.root:
            return

        q = deque([self.root])
        node_to_delete = None
        last_node = None
        parent_of_last = None

        while q:
            current = q.popleft()
            if current.value == value:
                node_to_delete = current
            if current.left:
                parent_of_last = current
                q.append(current.left)
            if current.right:
                parent_of_last = current
                q.append(current.right)
            last_node = current

        if node_to_delete and last_node:
            node_to_delete.value = last_node.value  # Replace value
            # Delete the last node
            if parent_of_last:
                if parent_of_last.right == last_node:
                    parent_of_last.right = None
                elif parent_of_last.left == last_node:
                    parent_of_last.left = None
            elif self.root == last_node:
                self.root = None  # Single-node tree
