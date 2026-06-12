class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        st = {"*", "-", "+", "/"}

        for i, c in enumerate(tokens):
            if c in st:
                s2 = stk.pop()
                s1 = stk.pop()
                ans = s1+c+s2
                stk.append(str(int(eval(ans))))
            else:
                stk.append(c)
        
        return int(stk.pop())


        