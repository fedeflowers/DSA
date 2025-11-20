class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        #serve un current e un max, se il current super max, aggiorna
        curr_pos = curr_neg = pos = neg = 0
        #Kedane's algorithm, take min sum and max sum
        #max sum
        for el in nums:
            curr_pos += el
            curr_neg += el
            pos = max(curr_pos, pos, el)
            curr_pos = max(curr_pos, el)
            neg = min(curr_neg, neg, el)
            curr_neg = min(curr_neg, el)

        return max(pos, abs(neg))