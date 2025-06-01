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
        
## The optimal solution and here we use an algorithm known as bucket sort, what bucket sort essentially is, is basically creating "buckets" 
## depending on the amount of times a certain number is repeated and labelling the buckets with the amount of times it's repeated and then
## storing the number in that bucket which essentially makes it so that  each number is only stored in a bucket once depending on it's freq
## so we first store the numbers in a dictionary to find the frequency then restore it in the bucket which in this case is "freq" and then 
## iterate through the bucket to append the numbers to our final result array and we can see that there is two loops used however, it still
## maintains the time complexity of O(n) and the reason being that the total amount of numbers is still the same and we are iterating through
## the same n amount of numbers as we did before and are only appending the numbers n amount of times as well. This is something known as
## an "amortized analysis"


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            storage[i] = 1 + storage.get(i, 0)
        for n,c in storage.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
