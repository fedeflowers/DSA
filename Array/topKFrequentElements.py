"""
# Explanation of the LeetCode Solution for "Top K Frequent Elements"

## 1. Approach Explanation

The solution uses a combination of **frequency counting** and a **quickselect algorithm** to efficiently find the top k most frequent elements in an array. Here's a step-by-step breakdown of the approach:

1. **Counting Frequencies**: 
   - The `Counter` from the `collections` module is used to count the occurrences of each number in the input list `nums`. This gives a dictionary-like object `freq` where the keys are the numbers and the values are their frequencies.
  
2. **Extracting Unique Elements**:
   - The unique keys from the frequency counter are extracted into a list called `unique`.

3. **Quickselect Algorithm**:
   - The algorithm defines a helper function `quickselect(arr, target_idx)` that recursively partitions the array `arr` based on the frequencies of the elements, relative to a randomly chosen pivot.
   - It creates three partitions:
     - `lows`: Elements that are less frequent than the pivot.
     - `mids`: Elements that are equally frequent as the pivot.
     - `highs`: Elements that are more frequent than the pivot.
   - It then checks where the `target_idx` falls:
     - If it's in the `lows`, it recursively searches in that partition.
     - If it's in the `mids`, it returns the pivot, as this is where the cutoff is found.
     - If it's in the `highs`, it adjusts the `target_idx` and continues searching in that partition.
  
4. **Getting Top K Frequent Elements**:
   - The `kth_most_freq` is determined by calling `quickselect` with the index corresponding to the k-th most frequent element.
   - Finally, it returns all elements with a frequency greater than or equal to the frequency of the `kth_most_freq`.

## 2. Time and Space Complexity Analysis

- **Time Complexity**:
  - The average case time complexity of the quickselect algorithm is O(N), where N is the number of unique elements. In the worst case, it can degrade to O(N^2) if the pivot selection is poor, but this is rare when using a randomized pivot as done here.
  - The frequency counting with `Counter` takes O(N), where N is the total number of elements in `nums`.
  - Therefore, the overall time complexity can be approximated to O(N) for typical cases.

- **Space Complexity**:
  - Space complexity is O(U) where U is the number of unique elements. This includes space for storing the frequency count and the `unique` list.
  - Additional space is used for the partitions in the quickselect function, but since these are generated in each recursive call and are not retained beyond that scope, they do not contribute to overall complexity.

## 3. Efficiency of the Approach

This approach is efficient due to several reasons:

- **Average Case Performance**: The quickselect algorithm leverages a divide-and-conquer strategy that allows it to efficiently narrow down the search for the k-th largest element without needing to sort the entire array. This results in faster runtime on average compared to sorting-based approaches, which would take O(U log U).

- **Reduction of Redundant Computation**: By focusing only on unique elements and their frequencies, the algorithm reduces unnecessary comparisons and operations, especially when k is much smaller than the total number of elements.

- **Randomized Pivot Selection**: The use of a random pivot helps prevent worst-case scenarios that could arise due to sorted or reversed input arrays, leading to consistently good performance in practice.

In summary, this solution effectively combines frequency counting with an efficient selection algorithm to deliver a robust and scalable solution to the problem of finding the top k frequent elements in an array.

Runtime: undefined
Memory: 22920000
"""

import random
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        unique = list(freq.keys())

        def quickselect(arr, target_idx):
            if len(arr) == 1:
                return arr[0]

            pivot = random.choice(arr)
            pivot_freq = freq[pivot]

            # Partition the numbers based on their frequency relative to the pivot's frequency
            lows = [x for x in arr if freq[x] < pivot_freq]
            mids = [x for x in arr if freq[x] == pivot_freq]
            highs = [x for x in arr if freq[x] > pivot_freq]

            if target_idx < len(lows):
                # Target is in the lows partition
                return quickselect(lows, target_idx)
            elif target_idx < len(lows) + len(mids):
                # Target frequency is the pivot frequency (cutoff found)
                return mids[0]
            else:
                # Target is in the highs partition.
                # Adjust the target index to be relative to the 'highs' array.
                new_target_idx = target_idx - len(lows) - len(mids)
                return quickselect(highs, new_target_idx) 

        kth_most_freq = quickselect(unique, len(unique) - k)
        return [x for x in unique if freq[x] >= freq[kth_most_freq]]

