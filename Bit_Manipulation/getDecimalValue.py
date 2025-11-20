# Convert_Binary_Number_in_a_Linked_List_to_Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # number = []
        # curr = head
        # while curr:
        #     number.append(curr.val)
        #     curr = curr.next

        # val = 0
        # n = len(number)
        # for i in range(n):
        #     if number[i]:
        #         val += pow(2, n-i-1) 

        # return val

        curr = head
        res = 0
        #O(1) mem
        while curr:
            res = res << 1
            res |= curr.val
            curr = curr.next

        return res

        