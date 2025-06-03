## okay I know garbage code but comeon give me a break my head is not working rn anyways O(n^6)...... don't judge... first attempt 

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
