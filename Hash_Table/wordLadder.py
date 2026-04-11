"""
## Explanation of the LeetCode Solution for "Word Ladder"

### 1. Approach

The approach used in this solution is based on the Breadth-First Search (BFS) algorithm. The goal of the "Word Ladder" problem is to find the shortest transformation sequence from the `beginWord` to the `endWord`, where each transformed word must exist in the provided `wordList` and can only differ by one letter.

Here’s how the algorithm works:

- **Initialization**: 
  - Convert the `wordList` into a set for O(1) average-time complexity of lookups.
  - Create a visited set to keep track of the words that we have already processed, starting with the `beginWord`.
  - Use a deque (double-ended queue) to facilitate BFS, initializing it with the tuple `(beginWord, 1)`, where `1` represents the initial distance.

- **BFS Loop**: 
  - Process the words in the queue until it is empty:
    - Dequeue the first element to get the current word and its associated distance.
    - If the current word equals `endWord`, return the distance as the result (the length of the transformation sequence).
    - Iterate through each character of the current word:
      - For each character, attempt to replace it with every letter from 'a' to 'z' (a total of 26 possibilities).
      - Generate a new word and check if it is in the `wordList` and has not been visited. If both conditions are satisfied, enqueue the new word with its incremented distance, and mark it as visited.

- **Final Return**: If the queue is exhausted and `endWord` has not been found, return `0`, indicating no possible transformation exists.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - The BFS explores each word level by level and generates up to \(26 \times L\) possible new words per current word (where \(L\) is the length of the words). In the worst case, it might have to explore all words in the `wordList`. Thus, the time complexity can be approximated as \(O(N \times L \times 26)\), where \(N\) is the number of words in `wordList`.

- **Space Complexity**: 
  - In the worst case, the space used by the queue can be \(O(N)\), and the visited set also uses \(O(N)\). Thus, the total space complexity is \(O(N)\).

### 3. Efficiency of This Approach

This BFS approach is efficient for the following reasons:

- **Optimality**: BFS is well-suited for finding the shortest path in an unweighted graph, where each transformation can be thought of as an edge connecting two nodes (words).
  
- **Set Lookup**: Using a set for `wordList` allows O(1) average time complexity for checking if a new word exists, significantly speeding up the process compared to a list-based lookup.

- **Early Exit**: The algorithm can immediately return the distance upon finding the `endWord`, minimizing unnecessary processing.

Given the constraints of the problem, BFS is a natural fit that balances complexity and performance, enabling the solution to handle a variety of inputs efficiently.

Runtime: undefined
Memory: 20468000
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        visited = set(beginWord)
        queue = Deque([(beginWord, 1)])
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i, c in enumerate(word):
                for j in range(1, 26):
                    new_ch = chr(ord('a') + (ord(c) - ord('a') + j) % 26)
                    new_word = word[:i] + new_ch + word[i+1:]

                    if new_word not in visited and new_word in wordList:
                        queue.append((new_word, dist + 1))
                        visited.add(new_word)
                        
        return 0
