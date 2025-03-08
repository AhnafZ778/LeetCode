class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x[-1::-1] == x:
            return True
        else:
            return False
