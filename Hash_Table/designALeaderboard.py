"""
```markdown
## Explanation of the Solution for "Design A Leaderboard"

### 1. Approach

The solution implements a leaderboard system using a class called `Leaderboard`. The leaderbord maintains player scores through a dictionary (`self.scores`) where the keys are player IDs and the values are their corresponding scores. The class has the following methods:

- **`__init__()`**: Initializes the leaderboard with an empty dictionary to store player scores.
  
- **`addScore(playerId: int, score: int)`**: This method updates the score of a player. If the player does not exist, it initializes their score to zero and adds the provided score. This method uses the dictionary's `get()` method to simplify the process of adding scores.

- **`top(K: int)`**: This method calculates the sum of the top K players' scores using a min-heap. It leverages the `heapq.nlargest()` function to efficiently retrieve the K largest scores from the dictionary values, and returns their sum.

- **`reset(playerId: int)`**: This method removes a player from the leaderboard, deleting their entry from the `self.scores` dictionary.

### 2. Time and Space Complexity Analysis

- **`addScore(playerId: int, score: int)`**:
  - **Time Complexity**: O(1) - inserting/updating an entry in a dictionary is on average O(1).
  - **Space Complexity**: O(1) - we are not using additional data structures in this method.

- **`top(K: int)`**:
  - **Time Complexity**: O(N log K) - the `heapq.nlargest(K, self.scores.values())` function retrieves the K largest scores from N total scores, which involves heap operations that take O(log K) time.
  - **Space Complexity**: O(K) - the method uses space to store the K largest scores.

- **`reset(playerId: int)`**:
  - **Time Complexity**: O(1) - checking if a player exists and deleting an entry in a dictionary is O(1) on average.
  - **Space Complexity**: O(1) - no additional space is used in this method.

Overall, the space complexity is O(N) where N is the number of unique player scores stored in the dictionary.

### 3. Efficiency of the Approach

This approach is efficient for the following reasons:

- **Fast Score Updates**: The use of a dictionary allows for O(1) average time complexity for adding or resetting player scores, making it suitable for real-time updates.

- **Efficient Top K Calculation**: Using the `heapq.nlargest()` function efficiently identifies the top K scores, which is critical for performance, especially as the number of players increases.

- **Memory Usage**: The leaderboard only stores the scores of active players, optimizing memory consumption by only retaining the necessary data.

In summary, this solution strikes a balance between performance and simplicity, making it a practical choice for a dynamic leaderboard system.
```

Runtime: undefined
Memory: 19792000
"""

class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        # O(1)
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    def top(self, K: int) -> int:
        # O(N log K) using a min-heap of size K
        return sum(heapq.nlargest(K, self.scores.values()))

    def reset(self, playerId: int) -> None:
        # O(1)
        if playerId in self.scores:
            del self.scores[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
