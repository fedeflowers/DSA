"""
```markdown
# Explanation of the LeetCode Solution for "Add Two Numbers"

## 1. Brief Explanation of the Approach

The problem "Add Two Numbers" involves adding two numbers represented as linked lists, where each node contains a digit, and the digits are stored in reverse order. The proposed solution uses a while loop to traverse both linked lists simultaneously and perform the addition. Here’s a step-by-step breakdown of the approach:

- Two pointers, `curr_l1` and `curr_l2`, are initialized to the head of each linked list (`l1` and `l2` respectively).
- A `carry` variable is used to keep track of any value that needs to be carried over when the sum of two digits exceeds 9.
- A dummy node `dummy` is created to facilitate easy list construction, with a head pointer pointing to this dummy node (`head`).
- Inside the loop, we check if either list `curr_l1` or `curr_l2` has remaining nodes. If they do, we retrieve the current digit; if not, we use 0.
- The current digits along with the `carry` are summed. The new digit to place into the result linked list is obtained using `summ % 10`, and `carry` is updated using `summ // 10`.
- A new ListNode is created with the computed digit and attached to the result linked list.
- The pointers `curr_l1` and `curr_l2` are advanced to their respective next nodes if they exist.
- The loop continues until both lists have been fully traversed and there’s no carry left.
- Finally, the function returns the node following the dummy head, which contains the resulting linked list.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(max(N, M)), where N is the length of the first linked list and M is the length of the second linked list. We go through both linked lists once.
  
- **Space Complexity**: O(max(N, M)), as in the worst case (if the result has the maximum possible number of nodes), we have to store the sum of the two lists in a new linked list.

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **One Pass Addition**: The algorithm processes each node of the linked lists only once, which is optimal for a problem involving linked lists.
  
- **Handles Various Lengths**: It efficiently deals with linked lists of different lengths and also accounts for any carry value from the summation.
  
- **Constant Space for Output**: The solution generates the output list dynamically, ensuring that we only use additional space proportional to the result size, rather than pre-allocating large arrays.

Overall, this method neatly ties together traversal, digit addition, and carry handling into an elegant solution for the problem posed by adding two numbers represented as linked lists.
```

Runtime: undefined
Memory: 18028000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = l1
        curr_l2 = l2
        carry = 0
        dummy = head = ListNode(-1)
        while curr_l1 or curr_l2 or carry:
            if curr_l1: 
                num1 = curr_l1.val 
            else:
                num1 = 0
            if curr_l2: 
                num2 = curr_l2.val 
            else:
                num2 = 0

            summ = num1 + num2 + carry 
            carry = summ//10

            dummy.next = ListNode(summ % 10)

            if curr_l1:
                curr_l1 = curr_l1.next
            if curr_l2:
                curr_l2 = curr_l2.next

            dummy = dummy.next



        return head.next
