class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stk = []

        for i, tmp in enumerate(temperatures):
            
            while stk and stk[-1][0] < tmp:
                ele, idx = stk.pop()
                ans[idx] = i-idx

            stk.append((tmp, i))
        return ans



