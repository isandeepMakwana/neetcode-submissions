class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stk = []

        for i, h in enumerate(heights):
            idx = i
            while stk and stk[-1][0] > h:
                ele, index = stk.pop()
                ans = max(ans, ele * (i-index))
                idx = index
            stk.append((h, idx))
        
        while stk:
            ele, index = stk.pop()
            ans = max(ans, ele * (len(heights)-index))
        
        return ans