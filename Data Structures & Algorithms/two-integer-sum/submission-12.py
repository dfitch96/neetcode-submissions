class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # BRUTE FORCE O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


        difference = {}
        for i in range(len(nums)):
            if target - nums[i] in difference:
                return [difference[target - nums[i]], i]
            else:
                difference[nums[i]] = i









