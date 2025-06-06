## Set apparently has a function of .remove and .add to get rid and add data
## Other than that it's a pretty basic sliding window except. The r instead of
## increasing using a while loop increments using for loop contrary to the 
## question I solved previously

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset= set()
        l = 0
        res = 0
        for r in range(len(s)): 
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r-l+1)
        return res
