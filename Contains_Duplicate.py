class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s1 = set(nums)
        if len(s1) == len(nums):
            return False
        else:
            return True
