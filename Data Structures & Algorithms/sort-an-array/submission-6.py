class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    
    def merge_sort(self, nums, l, r):
        if r <= l:
            return 

        middle = (r + l) // 2
        self.merge_sort(nums, l, middle)
        self.merge_sort(nums, middle + 1, r)
        self.merge(nums, l, r)

        
     
    

    def merge(self, nums, l, r):
        middle = (l + r) // 2

        temp = []
        left, right = l, middle + 1

        while left <= middle and right <= r:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while left <= middle:
            temp.append(nums[left])
            left += 1

        while right <= r:
            temp.append(nums[right])
            right += 1
        
        for i in range(len(temp)):
            nums[l + i] = temp[i]
        

