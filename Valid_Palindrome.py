## Pretty basic code, however apparently due to usage of a string and as string is immutable it is having to traverse the string while also traversing
## the loop hence the time complexity becomes O(n^2)

## In Python as strings are immutable what it basically does is creates a whole another string whenever you use "+=" function to store it so basically having O(n) time complexity while
## also not being being very space friendly for obvious reasons
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
## Nothing changed except I'm storing them in a list and later joining it all using .join() function which reduces the time complexity to O(n) from O(n^2)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        count = 0
        store = []
        for i in s:
            if "A" <= i <= "Z" or "a" <= i <= "z":
                store += i.lower()
            elif "0" <= i <= "9":
                store += i
        store = "".join(store)
        while count != len(store)//2:
            if store[count] != store[len(store)-count-1]:
                return False
            count += 1
        return True
