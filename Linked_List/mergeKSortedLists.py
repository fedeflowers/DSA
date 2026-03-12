"""
## Explanation of the Approach

This solution uses a divide-and-conquer strategy to merge `k` sorted linked lists into one sorted linked list. The key components of the approach are:

1. **Merge Function (`merge2`)**: This function takes two sorted linked lists and merges them into a single sorted linked list. It traverses both lists simultaneously, adding the smaller of the two current nodes to the result list, until one of the lists is exhausted. If one list still has remaining elements, it appends them to the end of the result.

2. **Merge Sort Function (`mergesort`)**: This function recursively divides the list of linked lists into smaller groups until it reaches base cases where the number of lists is 0 or 1. It then calls the `merge2` function to merge the results from the left and right halves.

3. **Main Function**: The main function checks if the input list is empty and calls the `mergesort` function to initiate the merging process. It returns the head of the merged sorted linked list.

By recursively dividing the problem and merging the results, this implementation achieves an efficient merge of multiple sorted lists.

## Time and Space Complexity Analysis

1. **Time Complexity**:
   - Merging two sorted linked lists takes O(N) time, where N is the total number of nodes in both lists.
   - The overall time complexity is O(N log k) for merging `k` lists, where N is the total number of nodes across all lists. This is because we are dividing the list of `k` linked lists using a merge sort approach, which takes O(log k) divisions.

2. **Space Complexity**:
   - The space complexity is O(1) for the merging process since we are reorganizing the nodes in place and do not allocate additional memory proportional to the input size. However, in function call stack space for recursion, it could be noted as O(log k).

## Why This Approach is Efficient

This approach is efficient due to several reasons:

1. **Divide-and-Conquer**: By leveraging the divide-and-conquer strategy, the solution efficiently reduces the number of lists to merge at each step. This reduces the potential overhead of merging all lists at once.

2. **Adaptive Merging**: Merging sorted lists is inherently efficient, as only linear time is needed for merging once the lists are divided, keeping the operation time manageable even with a higher number of lists.

3. **In-Place Merging**: The `merge2` function constructs the merged list without requiring additional data structures (like arrays or custom nodes), resulting in lower space usage compared to other methods that might store all values before merging.

Overall, this efficient use of merging and recursive division leads to a solution that is well-suited for handling multiple sorted linked lists.

Runtime: undefined
Memory: 22596000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # res = curr = ListNode()
        # values = []
        # for l in lists:
        #     while l:
        #         values.append(l.val)
        #         l = l.next

        # values.sort() #N log N
        # for v in values:
        #     curr.next = ListNode(v)
        #     curr = curr.next

        # return res.next

        #optimize memory
        # merge 2 sorted lists
        def merge2(a, b):
            curr_a = a
            curr_b = b
            res = curr_res = ListNode()
            while curr_a and curr_b:
                if curr_a.val < curr_b.val:
                    curr_res.next = curr_a
                    curr_a = curr_a.next
                else:
                    curr_res.next = curr_b
                    curr_b = curr_b.next
                curr_res = curr_res.next


            if curr_a:
                curr_res.next = curr_a
            else:
                curr_res.next = curr_b

            return res.next
        
        def mergesort(lists):
            if len(lists) <=1:
                return lists[0]

            middle = len(lists) //2
            left = mergesort(lists[:middle])
            right = mergesort(lists[middle:])
            return merge2(left, right)
        
        if not lists:
            return None

        return mergesort(lists)


            
                    
                
