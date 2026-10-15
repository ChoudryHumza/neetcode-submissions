class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutiveOnes = 0
        storageOfConsecutiveOnes = []
        for num in nums:
            if num == 1:
                consecutiveOnes+=1
            else:
                storageOfConsecutiveOnes.append(consecutiveOnes)
                consecutiveOnes = 0
        
        storageOfConsecutiveOnes.append(consecutiveOnes)
        return max(storageOfConsecutiveOnes)

