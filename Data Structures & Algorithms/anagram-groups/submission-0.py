class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for i in strs:
            if str(sorted(i)) in dct:
                dct[str(sorted(i))].append(i)
            else:
                dct[str(sorted(i))] = [i]
        return list(dct.values())