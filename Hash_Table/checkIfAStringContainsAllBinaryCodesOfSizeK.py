"""
## Explanation of the Approach

The provided solution to the problem "Check If a String Contains All Binary Codes of Size K" operates by checking if a given binary string contains all possible binary substrings of length `k`. 

1. **Understanding Binary Codes**: 
   - A binary code of length `k` can take on values of either '0' or '1' at each position. Thus, there are a total of \(2^k\) unique combinations for such substrings.
   
2. **Using a Set for Uniqueness**:
   - The solution uses a set named `uniques` to store unique binary substrings of length `k` found in the string `s`.

3. **Iterating Over the String**:
   - The code iterates through the string, extracting all possible contiguous substrings of length `k` using slicing (`s[i:i+k]`), from index `0` to `len(s) - k + 1`.
   - Each unique substring is added to the set.
   
4. **Early Exit**:
   - If the size of the set `uniques` ever reaches \(2^k\) during the iterations, we can immediately return `True`, as that confirms that all binary codes of that length are present in the string.
   
5. **Final Check**:
   - If the loop finishes and we haven't returned `True`, it means that not all binary codes are present in `s`, so the function returns `False`.

## Time and Space Complexity Analysis

- **Time Complexity**: 
  - The time complexity of the algorithm is \(O(N)\), where \(N\) is the length of the input string `s`. This is because we scan through the string exactly once and perform constant-time operations for each substring of length `k`.
  
- **Space Complexity**: 
  - The space complexity is \(O(1)\) for the `uniques` set in terms of additional space, but more accurately it could be considered \(O(2^k)\) because in the worst case, you may need to store up to \(2^k\) unique substrings. The actual space used by the set grows with `k`, but it is capped at \(2^k\).

## Why This Approach is Efficient

- **Direct and Simple**: 
  - This approach provides a clear and straightforward way to solve the problem by leveraging hashing (using a set) to efficiently track unique substrings instead of redundant checks.

- **Early Stopping**:
  - The use of an early exit condition (when the unique count reaches \(2^k\)) significantly optimizes performance because it prevents unnecessary iterations once the goal is achieved.

- **Optimal Checks**:
  - Since it only needs to check up to \(N-k+1\) substrings of length `k`, it minimizes the number of checks required while ensuring it checks all potential substrings.

In summary, the solution is efficient, concise, and well-suited for the problem by strategically using hashing to keep track of unique binary codes of size `k`.

Runtime: undefined
Memory: 52232000
"""

# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         # A binary code has exactly 2 options per position ('0' or '1'). 
#         # For a length of k, the total number of unique combinations is 2^k. 
#         # Therefore, to contain every possible binary code of size k, the string must yield exactly 2^k distinct substrings of that length.
#         window = {}
#         uniques = set()
#         start = 0
#         for e in range(len(s)):
#             window[s[e]] = window.get(s[e], 0) + 1
#             while sum(window.values()) > k :
#                 window[s[start]] -= 1
#                 start+=1

#             if sum(window.values()) == k:
#                 uniques.add(s[start:e+1])

#         return len(uniques) == 2 ** k
        
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        required_count = 2 ** k
        uniques = set()
        
        for i in range(len(s) - k + 1):
            uniques.add(s[i:i+k])
            
            if len(uniques) == required_count:
                return True
                
        return False
