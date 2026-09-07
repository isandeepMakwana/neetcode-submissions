from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        window = Counter(s2[:len(s1)])
        left =0

        if target == window:
            return True

        for r in range(len(s1), len(s2)):
            if target == window:
                return True
            window[s2[r]] +=1

            while (r - left + 1) > len(s1):
                window[s2[left]] -=1

                if window[s2[left]] <=0:
                    del window[s2[left]]
                left +=1

                if target==window:
                    return True
        return False