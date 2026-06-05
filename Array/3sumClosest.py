"""
# Explanation of the 3Sum Closest Solution

## 1. Approach

The given solution utilizes a two-pointer technique after sorting the input list `nums`. The main goal is to find the sum of any three distinct integers in `nums` that is closest to a specified `target`. Here’s a brief step-by-step explanation of how the algorithm works:

- **Sorting:** First, the input list `nums` is sorted to facilitate the two-pointer approach.
  
- **Iterating through elements:** The solution iterates through the list with an index `i`, which represents the first element of the triplet. The loop runs until `l-2` to ensure there are at least two more elements to consider for the triplet.

- **Two-pointer technique:** For each selected element (indexed by `i`), two pointers `s` (start) and `r` (right) are initialized. `s` starts just after `i` and `r` starts at the end of the list. The pointers help in determining the other two elements of the triplet.

- **Calculating the sum:** Inside the inner while loop, the sum `curr_sum` of the triplet formed by elements at indices `s`, `r`, and `i` is calculated.

- **Checking and updating closest sum:** If `curr_sum` equals `target`, the function immediately returns `target` as the closest sum. If `curr_sum` is less than `target`, the left pointer `s` is incremented to increase the sum. If it is greater, the right pointer `r` is decremented to decrease the sum. After each calculation, the algorithm checks if the current sum is closer to the target than previously found sums, updating `closest` and `best_candidate` as necessary.

- **Returning the best candidate:** After all iterations, the function returns the `best_candidate`, which is the sum closest to the target.

## 2. Time and Space Complexity

- **Time Complexity:** The time complexity of this solution is \(O(N^2)\), where \(N\) is the number of elements in the input list `nums`. This complexity arises because for each element (for loop iterating over \(N\)), the two-pointer technique involves scanning the remaining elements roughly in linear time (in the worst case).

- **Space Complexity:** The space complexity is \(O(1)\) since the algorithm only uses a constant amount of extra space (for variables like `closest`, `best_candidate`, and indices).

## 3. Efficiency of the Approach

This approach is efficient mainly due to two reasons:

1. **Sorting and Two-Pointer Method:** Sorting the input list takes \(O(N \log N)\), but the use of the two-pointer technique ensures that each additional element results in a linear search among the rest of the elements, leading to an overall quadratic time complexity. This is considerably less computationally expensive than a brute-force solution that would require checking all combinations of triplets.

2. **Early Exit:** The algorithm has an early exit condition when it finds an exact match (i.e., `curr_sum == target`), which minimizes unnecessary computations.

This leads to a balanced trade-off between simplicity and performance, making the algorithm efficient for solving the problem as intended.

Runtime: undefined
Memory: 19496000
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        closest = float("inf")
        best_candidate = float("inf")
        for i in range(l-2):
            s = i + 1
            r = l - 1
            while s < r :
                curr_sum = nums[s] + nums[r] + nums[i]
                if curr_sum == target:
                    return target
                elif curr_sum < target:
                    s += 1
                elif curr_sum > target:
                    r -= 1

                if abs(target - curr_sum) < closest:
                    closest = abs(target - curr_sum)
                    best_candidate = curr_sum

        return best_candidate
