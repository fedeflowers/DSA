"""
```markdown
# Explanation of the LeetCode Solution for "Implement Queue using Stacks"

## 1. Approach Explanation

The problem requires us to implement a queue using two stacks. A queue operates in a First-In-First-Out (FIFO) manner, while a stack operates in a Last-In-First-Out (LIFO) manner. We can leverage the characteristics of the stacks to simulate the queue operations.

### Components of the Solution:
- **Initialization**:
  - Two stacks are initialized: `first` and `second`.
  
- **Push**:
  - When we `push` an element, we simply add it to the `first` stack. This step is direct and takes O(1) time.

- **Pop**:
  - When popping an element, we need to retrieve the oldest element (the one that has been in the queue the longest). If the `second` stack is not empty, we pop from it directly, which takes O(1) time. 
  - If `second` is empty, we transfer all elements from `first` to `second` (flipping their order in the process) and then pop from `second`. This transfer operation is handled by the `_popolate` helper method and takes O(n) time in the worst case, where n is the total number of elements in `first`.

- **Peek**:
  - The `peek` operation works similarly to `pop`. If `second` is not empty, we simply return the top element of `second`. If it’s empty, we transfer elements from `first` to `second` and then return the top of `second`.

- **Empty**:
  - The `empty` method checks if both stacks are empty, effectively determining if the queue is empty.

## 2. Time and Space Complexity Analysis

### Time Complexity:
- **Push**: O(1) - Directly appending to the stack.
- **Pop**: Amortized O(1) - Each element is moved between stacks at most once, leading to an average of O(1) time for every pop operation across multiple calls.
- **Peek**: Amortized O(1) - Similar reasoning as pop; it requires a move only when `second` is empty.
- **Empty**: O(1) - Simple length check.

Overall, each operation (push, pop, peek, and empty) can be considered O(1) amortized over a sequence of operations.

### Space Complexity:
- O(n) - The space needed to store the elements in the two stacks is proportional to the number of elements, n, that have been pushed onto the queue.

## 3. Efficiency of the Approach

The efficiency of this approach comes from the amortized constant-time complexity for the operations. By transferring elements between the two stacks only when necessary, we efficiently use the LIFO characteristic of stacks to support the FIFO behavior of queues.

This strategy minimizes the number of times we rearrange the elements, ensuring that the overall cost of operations remains low over a series of operations. Thus, while some operations may seem costly (such as transferring elements), they are infrequent in the grand scheme and lead to an efficient implementation of the queue.

```


Runtime: undefined
Memory: 17752000
"""

class MyQueue:

    def __init__(self):
        self.first = []
        self.second = []        

    def _popolate(self):
        while self.first:
            self.second.append(self.first.pop())

    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        if not self.second and not self.first:
            return None
        if self.second:
            return self.second.pop()
        else:
            self._popolate()
            return self.second.pop()

    def peek(self) -> int:
        if not self.second and not self.first:
            return None
        if self.second:
            return self.second[-1]
        else:
            self._popolate()
            return self.second[-1]
        

    def empty(self) -> bool:
        return len(self.first) + len(self.second) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# [6,7,8]
# [5,3,3,2,1]

# [1,2,3,4,5]

