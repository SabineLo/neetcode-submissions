class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input - list of numbers
        #return - a number that symbolizes how long there has been a consecutive sequence, 
        #Reminder - dont have to be consecutive in original array
        #we can sort it from smallest to biggest
        numSet = set(nums) #basically sorting it getting rid of duplicates! didnt know we could do that 
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet: #this just gets me started?
                length = 1
                while(num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest