class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k = len(nums)
        nums2 = [0] * 2 * len(nums)
        for i in range(len(nums)):
            nums2[i] = nums[i]
            nums2[k] = nums[i]
            k+=1
        return nums2