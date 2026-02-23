"""
## Explanation of the Solution

### 1. Approach:
The solution aims to determine whether a given string `s` contains all possible binary codes of a specified length `k`. A binary code of length `k` can have `2^k` unique combinations, which are strings composed of `0`s and `1`s.

The algorithm uses a sliding window approach with a frequency map (`window`) to maintain a count of characters in a window of the string. The key steps are:

- Iterate through each character in the string `s` using an index `e`.
- For each character, update the frequency of that character in the `window` dictionary.
- If the total number of characters in the current window exceeds `k`, move the starting index of the window (`start`) to the right until the window size becomes `k`.
- Whenever the window size precisely equals `k`, the substring from `start` to `e` is a valid binary code and is added to a set `uniques`.
- At the end of the iteration, the algorithm checks if the size of the `uniques` set is equal to `2^k`, indicating that all binary codes of length `k` are found in `s`.

### 2. Time and Space Complexity Analysis:
- **Time Complexity:** The time complexity of this algorithm is O(N), where N is the length of the string `s`. This is because each character in `s` is processed exactly once, and the operations involving updates and checks to the `window` and `uniques` data structures take constant time on average.
  
- **Space Complexity:** The space complexity is O(2^k) due to the need to store all unique binary substrings of length `k` in the set `uniques`. Additionally, the frequency map `window` can potentially store a maximum of 2 keys if only binary `0`s and `1`s are considered.

### 3. Efficiency of the Approach:
This approach is efficient for several reasons:
- **Direct Counting:** The use of a sliding window allows for efficient substring management without needing to create multiple overlapping substrings explicitly.
- **Set for Uniqueness:** By leveraging a set to store distinct substrings, we can quickly check if we have encountered all `2^k` combinations.
- **Single Pass:** Processing the string in a single pass while maintaining the relevant window guarantees optimal time efficiency, making practical applications feasible for reasonably sized strings even as `k` increases.
  
Overall, the sliding window technique combined with a hash map for frequency counting minimizes both computation and memory overhead, making it well-suited for the problem at hand.

Runtime: undefined
Memory: 52104000
"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # A binary code has exactly 2 options per position ('0' or '1'). 
        # For a length of k, the total number of unique combinations is 2^k. 
        # Therefore, to contain every possible binary code of size k, the string must yield exactly 2^k distinct substrings of that length.
        window = {}
        uniques = set()
        start = 0
        for e in range(len(s)):
            window[s[e]] = window.get(s[e], 0) + 1
            while sum(window.values()) > k :
                window[s[start]] -= 1
                start+=1

            if sum(window.values()) == k:
                uniques.add(s[start:e+1])

        return len(uniques) == 2 ** k
        
