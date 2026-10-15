class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)):
                temp = arr[j]
                for k in range(j+1, len(arr)):
                    if temp < arr[k]:
                        temp = arr[k]
                break
            arr[i] = temp
        
        arr[len(arr)-2] = arr[len(arr)-1]
        arr[len(arr)-1] = -1
        return arr