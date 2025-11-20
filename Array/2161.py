class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        center = []
        for el in nums:
            if el < pivot:
                left.append(el)
            elif el == pivot:
                center.append(el)
            else:
                right.append(el)

        return left + center + right