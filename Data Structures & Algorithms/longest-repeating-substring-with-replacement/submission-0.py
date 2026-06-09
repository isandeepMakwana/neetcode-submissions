class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = ans = 0
        counter = {}
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1

            while (r-l+1) - max(counter.values()) > k:
                if counter.get(s[l]) > 0:
                    counter[s[l]] -=1
                l+=1
            
            ans = max(ans, (r-l+1))
        return ans
