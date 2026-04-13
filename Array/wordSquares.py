"""
# Explanation of the LeetCode Solution for "Word Squares"

## 1. Brief Explanation of the Approach

The solution employs a backtracking method to construct all possible word squares using a list of words. A word square is formed by arranging words such that the ith word is formed by the ith letters of all the words in the square. The approach can be summarized as follows:

- **Prefix Construction**: 
  - The algorithm creates a dictionary (`prefix`) where keys are prefixes of words, and values are lists of words that share the corresponding prefix. For instance, if "ball" is in the word list, prefixes like "b", "ba", "bal", and "ball" will be created with "ball" being in each of their corresponding lists.
  
- **Backtracking**:
  - The backtracking function attempts to build the word square incrementally. It starts with an initial word, checks the next layer of candidates using prefixes that match the square formed so far, and continues to add candidates until a complete square is formed.
  - If the current square reaches the desired length (`n`), that square is added to the results list. The function uses the current length of the square to determine which character to consider for the new prefix.

- **Iterating through words**:
  - The process begins by iterating through each word in the input list, triggering the backtracking function initialized with that word.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - The overall time complexity can be approximated as O(N^4) in the worst case because for each of the N words in the list, and for each prefix computed (which could involve multiple recursive calls), we check all potential candidates for each position in the square. Keep in mind that N represents the number of words in the input list, and it's assumed that the lengths of the words are limited to 4.

- **Space Complexity**: 
  - The space complexity is largely driven by the `prefix` dictionary which could potentially store a significant number of prefixes (though their quantity is limited). Additionally, auxiliary space used by the recursion stack and storing the resulting word squares adds to this complexity. In total, we can consider space complexity to be O(N * L), where L is the length of the words, again assuming N is manageable due to typical constraints in competitive programming.

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **Prefix Optimization**: By pre-computing the possible prefixes and storing the candidates in a dictionary, the algorithm can quickly retrieve the next possible candidates at each step of the backtracking process. This reduces unnecessary comparisons and speeds up the search significantly.

- **Backtracking**: The backtracking ensures that the solution space is explored efficiently by pruning invalid paths early on as soon as it becomes clear that a square cannot be formed. Since every attempt builds on previously validated words, it minimizes re-evaluation of potential candidates.

- **Handling Constraints**: The problem constraints shape the algorithm's efficiency; since the words are limited to 4 letters, the number of combinations is feasible, and thus the approach can potentially identify all valid word squares without excessive computation that would be incurred by brute force methods.

Overall, the combination of prefix creation and backtracking allows the solution to effectively explore and construct valid word squares while minimizing overhead.

Runtime: undefined
Memory: 42968000
"""

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # secret, you choose a word, based on that word you can have specific candidates,
        # constraints are 4 chars per word, so max square of 4
        # based the word build the prefix you need
        # you choose ball, next prefix -> a
        # area -> le, lead -> lad, lady
        
        n = len(words[0])
        
        # build prefixes
        prefix = defaultdict(list)
        for word in words:
            for i in range(1, len(word) + 1): # always 4
                prefix[word[:i]].append(word) # append the candidate
                
        res = []
        def backtrack(square: str) -> None:
            if len(square) == n:
                res.append(square[:])
                return
            
            k = len(square)
            pref_to_search = "".join([square[i][k] for i in range(k)]) # build prefix
            
            for candidate in prefix[pref_to_search]:
                square.append(candidate)
                backtrack(square)
                square.pop()
                
        
        for word in words:
            backtrack([word]) 
        
        return res
            
            
            
            
            
            
            
            
            
            
            
