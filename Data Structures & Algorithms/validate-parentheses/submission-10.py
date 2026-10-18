class Solution:
    def isValid(self, s: str) -> bool:
        open_parentheses = []

        if len(s) <= 1:
            return False
        else:
            for char in s:
                if char in ["[", "(", "{"]:
                    open_parentheses.append(char)
                else:
                    if char == "]":
                        if not open_parentheses or open_parentheses[-1] != "[":
                            return False
                        else:
                            open_parentheses.pop()
                    elif char == "}":
                        if not open_parentheses or open_parentheses[-1] != "{":
                            return False
                        else:
                            open_parentheses.pop()
                    elif char == ")":
                        if not open_parentheses or open_parentheses[-1] != "(":
                            return False
                        else:
                            open_parentheses.pop()
        
        if not open_parentheses:
            return True
        else:
            print (open_parentheses)
            return False