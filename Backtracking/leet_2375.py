class Solution:
    def smallestNumber(self, pattern: str) -> str:
        nums = [str(i) for i in range(1, 10)]

        def build(start, pattern, index, nums):
            if index == len(pattern):
                return start

            for i in range(len(nums)):
                if pattern[index] == 'I':
                    if nums[i] > start[index]:
                        res = build(start + nums[i], pattern, index+1, nums[:i] + nums[i+1:])
                        if res:
                            return res
                else:
                    if nums[i] < start[index]:
                        res = build(start + nums[i], pattern, index+1, nums[:i] + nums[i+1:])
                        if res:
                            return res
        
        for i in range(len(nums)):
            res = build(nums[i], pattern, 0, nums[:i] + nums[i+1:])
            if res:
                return res