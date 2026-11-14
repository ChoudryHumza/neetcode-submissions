class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        zero = 0
        twos = len(nums)-1
  
        i =0
        while i <= twos:
            if i<=twos:
                if nums[i] == 0:
                    temp = nums[zero]
                    nums[zero] = 0
                    nums[i] = temp
                    zero +=1
                elif nums[i] == 2:
                    temp = nums[twos]
                    nums[twos] = 2
                    nums[i] = temp
                    i -=1
                    twos-=1
                i+=1
