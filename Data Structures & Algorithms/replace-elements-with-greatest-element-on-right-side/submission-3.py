class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = [0] * (len(arr) + 1)
        temp[-1] = -1
        for i in range(len(arr)-1, -1,-1):
            rightmax = max(temp[i+1], arr[i])
            temp[i] = rightmax
        temp.pop(0)
        return temp