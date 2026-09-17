class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} 

# Basically we checking if the diff + n = target but reverse order and we do that
#By putting the answer in map and if its in there then we return it.
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return