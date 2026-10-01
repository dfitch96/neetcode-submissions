class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffs = {}

        i = 0 
        while i < len(nums):
            if target - nums[i] in diffs:
                return [diffs[target - nums[i]], i]
            else:
                diffs[nums[i]] = i
            i += 1

        return []