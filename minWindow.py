## My first Hard problem and I solved it without needing to look at any solutions only needed an explanation on how to solve it and did it
## Kind proud of myself ngl

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1, d2 = {} , {}
        for i in t:
            d1[i] = d1.get(i,0) + 1

        have = 0
        need = len(d1)
        res = len(s)
        rs = ""

        l = 0
        for r in range(len(s)):
            if s[r] in d1:  
                d2[s[r]] = d2.get(s[r], 0) + 1
                if d2[s[r]] == d1[s[r]]:
                    have += 1
            while have == need:
                if res >= r - l + 1:
                    res = min(res, r-l+1)
                    rs = s[l:r+1]
                if s[l] in d2:
                    d2[s[l]] -= 1
                    if d2[s[l]] < d1[s[l]]:
                        have -= 1
                l += 1
        return rs
