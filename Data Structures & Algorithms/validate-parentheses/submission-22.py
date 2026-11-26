class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return False

        kk = []
        for char in s:
            if char in "({[":
                kk.append(char)
            elif char == ")":
                if kk and kk[-1] == "(":
                    kk.pop()
                else:
                    return False
            elif char == "]":
                if kk and kk[-1] == "[":
                    kk.pop()
                else:
                    return False
            elif char == "}":
                if kk and kk[-1] == "{":
                    kk.pop()
                else:
                    return False
            
        return True if not kk else False 


