class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxi = -1
        for i in range(len(arr) - 1, -1, -1):
            oldValue = arr[i]
            arr[i] = maxi
            maxi = max(oldValue,arr[i])
        
        return arr