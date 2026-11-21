class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        length = len(nums)
        l = 0 
        r = length - 1
        
        while l <= r and nums:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1