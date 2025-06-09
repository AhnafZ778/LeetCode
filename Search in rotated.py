## Binary Search

## Scope is a very important thing to remember for this problem
## if the target is smaller than the smallest in the sequence then
## it's outside the scope of the smallest and then if the target is 
## also bigger than the biggest number of sequence which let's say is 
## the middle one if left to mid is a ordered sequence then it's outside
## the scope of the biggest number in the sequence too. in this case
## it can only be found to the right of the sequence
## now the same can be said if left to middle is not an ordered sequence


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            
            if nums[m] >= nums[l]:
                if nums[l] > target or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[r] < target or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
