class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        if len(s) < 2:
            return
        else: 
            k = len(s)-1
            for i in range(len(s)):
                if i < k:
                    temp = s[k]
                    s[k] = s[i]
                    s[i] = temp 
                    i+=1
                    k-=1
                else:
                    break
        