## first attempt 

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
      res = []
      for i in range(len(nums)-2):
          for j in range(i+1, len(nums)-1):
              for k in range(j+1, len(nums)):
                  if nums[i] + nums[j] + nums[k] == 0:
                      l1 = []
                      l1.append(nums[i])
                      l1.append(nums[j])
                      l1.append(nums[k])
                      l1.sort()
                      if l1 not in res:
                          res.append(l1)      
      return res
## I pray for your eyes

## This is the optimal solution O(n^2) here we basically use two pointers while keeping a pointer at the start and iterating slowly from the start, while doing so we use two pointers one
## from the immediate next index of current one and the other from the last, everything else is pretty standard 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            l,r = i + 1, len(nums)-1
            while l < r:
                if a + nums[l] + nums[r] > 0:
                    r -= 1
                elif a + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    if [a,nums[l],nums[r]] not in res:
                        res.append([a, nums[l], nums[r]])
                    l += 1
        return res
