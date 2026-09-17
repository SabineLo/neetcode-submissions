class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSeen = set()
        for num in nums:
            if num in numSeen:
                return True
            numSeen.add(num)
        return False