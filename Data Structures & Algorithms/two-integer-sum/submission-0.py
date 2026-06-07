class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for i in range(len(nums)):
            if nums[i] in dct: 
                return [dct[nums[i]], i]
            else:
                dct[target- nums[i]] = i
        return []