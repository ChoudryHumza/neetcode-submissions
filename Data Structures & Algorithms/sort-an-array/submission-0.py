class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        for i in range(len(nums)):
            minVal = nums[i]
            index = i
            for j in range(1+i, len(nums)):
                if minVal < nums[j]:
                    continue
                else:
                    minVal = nums[j]
                    index = j   
            temp = nums[i]
            nums[i] = minVal
            nums[index] = temp
        return nums