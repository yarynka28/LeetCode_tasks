class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(len(nums)):
            if nums[num]+nums[num+1] == target:
                return [num, num+1]
              
