## First attempt, time complexity of O(n^2) where n is length of input string

class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += i
            s += " "
        return s
    def decode(self, s: str) -> List[str]:
        res = []
        s1 = ""
        for i in s:
            if i == " ":
                res.append(s1)
                s1 = ""
            else:
                s1 += i
        return res
## Though accepted it is fundamentally wrong as we never know what string could be passed to encode or decode, I assumed space to be a valid
## separator however, that is not always going to be the case and sometimes if space is passed in a string then the code will not work as 
## intended



## This is the actual O(n) solution, here again the second while loop doesn't make it O(n^2) still as we are still only iterating over an 
## index only once, while also appending only once all together and no index is being overlapped

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:(j+1+length)])
            i = j + 1 + length
        return res
