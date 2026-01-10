"""
# LeetCode Solution Explanation for "Design A Leaderboard"

## 1. Approach Explanation

The solution implements a simple leaderboard system where each player is identified by a unique `playerId`, and they have associated scores which can be added to or reset. The main components of this implementation are:

- **Data Structure**: A Python dictionary `self.scores` is used to maintain the current scores of all players. The `playerId` serves as the key while the score is the value.

- **Methods**:
  - `addScore(playerId: int, score: int)`: This method adds a given score to a player's current score. If the player does not exist in the dictionary, they are initialized with the provided score. The operation is efficient and executed in constant time O(1).
  
  - `top(K: int)`: This method computes the total score of the top `K` players. It uses the `heapq.nlargest` function to efficiently retrieve the top `K` scores from the list of all scores. The time complexity for this operation is O(N log K) due to the need to maintain a min-heap of size K.
  
  - `reset(playerId: int)`: This method resets a player's score to zero by removing their entry from the dictionary. If the player exists, their score is deleted in constant time O(1).

Overall, the approach efficiently addresses the requirements of tracking scores, calculating top scores, and resetting scores for players.

## 2. Time and Space Complexity Analysis

- **Time Complexity**:
  - `addScore`: O(1)
  - `top`: O(N log K), where N is the number of players (i.e., the number of unique player IDs in the leaderboard). This is because `heapq.nlargest` requires O(N) to consider all players and O(log K) to maintain the min-heap of size K.
  - `reset`: O(1)

- **Space Complexity**: O(N), where N is the total number of unique player IDs. This is due to the space used by the `self.scores` dictionary to store each player's score.

## 3. Efficiency of the Approach

This approach is efficient for several reasons:

- **Simplicity of Operations**: The use of dictionary operations (`addScore` and `reset`) allows for quick updates and deletions without needing to traverse or sort large datasets, resulting in constant time complexity for these operations.

- **Optimal Score Retrieval**: The use of a heap to retrieve the top `K` scores balances the need between having quick access to the largest scores while ensuring that updates to the leaderboard can scale with the number of players.

- **Flexibility**: The structure can easily accommodate various numbers of players and scores without a significant increase in complexity or resource requirements.

This combination of efficient data structure choice and algorithmic strategies ensures that the leaderboard can handle operations effectively, even as the number of players increases.

Runtime: undefined
Memory: 19960000
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
