class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] not in ["+", "C", "D"]:
                stack.append(int(operations[i]))
            elif operations[i] == "+":
                num1 = stack.pop()
                add = num1 + stack[-1]
                stack.append(num1)
                stack.append(add)
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                multiply = 2 * stack[-1]
                stack.append(multiply)
        
        total = 0
        for i in range(len(stack)):
            total += int(stack.pop())
        
        return total