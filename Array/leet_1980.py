class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        converted = [int(num, 2) for num in nums]

        for i in range(2**len(nums)):
            if i not in converted:
                break
        #adapt to output
        output = bin(i)[2:]
        while len(output) < len(nums):
            output = "0" + output
        return output
        