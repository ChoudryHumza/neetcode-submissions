class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashed = Counter(nums)
        for key, value in hashed.items():
            if value > len(nums) / 2:
                return key
        