class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        #grouping
        groups = defaultdict(lambda: [-1, -1])
        for el in nums:
            digits_sum = 0
            for c in str(el):
                digits_sum += int(c)
            
            max1, max2 = groups[digits_sum]
            if el > max1:
                groups[digits_sum] = [el, max1]
            elif el > max2:
                groups[digits_sum][1] = el
        res = -1

        for g in groups:
            max1, max2 = groups[g]
            if max2 > -1:
                res = max(res, max1+  max2)
        return res 