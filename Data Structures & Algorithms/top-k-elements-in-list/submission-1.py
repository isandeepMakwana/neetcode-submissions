from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)        
        lst = list(counter.items())
        lst.sort(key = lambda x: x[1])

        return [i[0] for i in lst[-k:]]