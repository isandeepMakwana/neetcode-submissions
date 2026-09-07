class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1 = sorted(s1)
        
        for r in range(len(s1), len(s2)+1):
            # print(s2[left : r])
            if s1 == sorted(s2[left : r]):
                return True
            
            while (r - left + 1) > len(s1):
                left +=1
            
        return False
