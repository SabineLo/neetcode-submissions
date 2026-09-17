class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #hashset or a fast and slow pointer
        #I have an idea for the fast and slow pointer but i see that it would fail
        #I can sort it and use hashmap but if I want 0(1) space complexity 
        #But the logic would be when slow == fast value I would turn the value
        #Issue: Might not for every case, I have different starting points check them and then move?
        #Loop will end early
        seen = set()
        nums = sorted(nums)
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1