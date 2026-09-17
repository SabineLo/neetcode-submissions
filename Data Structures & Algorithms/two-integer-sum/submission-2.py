class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We want to return smaller index first
        #We want to have a dictonary that stores the number,index
        values = {}

        for i, n in enumerate(nums):
            pastValue = target - n # n + pastValue = target
            if pastValue in values:
                return [values[pastValue],i]
            values[n] = i    