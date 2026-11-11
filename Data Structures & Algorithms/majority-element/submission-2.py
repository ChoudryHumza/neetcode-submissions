class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nTimes = len(nums) // 2
        n = Counter(nums)
        for num, count in n.items():
            if count > nTimes:
                return num
        