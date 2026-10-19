class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) < 2:
            return False

        stack = []
        for char in s:
            if char in ["{", "[", "("]:
                stack.append(char)
            elif char in ["}", "]", ")"]:
                if not stack:
                    return False
                else:
                    if char == "}" and stack[-1] == "{":
                        stack.pop()
                    elif char == "]" and stack[-1] == "[":
                        stack.pop()
                    elif char == ")" and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
        
        if not stack:
            return True
        else:
            return False