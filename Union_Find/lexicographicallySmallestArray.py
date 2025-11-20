class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        groups = [] #list of queues so then i can pop the first element
        map_group = {} # num -> group

        #sort nums and create groups:
        sorted_nums = sorted(nums)
        curr_group = deque([sorted_nums[0]])
        i_group = 0
        map_group[sorted_nums[0]] = i_group
        for i in range(1, n):
            if abs(sorted_nums[i] - sorted_nums[i-1]) > limit:
                groups.append(curr_group)
                i_group += 1
                #new group
                curr_group = deque([sorted_nums[i]])
            else:
                curr_group.append(sorted_nums[i])    
            map_group[sorted_nums[i]] = i_group

        #append remaining elements
        groups.append(curr_group)
        for el in curr_group:
            map_group[el] = i_group

        #UNION GROUPS
        #for each group pop the first one
        #retrieve group and then pop element
        res = []
        for el in nums:
            res.append(groups[map_group[el]].popleft())
        return res
        