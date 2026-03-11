"""
# LRU Cache Solution Explanation

## 1. Brief Explanation of the Approach

The provided code implements an LRU (Least Recently Used) Cache using a combination of a doubly linked list and a hash map (dictionary). The doubly linked list allows for efficient addition and removal of nodes while maintaining the order of usage, with the most recently used items at the tail and the least recently used items at the head.

### Key Components:
- **ListNode**: Represents a node in the doubly linked list, containing the key-value pair and pointers to both the next and previous nodes.
- **LRUCache**: The main class that manages the cache. It initializes with a specified capacity and uses a hash map (`cache`) to store keys and pointers to their corresponding nodes in the linked list.

### Methods:
- **_remove(key)**: Removes a node associated with the given key from the linked list and the hash map.
- **_add(key, val)**: Adds a new node with the specified key-value pair to the end (tail) of the linked list.
- **_to_end(key, val)**: Updates the position of a key in the cache to the most recently used position by removing it (if it exists) and adding it again.
- **get(key)**: Retrieves the value associated with a key. If the key exists, it updates the key's position to the most recently used and returns the value; otherwise, it returns -1.
- **put(key, value)**: Adds a key-value pair to the cache and checks if the capacity is exceeded. If it is, the least recently used item (head.next) is removed.

## 2. Time and Space Complexity Analysis

### Time Complexity:
- **get(key)**: O(1) - The cache is accessed in constant time using the hash map.
- **put(key, value)**: O(1) - Involves operations that are all constant time due to the hash map and linked list interactions.
- **_add() and _remove()**: O(1) - Both operations involve adjusting pointers in the linked list and accessing the hash map.

### Space Complexity:
- O(capacity) - The space used is linear with respect to the cache capacity, due to storing at most 'capacity' nodes in the linked list and their corresponding entries in the hash map.

## 3. Why This Approach is Efficient

This approach effectively combines the strengths of both the hash map and doubly linked list:
- **Hash Map**: Provides O(1) average time complexity for lookups (to check in the cache) and removals based on the key.
- **Doubly Linked List**: Allows for efficient reordering of nodes based on usage without needing to traverse the structure; each operation (addition/removal) is done in O(1) time.

Thus, this structure provides optimal performance for the LRU Cache operations, making it a robust choice for the problem requirement to efficiently handle cache operations while maintaining the order of usage.

Runtime: undefined
Memory: 76796000
"""

class ListNode():
    def __init__(self, key = -1, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def _remove(self, key):
        node = self.cache[key]
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.cache[key]

    def _add(self, key, val):
        node = ListNode(key, val)
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node
        self.cache[key] = node


    def _to_end(self, key, val):
        if key in self.cache:
            self._remove(key)
        self._add(key, val)


    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            self._to_end(key, val)
            return val

        return -1


    def put(self, key: int, value: int) -> None:
        self._to_end(key, value)
        if len(self.cache) > self.capacity:
            node = self.head.next
            self._remove(node.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
