class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        n = len(nums)
        good_pairs = 0
        for i, el in enumerate(nums):
            good_pairs += freq[el-i]
            freq[el -i] += 1

        return (n * (n-1) )// 2 - good_pairs
