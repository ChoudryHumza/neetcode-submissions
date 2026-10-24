class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        current = 0
        max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current+=1
            else:
                current = 0
            
            if max < current:
                max = current
        return max
