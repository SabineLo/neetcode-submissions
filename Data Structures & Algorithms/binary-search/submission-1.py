class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Our array is sorted in ascending order, and we have a target 
        #In order to search more efficiently instead of going through everything on list 
        #We can find its approximate location and search there
        #[0,1,2,3,9]
        l_ptr = 0
        r_ptr = len(nums) -1

        while l_ptr <= r_ptr:
            m_index = (r_ptr + l_ptr)//2
            # If our middle is greater then the target we have to check the left side
            if(nums[m_index] > target):
                r_ptr = m_index - 1
            elif(nums[m_index] < target):
                l_ptr = m_index + 1
            else:
                return m_index
        return -1





            