class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            '}' :'{',
            ']':'[',
            ')': '('
        }
        st = []
        for c in s:
            if c not in mp:
                st.append(c)
            else:
                if st and st[-1] == mp[c]:
                    st.pop()
                else:
                    return False
        return not st





