"""
## Explanation of the LeetCode Solution for "Valid Anagram"

### 1. Brief Explanation of the Approach
The given solution checks if two strings, `s` and `t`, are anagrams of each other. The approach used in this solution involves the following steps:

- Both strings `s` and `t` are converted into lists of characters and then sorted.
- The sorted lists of both strings are compared.
- If the sorted versions of the two strings are identical, the function returns `True`, indicating that `s` and `t` are anagrams. Otherwise, it returns `False`.

The sorting step ensures that if both strings are anagrams, their characters will be in the same order after sorting.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The time complexity of this solution is O(N log N), where N is the length of the longer string among `s` and `t`. This is due to the sorting operation, which generally has a time complexity of O(N log N).
  
- **Space Complexity**: The space complexity is O(N) as well, since two lists are created to store the characters of `s` and `t` before sorting. Each of these lists requires space proportional to the length of the respective strings.

### 3. Why This Approach is Efficient
This sorting-based approach is simple and easy to understand. It provides a clear method to determine if two strings are anagrams by leveraging the properties of sorted orders. 

- **Pros**: The algorithm correctly handles cases where characters may appear multiple times and is also straightforward in terms of implementation.
- **Cons**: While it is efficient in terms of code simplicity, it may not be the most optimal in terms of time complexity compared to other potential approaches (like using frequency counts), which can achieve O(N) time complexity with a linear traversal and a constant space overhead.

While the sorting method is efficient for small to moderately sized strings, for very large strings or performance-critical applications, other techniques (like counting characters with a hash map or an array) might be preferred due to their linear time complexity. 

Overall, this solution effectively leverages sorting to solve the anagram problem, making it a valid and straightforward solution.

Runtime: undefined
Memory: 20864000
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        print(s, t)
        return s == t
