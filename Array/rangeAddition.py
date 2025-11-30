"""
## Explanation of the Solution to the "Range Addition" Problem

### 1. Approach Explanation
The problem involves performing multiple range updates on an array of zeros. Instead of updating each index for every range operation directly, which can be inefficient, the solution employs a more optimal technique known as the **difference array** method. 

Here's how it works:

- **Initialization**: We start with an array `arr` initialized with zeros of the given `length`.
  
- **Range Update**: For each update specified by `s`, `e`, and `inc` (where `s` is the start index, `e` is the end index, and `inc` is the increment value), we:
  - Increase `arr[s]` by `inc` to denote that starting from index `s`, we want to add `inc`.
  - Decrease `arr[e + 1]` by `inc` (if `e + 1` is within bounds) to indicate that the addition should stop after index `e`.

- **Final Array Construction**: After processing all updates, we compute the final modified array. We iterate through the `arr`, maintaining a running sum (`curr_s`) that allows us to build the actual values of the modified array by summing up the differences.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The overall time complexity is \( O(N + U) \), where \( N \) is the length of the resulting array and \( U \) is the number of updates. We loop through the updates once (O(U)) and then iterate through the entire array once to construct the final result (O(N)).

- **Space Complexity**: The auxiliary space used is \( O(N) \) for the `arr` and final output array `final_arr`. Hence, the overall space complexity is \( O(N) \).

### 3. Why this Approach is Efficient
This approach is efficient due to the following reasons:

- **Reduced Operations**: Instead of updating every index for each range operation (which can lead to a time complexity of \( O(U \times N) \) in the worst-case scenario), this method reduces the number of operations needed to just two for each update, regardless of the size of the range.

- **Directly Builds the Result**: The use of a difference array allows for a quick compilation of the results through a single pass after all updates have been marked. This avoids redundant calculations and minimizes time spent.

- **Optimized for Large Inputs**: In scenarios where there are many updates but the actual length of the array is sizeable, this method significantly optimizes performance and is especially useful in competitive programming and scenarios with high constraints.

This method effectively allows for efficient range modifications while maintaining a low computational overhead, making it a suitable choice for problems like "Range Addition".

Runtime: undefined
Memory: 23496000
"""

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        #easiest way, incr first index, decrements last index + 1
        arr = [0] * length
        for s, e, inc in updates:
            arr[s] += inc
            if e+1 < length:
                arr[e+1] -= inc

        final_arr = []
        curr_s = 0
        for el in arr:
            curr_s += el
            final_arr.append(curr_s)

        return final_arr
