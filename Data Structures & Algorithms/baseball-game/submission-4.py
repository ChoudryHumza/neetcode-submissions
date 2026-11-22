class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        arr = []
        for s in operations:
            if s == "+":
                arr.append(arr[-1] + arr[-2])
            elif s == "D":
                arr.append(arr[-1]*2)
            elif s == "C":
                arr.pop()
            else:
                arr.append(int(s)) 
        return sum(arr)