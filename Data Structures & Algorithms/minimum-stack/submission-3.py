class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append((val, val))
        else:
            curr_min = min(val, self.stk[-1][1])
            self.stk.append((val , curr_min))

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()
        

    def top(self) -> int:
        if self.stk:
            return self.stk[-1][0]
        return -1
        

    def getMin(self) -> int:
        if self.stk:
            return self.stk[-1][1]
        return -1
        
