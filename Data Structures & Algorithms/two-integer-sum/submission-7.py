class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #find two numbers that add up to target return the indices []
        prevAnswers = defaultdict(int) #I only wanna go through this once so i use this?
        #This means that my key is the number and mmy value is the index
        for i,n in enumerate(nums): # So i wanna make sure i get the number and index in this first try
            # n + prevAnswer = target
            diff = target - n
            if diff in prevAnswers:
                return([prevAnswers[diff], i])
            prevAnswers[n] = i




