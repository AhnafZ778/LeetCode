class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(len(nums)):
            if target - nums[i] in dict1:
                return i, dict1[target- nums[i]]
            else:
                dict1[nums[i]] = i
