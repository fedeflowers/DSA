"""
```markdown
## Explanation of LeetCode Solution for "Valid Anagram"

### 1. Brief Explanation of the Approach
The provided solution utilizes an array to count the occurrences of each character from the two input strings, `s` and `t`. Both strings are assumed to consist of lowercase English letters.

- **Character Counting**: An array `d` of size 26 (for each letter in the alphabet) is initialized to hold counts of characters. 
  - For each character in string `s`, the corresponding index in the array is incremented.
  - For each character in string `t`, the corresponding index is decremented.

- **Final Check**: After processing both strings, if `s` and `t` are anagrams, all entries in the array `d` should equal zero (indicating that every character in `s` has a matching character in `t`).

### 2. Time and Space Complexity Analysis
- **Time Complexity**: 
  - Iteration through string `s`: O(N), where N is the length of string `s`.
  - Iteration through string `t`: O(M), where M is the length of string `t`.
  - Hence, the overall time complexity is O(N + M). In the case where both strings are of equal length, it simplifies to O(N).

- **Space Complexity**: 
  - The space complexity is O(1) since we only utilize a fixed-size list of 26 integers, regardless of the size of the input strings. This means the space used does not grow with the input size.

### 3. Why This Approach is Efficient
This approach is efficient for the following reasons:
- **Linear Time Complexity**: The solution runs in linear time relative to the total length of the input strings, which is efficient given that we can’t determine whether they are anagrams without examining each character at least once.
- **Constant Space Usage**: It uses a constant amount of space (an array of 26 integers) to keep track of character counts, leading to effective memory utilization.
- **Simplicity**: The algorithm is straightforward and easy to understand. It directly reflects the properties of anagrams, making it conceptually simple while providing optimal performance.
```


Runtime: undefined
Memory: 19444000
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = [0] * 26
        for ch in s:
            d[ord(ch) - ord("a")] += 1
        for ch in t:
            d[ord(ch) - ord("a")] -= 1


        return all(el == 0 for el in d)


