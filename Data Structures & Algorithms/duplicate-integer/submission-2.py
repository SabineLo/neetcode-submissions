class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Goal: Find if anything more then once and return boolean
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False