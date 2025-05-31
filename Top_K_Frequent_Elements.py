## First solution which is very inefficient in terms of time complexity but the easiest one I could come up with in the shortest amount of time
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage = {}
        for i in nums:
            if i not in storage:
                storage[i] = 1
            else:
                storage[i] += 1
        ans = []
        count = 0
        while count != k:
            max = 0
            for i,j in storage.items():
                if j > max and j not in ans:
                    max = i
            ans.append(max)
            count += 1
        return ans
