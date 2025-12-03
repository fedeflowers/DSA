"""
```markdown
## Explanation of the Solution

### 1. Brief Explanation of the Approach
The provided solution determines the index of the first non-repeating character in a given string `s`. The approach uses two dictionaries:
- `counter`: to keep track of the count of each character in the string.
- `indexes_single`: to store the index of characters that have been identified as unique (i.e., they appear only once in the string).

The algorithm proceeds as follows:
1. It iterates over each character `l` in the string `s`, using `enumerate` to also capture the index `i`.
2. For each character:
   - It updates the `counter` dictionary with the count of that character.
   - It updates the `indexes_single` dictionary with the index of the character.
   - If the character's count in `counter` reaches 2 or more, it removes the character from the `indexes_single` dictionary as it is no longer unique.
3. After processing all characters, if there are any characters left in `indexes_single`, it returns the smallest index among those characters. If all characters are non-unique, it returns -1.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N), where N is the length of the string `s`. The solution processes each character in the string exactly once in a single pass.
- **Space Complexity**: O(1) considering the character set is constant, as the space used for dictionaries is proportional to the number of unique characters. In the worst-case scenario, for alphabets (assuming no special characters), the space complexity can be considered O(1) because there are a limited number of characters (e.g., 26 for lowercase letters).

### 3. Why This Approach is Efficient
This approach is efficient due to its use of a single pass (O(N) time complexity) to gather necessary information about character counts and their indices. Instead of using additional data structures like lists to store unique characters, it utilizes dictionaries to ensure constant-time lookups and updates. The maintenance of indices only for characters that could potentially be unique allows for a quick retrieval of the first non-repeating character at the end of the process. Overall, this method minimizes overhead and efficiently achieves the goal of identifying the first unique character.
```

Runtime: undefined
Memory: 17912000
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        #l : count
        #l : index
        #se count > 1 tolgo index da set?
        counter = {}
        indexes_single = {}
        for i, l in enumerate(s):
            counter[l] = counter.get(l, 0) + 1
            indexes_single[l] = i
            if counter[l] >= 2:
                del indexes_single[l]

        if len(indexes_single) >= 1:
            return min(indexes_single.values())
        return -1
        
