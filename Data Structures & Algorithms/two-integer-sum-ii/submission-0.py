class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while (left < right):
            sm = nums[left] + nums[right]
            if sm == target:
                return [left+1, right+1]
            if sm > target : 
                right -=1
            else:
                left +=1
        
        return [left+1, right+1]