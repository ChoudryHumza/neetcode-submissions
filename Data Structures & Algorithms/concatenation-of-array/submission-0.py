class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        nums.extend(nums)
        return nums

        


