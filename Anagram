class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        d1 , d2 = {}, {}

        for i in range(len(s)):
            d1[s[i]] = 1 + d1.get(s[i], 0)
            d2[t[i]] = 1 + d2.get(t[i], 0)
        for c in d1:
            if d1[c] != d2.get(c, 0):
                return False
        return True
