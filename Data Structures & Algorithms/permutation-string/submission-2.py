from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s_cnt = Counter(s1)
        l = 0
        for r in range(len(s1)-1, len(s2)):
            if (r-l+1) < len(s1):
                continue
            curr = Counter(s2[l:r+1])
            if curr == s_cnt:
                return True

            while (r-l+1) >=len(s1):
                l+=1

        return False
            

