# BINARY_SEARCH_TREE

class BST:
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError("invalid input")
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if not isinstance(value, int):
            raise TypeError("invalid input")
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
    
    def getmin(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr.value

    def remove(self, value):
        if not isinstance(value, int):
            raise TypeError("invalid input")
        
        if value == self.value:
            if not self.right and not self.left:
                return None
            elif self.right and not self.left:
                return self.right
            elif self.left and not self.right:
                return self.left
            else:
                #either max predecessor, or min successor, here is min successor
                min_child = self.right.getmin()
                self.value = min_child
                self.right = self.right.remove(min_child)
                

        elif value < self.value:
            if self.left:
                self.left = self.left.remove(value)
            else:
                return None
        else:
            if self.right:
                self.right = self.right.remove(value)
            else:
                return None

        return self

    def find(self, value):
        if not isinstance(value, int):
            raise TypeError("invalid input")
        
        if value == self.value:
            return True
        elif value < self.value:
            if self.left:
                return self.left.find(value)
            else:
                return False
        else:
            if self.right:
                return self.right.find(value)
            else:
                return False
        
    def countNodes(self):
        l_sum = r_sum = 0
        if self.left:
            l_sum = self.left.countNodes()
        if self.right:
            r_sum = self.right.countNodes()

        return l_sum + r_sum + 1


    def printValues(self):
        if self.left:
            self.left.printValues()
        print(self.value)
        if self.right:
            self.right.printValues()


root = BST(10)
root.insert(5)
root.insert(7)
root.insert(9)
root.insert(12)
root.insert(15)

print(root.countNodes())

root.remove(5)
print(root.countNodes())

root.remove(7)
print(root.countNodes())

root.remove(9)
print(root.countNodes())

root.remove(12)
print(root.countNodes())

root.remove(15)
print(root.countNodes())

root.remove(10)


root.printValues()