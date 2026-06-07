class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[n-i-1] = suffix[n-i] * nums[n-i]

        return [i*j for i, j in zip(prefix, suffix)] 



