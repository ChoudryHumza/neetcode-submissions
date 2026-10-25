class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = [0] * (2 * len(nums))
        index2 = len(nums)
        for i in range(len(nums)):
            nums2[i] = nums[i]
            nums2[index2] = nums[i]
            index2 +=1
        
        return nums2