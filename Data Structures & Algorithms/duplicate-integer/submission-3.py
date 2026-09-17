class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return boolean
        #input list
        #Goal: If there is a repeat return true
        seen = set() #Unique values
        #Why am I using a set rather then a list if its the same functionality 
            #Set → O(1) average time
            #Sets use a hash table internally, so checking for membership is basically 
            #instant (no scanning through all elements).
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

