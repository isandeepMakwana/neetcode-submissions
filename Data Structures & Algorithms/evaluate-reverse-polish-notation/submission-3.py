class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        st = {"*", "-", "+", "/"}

        for i, c in enumerate(tokens):
            if c in st:
                a = stk.pop()
                if c =="*":
                    stk.append(stk.pop() * a)
                elif c=="+":
                    stk.append(stk.pop() + a)
                elif c=="-":
                    stk.append(stk.pop() - a)
                else:
                    stk.append(int(stk.pop() / a))
            else:
                stk.append(int(c))
        
        return int(stk.pop())


        