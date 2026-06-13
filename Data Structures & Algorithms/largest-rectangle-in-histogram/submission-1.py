class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stk = []

        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][0] > h:
                ele, idx = stk.pop()
                ans = max(ans, ele * (i-idx))
                start = idx
            stk.append((h, start))
        
        while stk:
            ele, index = stk.pop()
            ans = max(ans, ele * (len(heights)-index))
        
        return ans