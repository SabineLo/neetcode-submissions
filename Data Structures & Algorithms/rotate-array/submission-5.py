class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #splice it by how many in k and move it to the end and keep the front section back 
        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]
                    #gets me the end   #gets me the start section

        #so basically me saying rotate it 4 times means give me the last 4 and put to front and i could do postivie k but idk what index the last 4 would be so easier to just do - to get the last 4 and then we divide it by % len(nums) because if we rotate it the len(nums) of time bring us back to original so then tells us to just rotate it x amount more times