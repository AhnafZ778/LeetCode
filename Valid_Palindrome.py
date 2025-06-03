## Pretty basic code
class Solution:
    def isPalindrome(self, s: str) -> bool:
        count = 0
        store = ""
        for i in s:
            if "A" <= i <= "Z" or "a" <= i <= "z":
                store += i.lower()
            elif "0" <= i <= "9":
                store += i
        while count != len(store)//2:
            if store[count] != store[len(store)-count-1]:
                return False
            count += 1
        return True
