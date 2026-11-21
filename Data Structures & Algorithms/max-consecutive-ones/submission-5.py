class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current +=1
            elif nums[i] == 0:
                current = 0
            maxi = max(maxi, current)

        return maxi
