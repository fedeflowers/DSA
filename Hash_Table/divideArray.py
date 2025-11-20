class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hs_map = {}
        for el in nums:
            hs_map[el] = hs_map.get(el, 0) + 1

        for el in hs_map:
            if hs_map[el] % 2 != 0:
                return False

        return True
        