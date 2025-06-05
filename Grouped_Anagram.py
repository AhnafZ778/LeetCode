class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
## Lol I tried to recap the codes I previously did and turns out I kept a suboptimal solution here O(n*mlogm) because sorted is used

## This is the corrent solution with time complexity O(n*m)

## ** Very important thing I learned, you can't store anything mutable inside a dictionary as a key so here I turned it into a tuple which
## is immutable otherwise the code was not working


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = {}
        for i in strs:
            arr = [0]*26
            for j in i:
                arr[ord(j) - ord("a")] += 1
            key = tuple(arr)
            if key not in d1:
                d1[key] = [i]
            else:
                d1[key].append(i)
