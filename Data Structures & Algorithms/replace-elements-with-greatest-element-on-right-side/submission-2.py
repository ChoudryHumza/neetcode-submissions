class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = [0] * len(arr)
        temp[-1] = -1
        for i in range(len(temp)-2, -1,-1):
            rightmax = max(temp[i+1], arr[i+1])
            temp[i] = rightmax
        return temp