class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                for j in range(i+1, len(nums)):
                    if nums[j] != val:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break 
        return len(nums) - nums.count(val)
