class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input - list of numbers
        #return - a number that symbolizes how long there has been a consecutive sequence, 
        #goals - find the beginning of the consecutive sequence and keep building from there
        numSet = set(nums)
        count = 0

        for num in nums:
            if (num - 1) not in numSet: #begnning of sequence
                length = 1
                while (num + length) in numSet: #looking for the consecutive sequence
                    length += 1
                count = max(count,length)
        return count