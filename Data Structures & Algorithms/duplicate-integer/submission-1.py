class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         #another way to do it which is similar to hash set is array just have one 
         #that is already seen
         seen = []
         for num in nums:
            if num in seen:
                return True
            seen.append(num)
         return False