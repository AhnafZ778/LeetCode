## Very basic stack code we use a dictionary to store the closing bracket and corresponding open ones as values, if it matches we check if the last bracket appended corresponds to it's 
## respective bracket in the dictionary if it doesn't we return false else we simply pop the last index of the stack and continue the loop

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d1 = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in d1:
                if stack and (stack[-1] == d1[i]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True
