from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        window, tcount = {}, dict(Counter(t))
        have , need = 0, len(tcount.keys())
        ans , anslen = [-1,-1], float("inf")

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in tcount and tcount[s[r]] == window[s[r]]:
                have +=1
            print(window, have, need)
            while have == need:
                if (r-l+1) < anslen:
                    ans = [l, r]
                    anslen = (r - l+1)
                
                if s[l] in tcount and tcount[s[l]] == window[s[l]]:
                    have -=1
                window[s[l]] -=1
                l+=1
        l, r = ans
        return s[l: r+1] if anslen != float("inf") else ""
            





        

            
        