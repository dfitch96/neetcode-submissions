class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = nums.count(val)
        end = len(nums) - 1
        for i in range(len(nums) - k):
            if nums[i] == val:
                while nums[end] == val:
                    end -= 1
                nums[i], nums[end] = nums[end], nums[i]

            

        return len(nums) - k

        