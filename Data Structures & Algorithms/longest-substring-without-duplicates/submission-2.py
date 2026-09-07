class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = curr = 0
        sett = set([])
        for right in range(len(s)):
            curr = s[right]
            while curr in sett and left < len(s):
                sett.remove(s[left])
                left +=1
            sett.add(curr)
            ans = max(ans , len(sett))

        return ans                