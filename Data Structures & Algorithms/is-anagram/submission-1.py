from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = dict(Counter(s))
        for i in t:
            if i in s_counter:
                s_counter[i] -=1
            else:
                return False
        
        for val in s_counter.values():
            if val > 0:
                return False
        return True


