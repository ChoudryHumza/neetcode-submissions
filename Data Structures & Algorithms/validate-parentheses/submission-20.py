class Solution:
    def isValid(self, s: str) -> bool:
        openBracket = []
        closedBracket = []
        if len(s) < 2:
            return False

        for char in s:
            if char in "([{":
                openBracket.append(char)
            elif char == '}':
                if len(openBracket) != 0 and openBracket[-1] == '{':
                    openBracket.pop()
                else:
                    return False
            elif char == ']':
                if len(openBracket) != 0 and openBracket[-1] == '[':
                    openBracket.pop()
                else:
                    return False
            elif char == ')':
                if len(openBracket) != 0 and openBracket[-1] == '(':
                    openBracket.pop()
                else:
                    return False
        
        return True if len(openBracket) == 0 else False
