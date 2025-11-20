# BST_OOD

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        elif key > root.key:
            root.right = self._insert_rec(root.right, key)
        return root

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_rec(root.left, key)
        else:
            return self._search_rec(root.right, key)

    def remove(self, key):
        self.root = self._remove_rec(self.root, key)

    def _remove_rec(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._remove_rec(root.left, key)
        elif key > root.key:
            root.right = self._remove_rec(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children: get inorder successor
            successor = self._min_value_node(root.right)
            root.key = successor.key
            root.right = self._remove_rec(root.right, successor.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        return self._inorder_rec(self.root)

    def _inorder_rec(self, root):
        if root is None:
            return []
        return self._inorder_rec(root.left) + [root.key] + self._inorder_rec(root.right)
