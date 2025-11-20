# Problem: 3Sum
# Link: https://leetcode.com/problems/3sum/

def threeSum(nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        left, right = i+1, n-1

        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return result