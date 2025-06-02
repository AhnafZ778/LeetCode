## Here the concept is pretty straight forward the easy approaches are obviously either a nested loop or using sort() function however these are O(n^2) and O(nlogn) respectively which isn't  
## the best case, so for the best case we can use a set and then traverse the given list and check if the (current num - 1) exists in the set this basically means we will check if the current
## number is the beginning of the consecutive number chain or not. Once we know that it is then we set the length at 1 and then use a while loop to continuously increase the current number
## and checking if it exists in the set this eventually gives us the length of the chain. and as this is a set and not a normal list the time complexity remains O(n) instead of O(n^2) as 
## it is a hash-map

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        maxi = 0
        for i in num:
            if i-1 not in num:
                length = 1
                while (i + length) in num:
                    length += 1
            if length > maxi:
                maxi = length
        return maxi
