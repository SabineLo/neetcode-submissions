class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Break down
        #Giving me an array and its giving me a target and i have to get the numbers
        #in the array that add up to target but i dont just get the numbers i get the position of them
    #[3,4,5,6]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): 
                if nums[i] + nums[j] == target:
                    return [i,j]
