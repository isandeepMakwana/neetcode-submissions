class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set([])
        mx_len = 0

        left =0 
        for i, right in enumerate(s):
            
            while right in sett:
                sett.remove(s[left])
                left +=1
            
            sett.add(right)
            mx_len = max(mx_len, len(sett))

        return mx_len