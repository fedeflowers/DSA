"""
Sure! Here’s an explanation of the given LeetCode solution for the problem "Median of Two Sorted Arrays":

## 1. Brief Explanation of the Approach

The algorithm finds the median of two sorted arrays by performing a binary search on the smaller array. The key insight is to partition both arrays into two halves such that all elements on the left are less than or equal to all elements on the right. Here's a step-by-step breakdown:

- **Initial Preparation**: First, the function ensures that the first array (A) is the smaller array. This helps to minimize the search space.
- **Calculate Total and Half**: It calculates the total length of both arrays combined and determines `half`, which is used to maintain the balance of the partition.
- **Binary Search Setup**: A binary search is then conducted on the smaller array (A). The search ranges are adjusted based on the comparison of the elements at the partition indices.
- **Partitioning Logic**: The partitions are defined by indices `i` (for array A) and `j` (for array B). Correct partitions mean that:
  - The maximum element on the left of A (`leftA`) must be less than or equal to the minimum element on the right of B (`rightB`).
  - Similarly, the maximum element on the left of B (`leftB`) must be less than or equal to the minimum element on the right of A (`rightA`).
- **Median Calculation**: Once the correct partition is found, the median can be computed:
  - If the total number of elements is even, the median is the average of the maximum of the left elements and the minimum of the right elements.
  - If the total is odd, the median is simply the minimum of the right elements.

The binary search adjusts either the left or right pointer based on the comparisons until the correct partition is found.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity is \( O(\log(\min(N, M))) \), where \( N \) and \( M \) are the lengths of the two arrays. This is because we are performing a binary search on the smaller array.
  
- **Space Complexity**: The space complexity is \( O(1) \) because we are using a constant amount of extra space and do not utilize any additional data structures.

## 3. Why This Approach is Efficient

This approach is efficient because:
- It leverages the sorted nature of the arrays by using binary search, which reduces the potential number of comparisons significantly compared to a linear approach of merging the arrays and finding the median.
- By always cutting down the search space to the smaller array and adjusting based on the relationships between the partition elements, it quickly homes in on the correct partition that defines the median.
- Instead of creating new arrays or data structures, it operates in-place with simple variables, leading to optimal space usage.

In summary, this binary search method efficiently finds the median in logarithmic time relative to the size of the smaller array while using minimal extra space.

Runtime: undefined
Memory: 18008000
"""

class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        # 2 arrays
        #fare bin search sul più piccolo, tenendo gli indici in modo che i  + j = half del totale, cioè prendo un tot degli elementi di A e un tot da B in modo che l'array tot sia bilanciato, quindi i+j = half
        # se è bilanciato allora la left di A <= rightB e leftB <= rightA
        #poi computo mediana se sono dispari o pari
        #fare bin search sempre sul più piccolo

        if len(A) > len(B):
            A, B = B, A

        # A contiene il più piccolo
        total = len(A) + len(B)
        half = total // 2
        #bin search sul più piccolo
        low = 0
        high = len(A)
        while low <= high:
            i = (low + high) // 2
            j = half - i

            leftA = A[i-1] if i > 0 else -float("inf") #se start array, il left = -inf cioè niente di più piccolo
            rightA = A[i] if i < len(A) else float("inf") #se end array, non c'è nulla di più grande
            leftB = B[j-1] if j > 0 else -float("inf")
            rightB  = B[j] if j < len(B) else float("inf")

            #compute median
            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB))/2
                else:
                    return min(rightA, rightB) 
            #update pointers
            elif leftA > rightB:
                high = i - 1
            else:
                low = i + 1
















