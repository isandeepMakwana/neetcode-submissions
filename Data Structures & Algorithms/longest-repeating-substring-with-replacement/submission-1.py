class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = ans = curr = 0
        arr = [0] * 26

        for r in range(len(s)):
            curr = ord(s[r]) - ord('A')
            arr[curr] +=1
            while sum(arr)-max(arr) > k:
                arr[ord(s[left]) - ord('A')] -=1
                left +=1
            # print(sum(arr), arr, k, sum(arr)-max(arr))
            ans = max(ans, sum(arr))    
        
        return ans