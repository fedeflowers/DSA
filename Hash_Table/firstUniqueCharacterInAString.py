"""
```markdown
### Explanation of the Approach

The solution for the "First Unique Character in a String" problem employs a two-step approach:

1. **Counting Character Occurrences**: It utilizes the `collections.Counter` from the Python standard library to build a frequency dictionary where each character in the string is counted, effectively capturing how many times each character appears in the input string `s`.

2. **Finding the First Unique Character**: After establishing the frequency counts, the code iterates through the string again using `enumerate`, which allows both the index and the character to be accessed. It checks the frequency of each character. The first character that has a count of 1 (unique) is returned by its index. If no unique character exists, the function returns -1.

### Time and Space Complexity Analysis

- **Time Complexity**: The overall time complexity of this solution is O(N), where N is the length of the input string `s`. This is because the solution makes two passes over the string: one for counting the characters and another for finding the first unique character.

- **Space Complexity**: The space complexity is O(K), where K is the number of unique characters in the string. The dictionary created by `Counter` will store entries for each unique character in the string.

### Why This Approach is Efficient

This approach is efficient for several reasons:

1. **Single Pass for Counting**: Using `collections.Counter` allows for an efficient counting of characters in a single pass over the string. This avoids the need for nested loops or multiple scans of the string.

2. **Immediate Retrieval for Index**: The second pass to find the first unique character checks a precomputed count, making it efficient to check uniqueness (a constant-time operation) as it iterates.

3. **Simplicity and Readability**: The use of standard library features like `Counter` not only simplifies the code but also enhances readability, making it easier for others to understand and maintain.

Overall, while solving the problem within the constraints, this approach balances clear logic and efficient execution.
```

Runtime: undefined
Memory: 18228000
"""

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         #l : count
#         #l : index
#         #se count > 1 tolgo index da set?
#         counter = {}
#         indexes_single = {}
#         for i, l in enumerate(s):
#             counter[l] = counter.get(l, 0) + 1
#             indexes_single[l] = i
#             if counter[l] >= 2:
#                 del indexes_single[l]

#         if len(indexes_single) >= 1:
#             return min(indexes_single.values())
#         return -1
        

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map: character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
