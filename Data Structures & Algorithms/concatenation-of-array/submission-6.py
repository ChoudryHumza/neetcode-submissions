class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        k = 0
        n = [0] * 2 * len(nums)
        for i in range(len(nums)):
            n[i] = nums[i]
            n[i+len(nums)] = nums[i]
        return n