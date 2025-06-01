## O(n^2) solution but not optimal 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            mul = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                mul *= nums[j] 
            res.append(mul)
        return res
## Here we use prefix to first store the multiple of the index with every previous values in the result list, later we then simply re iterate
## the given list backwards and then multiply it again using the same method thus giving us the required list of products.

## *Noteworthy: We used the default prefix to be 1 and postfix to be 1 as well and basically started multiplying and adding from the 
## second index or second to last for mathematical accuracy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
