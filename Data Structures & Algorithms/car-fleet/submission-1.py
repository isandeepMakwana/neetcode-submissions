class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(i, j) for i, j in zip(position , speed)]
        ps.sort(key=lambda x: -x[0])
        stk =[]
        for car in ps:
            if stk and stk[-1] >= (target - car[0])/car[1]:
                continue
            stk.append((target - car[0])/car[1])
        return len(stk)
