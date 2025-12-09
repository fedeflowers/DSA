"""
## Explanation of the Solution

1. **Approach**:
   The solution involves rearranging an array of integers such that positive and negative numbers alternate. The steps are as follows:
   - It first separates the positive and negative numbers from the input list `nums`.
   - It creates two lists: `pos` for positive numbers and `neg` for negative numbers.
   - Both lists are then reversed to facilitate easy popping from the end.
   - The result list `res` is constructed by popping elements alternately from `pos` and `neg` until both lists are empty.
   - Finally, the result list is returned.

   This will result in a reordered array where positive and negative numbers alternate starting with a positive number.

2. **Time and Space Complexity Analysis**:
   - **Time Complexity**: The algorithm processes the list `nums` to separate the positive and negative numbers, which takes O(N) time, where N is the length of `nums`. The while loop also runs O(N) times, since we pop one element from both lists in each iteration. Thus, the overall time complexity is O(N).
   
   - **Space Complexity**: The algorithm uses additional space to store the two lists of positive and negative numbers. In the worst case, if all numbers in `nums` are either positive or negative, the space used will still be O(N). Therefore, the overall space complexity is O(N).

3. **Efficiency of the Approach**:
   This approach is efficient for several reasons:
   - **Simplicity**: It employs straightforward list comprehensions for filtering the numbers, making the code readable and easy to understand.
   - **Use of List Operations**: By utilizing list operations like `pop()`, the algorithm avoids complexity related to index calculations. It can handle the required alternation cleanly without explicitly managing indices.
   - **Direct Alternation**: This method directly manages the arrangement of elements, ensuring that the output meets the specifications (alternating positive and negative numbers).
   - This approach optimally makes use of linear space and time, allowing it to efficiently handle large datasets within the constraints provided by the problem.

Runtime: undefined
Memory: 47764000
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0][::-1]
        neg = [x for x in nums if x < 0][::-1]
        res = []
        while len(pos) > 0 or len(neg) > 0:
            res.append(pos.pop())
            res.append(neg.pop())

        return res
