class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #of all the numbers {}
        numberDict = {}

        #enumerate gets me the index and the number value
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numberDict:
                return [numberDict[diff], i]
            numberDict[n] = i
        return []