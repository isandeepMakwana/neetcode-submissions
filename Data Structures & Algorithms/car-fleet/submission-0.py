class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(i, j) for i, j in zip(position , speed)]
        ps.sort(key=lambda x: -x[0])
        stk =[]
        for car in ps:
            stk.append((target - car[0])/car[1])
            if len(stk) >=2 and stk[-1] <= stk[-2]:
                stk.pop()

        return len(stk)
