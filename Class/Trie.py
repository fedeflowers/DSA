# Node
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.eow = False

class Trie:
    def __init__(self):
        self.root = Node()

    def ch_to_idx(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        curr = self.root
        for ch in word:
            idx = self.ch_to_idx(ch)
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.eow = True

    def _search(self, word):
        curr = self.root
        for ch in word:
            idx = self.ch_to_idx(ch)
            if curr.children[idx] is None:
                return None
            curr = curr.children[idx]
        return curr

    def search(self, word):
        node = self._search(word)
        if not node:
            return False
        if node and node.eow == True:
            return True
        return False

    def startsWith(self, prefix):
        node = self._search(prefix)
        if not node:
            return False
        return True

    def remove(self, word):
        def _remove(curr, word, depth):
            if curr is None:
                return False

            if depth == len(word):
                if curr.eow == False:
                    return False
                curr.eow = False
                return all(child is None for child in curr.children)

            idx = self.ch_to_idx(word[depth])
            safe_del = _remove(curr.children[idx], word, depth+1)

            if safe_del:
                curr.children[idx] = None 
                return not curr.eow and all(child is None for child in curr.children)

            return False

        _remove(self.root, word, 0)