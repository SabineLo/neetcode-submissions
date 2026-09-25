class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input - list of numbers
        #return - a number that symbolizes how long there has been a consecutive sequence, 
        numSet = set(nums)
        longest = 0 

        for num in nums:
            if (num - 1 not in numSet):
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(length,longest)
        return longest
                