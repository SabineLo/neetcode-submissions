class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numPos = {}

        for i, n in enumerate(nums):
            value = target - n
            if value in numPos:
                return [numPos[value], i]
            numPos[n] = i

