"""
# Explanation of the LeetCode Solution for "Add Two Numbers"

## 1. Approach

The problem involves adding two numbers represented as linked lists, where each node contains a single digit in reverse order. The approach taken in this solution can be summarized as follows:

- **Initialization**: A dummy node (`res`) is created to start building the resulting linked list. The `curr` pointer is used to navigate and append new nodes.
  
- **Main Loop**: The algorithm loops through both linked lists (`l1` and `l2`) as long as there are remaining digits in either list or there is a carry-over from the last addition:
  - **Extract Values**: For each iteration, the values of the current nodes from `l1` and `l2` are extracted. If either list has been fully traversed, its value is treated as `0`.
  - **Calculate New Value**: The sum of the current digits and any carry from the last iteration is calculated. The carry for the next iteration is determined using integer division (`// 10`), and the current digit to store is found using the modulus operator (`% 10`).
  - **Add New Node**: A new node containing the resulting digit is created and attached to the result linked list.
  - **Move Pointers**: The pointers for the result linked list and the input lists are updated accordingly.

- **Return Result**: Finally, the method returns the next node of the dummy head (which points to the actual start of the result linked list).

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(max(N, M))
  - Here, N is the number of nodes in `l1`, and M is the number of nodes in `l2`. The loop iterates through the longer of the two lists, processing each node once.

- **Space Complexity**: O(max(N, M))
  - The space complexity is primarily for storing the resulting linked list, which, in the worst case, will have a length of one more than the longer list.

## 3. Why This Approach is Efficient

This approach is efficient for a few reasons:

- **Single Pass**: The algorithm executes in a single pass through both linked lists, making it optimal in terms of time complexity as it only requires linear time proportional to the length of the longer linked list.
  
- **Minimal Overhead**: The use of a dummy node simplifies handling of edge cases (like leading zeros and empty lists) without needing additional checks or complexity.

- **Direct Manipulation**: By directly manipulating the linked list nodes, we avoid the need for conversion to and from integers, which could cause overflow issues and would be less efficient.

In summary, this solution provides a clean, efficient, and clear way to solve the problem of adding two numbers represented as linked lists, leveraging careful handling of carry and node manipulation.

Runtime: undefined
Memory: 17444000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        curr = res
        res.next = curr
        carry = 0
        while l1 or l2 or carry != 0:
            first = 0
            second = 0
            if l1:
                first = l1.val
                l1 = l1.next
            if l2:
                second = l2.val
                l2 = l2.next

            new_val = first + second + carry
            carry = new_val // 10
            new_node = ListNode(new_val % 10)
            curr.next = new_node
            curr = curr.next


        return res.next
