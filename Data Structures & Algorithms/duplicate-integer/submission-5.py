class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #does not allow us to have duplicates
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False