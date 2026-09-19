class Solution:
    def findMin(self, nums: List[int]) -> int:
    #inefficient -> to just find min
    #instead break into parts and search rather then searching whole thing
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (r + l) // 2 
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

