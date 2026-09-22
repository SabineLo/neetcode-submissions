class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in numsDict:
                return [numsDict[diff],index]
            else:
                numsDict[num] = index
        
